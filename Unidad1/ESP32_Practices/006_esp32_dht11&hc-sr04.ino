#include <WiFi.h>
#include <WebServer.h>
#include "DHT.h"

// ---------- WiFi ----------
const char* ssid     = "TU_SSID";
const char* password = "TU_PASSWORD";

// ---------- Ultrasonico ----------
const int trigPin = 5;
const int echoPin = 18;

// ---------- Semaforo ----------
const int ledVerde    = 23;
const int ledAmarillo = 22;
const int ledRojo     = 21;

// ---------- DHT ----------
#define DHTPIN 4
#define DHTTYPE DHT11   // o DHT22
DHT dht(DHTPIN, DHTTYPE);

WebServer server(80);

float temperatura = 0;
float humedad = 0;

// ---------- Funciones de sensores ----------
float getDistanceCm() {
  long duration;
  float distance;

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  duration = pulseIn(echoPin, HIGH, 30000);
  distance = (duration * 0.034) / 2.0;
  return distance;
}

void leerDHT() {
  float h = dht.readHumidity();
  float t = dht.readTemperature(); // °C

  if (!isnan(h) && !isnan(t)) {
    humedad = h;
    temperatura = t;
  } else {
    Serial.println("Error leyendo DHT");
  }
}

void actualizarSemaforo(float d) {
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarillo, LOW);
  digitalWrite(ledRojo, LOW);

  if (d < 20) {
    digitalWrite(ledRojo, HIGH);
  } else if (d < 80) {
    digitalWrite(ledAmarillo, HIGH);
  } else {
    digitalWrite(ledVerde, HIGH);
  }
}

// ---------- Página HTML ----------
const char MAIN_page[] PROGMEM = R"=====( 
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ESP32 - Distancia y Ambiente</title>
  <style>
    body { font-family: Arial; background:#111; color:#eee; text-align:center; }
    .container { margin-top:30px; }
    .card { background:#222; padding:20px; border-radius:10px; display:inline-block; margin:10px; min-width:260px; }
    .distance { font-size:48px; margin:10px 0; }
    .bar-container { width:80%; height:30px; background:#444; margin:0 auto; border-radius:15px; overflow:hidden; }
    .bar { height:100%; width:0; background:#4caf50; transition:width 0.3s, background 0.3s; }
    #status { margin-top:10px; font-size:20px; }
  </style>
</head>
<body>
  <h1>ESP32 + HC-SR04 + DHT11 + Semáforo</h1>

  <div class="container">
    <div class="card">
      <h2>Distancia</h2>
      <div id="distance" class="distance">-- cm</div>
      <div class="bar-container">
        <div id="bar" class="bar"></div>
      </div>
      <p id="status">Esperando lectura...</p>
    </div>

    <div class="card">
      <h2>Ambiente</h2>
      <div>Temperatura: <span id="temp">--</span> °C</div>
      <div>Humedad: <span id="hum">--</span> %</div>
    </div>
  </div>

  <script>
    function updateData() {
      fetch("/data")
        .then(response => response.text())
        .then(text => {
          const parts = text.split(",");
          const d = parseFloat(parts[0]);
          const t = parseFloat(parts[1]);
          const h = parseFloat(parts[2]);

          // Distancia
          if (!isNaN(d)) {
            document.getElementById("distance").innerText = d.toFixed(1) + " cm";

            let percent = d;
            if (percent < 0) percent = 0;
            if (percent > 200) percent = 200;
            percent = (percent / 200) * 100;

            const bar = document.getElementById("bar");
            bar.style.width = percent + "%";

            if (d < 20) {
              bar.style.background = "#f44336";
              document.getElementById("status").innerText = "¡Muy cerca! (Rojo)";
            } else if (d < 80) {
              bar.style.background = "#ff9800";
              document.getElementById("status").innerText = "Distancia media (Amarillo)";
            } else {
              bar.style.background = "#4caf50";
              document.getElementById("status").innerText = "Lejos (Verde)";
            }
          }

          // Temperatura y humedad
          if (!isNaN(t)) {
            document.getElementById("temp").innerText = t.toFixed(1);
          }
          if (!isNaN(h)) {
            document.getElementById("hum").innerText = h.toFixed(1);
          }
        })
        .catch(err => {
          document.getElementById("status").innerText = "Error leyendo datos";
        });
    }

    setInterval(updateData, 1000);
    updateData();
  </script>
</body>
</html>
)=====";

// ---------- Handlers ----------
void handleRoot() {
  server.send_P(200, "text/html", MAIN_page);
}

void handleData() {
  float d = getDistanceCm();
  actualizarSemaforo(d);
  leerDHT();

  String payload = String(d, 1) + "," + String(temperatura, 1) + "," + String(humedad, 1);
  server.send(200, "text/plain", payload);
}

// ---------- SETUP / LOOP ----------
void setup() {
  Serial.begin(115200);

  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);

  pinMode(ledVerde, OUTPUT);
  pinMode(ledAmarillo, OUTPUT);
  pinMode(ledRojo, OUTPUT);

  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarillo, LOW);
  digitalWrite(ledRojo, LOW);

  dht.begin();

  WiFi.begin(ssid, password);
  Serial.print("Conectando");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  server.on("/", handleRoot);
  server.on("/data", handleData);
  server.begin();
}

void loop() {
  server.handleClient();
}
