#include <WiFi.h>
#include <WebServer.h>
#include "DHT.h"

// -------- WIFI --------
const char* ssid = "TU SIDD";
const char* password = "PASSWORD";

// -------- DHT --------
#define DHTPIN 4
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);

// -------- WEB SERVER --------
WebServer server(80);

// -------- HTML --------
const char index_html[] PROGMEM = R"rawliteral(
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>ESP32 DHT11</title>
  <style>
    body {
      font-family: Arial;
      text-align: center;
      background: #111;
      color: #fff;
    }
    .card {
      background: #222;
      padding: 20px;
      margin: 40px auto;
      width: 300px;
      border-radius: 10px;
      box-shadow: 0 0 10px #00ffcc;
    }
    h1 { color: #00ffcc; }
    .value {
      font-size: 2.5em;
    }
  </style>
</head>
<body>
  <div class="card">
    <h1>ESP32 DHT11</h1>
    <p> Temperatura</p>
    <div class="value"><span id="temp">--</span> °C</div>
    <p> Humedad</p>
    <div class="value"><span id="hum">--</span> %</div>
  </div>

<script>
setInterval(() => {
  fetch("/data")
    .then(response => response.json())
    .then(data => {
      document.getElementById("temp").innerHTML = data.temperature;
      document.getElementById("hum").innerHTML = data.humidity;
    });
}, 2000);
</script>
</body>
</html>
)rawliteral";

// -------- HANDLERS --------
void handleRoot() {
  server.send(200, "text/html", index_html);
}

void handleData() {
  float t = dht.readTemperature();
  float h = dht.readHumidity();

  if (isnan(t) || isnan(h)) {
    server.send(500, "application/json", "{\"error\":\"DHT error\"}");
    return;
  }

  char json[100];
  snprintf(json, sizeof(json),
           "{\"temperature\":%.2f,\"humidity\":%.2f}", t, h);

  server.send(200, "application/json", json);
}

void setup() {
  Serial.begin(115200);
  dht.begin();

  // WiFi
  WiFi.begin(ssid, password);
  Serial.print("Conectando WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nWiFi conectado");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  // Rutas
  server.on("/", handleRoot);
  server.on("/data", handleData);

  server.begin();
  Serial.println("Servidor web iniciado");
}

void loop() {
  server.handleClient();
}
