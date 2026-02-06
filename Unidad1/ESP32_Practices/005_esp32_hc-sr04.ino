#include <WiFi.h>
#include <WebServer.h>

// WiFi
const char* ssid     = "TU_SSID";
const char* password = "TU_PASSWORD";

// Ultrasonico
const int trigPin = 5;
const int echoPin = 18;

// Semaforo
const int ledVerde    = 23;
const int ledAmarillo = 22;
const int ledRojo     = 21;

WebServer server(80);

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

void actualizarSemaforo(float d) {
  digitalWrite(ledVerde, LOW);
  digitalWrite(ledAmarillo, LOW);
  digitalWrite(ledRojo, LOW);

  if (d < 20) {          // Cerca
    digitalWrite(ledRojo, HIGH);
  } else if (d < 80) {   // Media
    digitalWrite(ledAmarillo, HIGH);
  } else {               // Lejos
    digitalWrite(ledVerde, HIGH);
  }
}

const char MAIN_page[] PROGMEM = R"=====( 
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ESP32 - Distancia HC-SR04</title>
  <style>
    body { font-family: Arial; background:#111; color:#eee; text-align:center; }
    .card { background:#222; padding:20px; border-radius:10px; display:inline-block; margin-top:40px; }
    .distance { font-size:48px; margin:10px 0; }
    .bar-container { width:80%; height:30px; background:#444; margin:0 auto; border-radius:15px; overflow:hidden; }
    .bar { height:100%; width:0; background:#4caf50; transition:width 0.3s, background 0.3s; }
    #status { margin-top:10px; font-size:20px; }
  </style>
</head>
<body>
  <h1>ESP32 + HC-SR04 + Semáforo</h1>
  <div class="card">
    <h2>Distancia medida</h2>
    <div id="distance" class="distance">-- cm</div>
    <div class="bar-container">
      <div id="bar" class="bar"></div>
    </div>
    <p id="status">Esperando lectura...</p>
  </div>

  <script>
    function updateDistance() {
      fetch("/distance")
        .then(response => response.text())
        .then(text => {
          const d = parseFloat(text);
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
        })
        .catch(err => {
          document.getElementById("status").innerText = "Error leyendo distancia";
        });
    }

    setInterval(updateDistance, 1000);
    updateDistance();
  </script>
</body>
</html>
)=====";

void handleRoot() {
  server.send_P(200, "text/html", MAIN_page);
}

void handleDistance() {
  float d = getDistanceCm();
  actualizarSemaforo(d);              // Actualiza LEDs
  String s = String(d, 1);
  server.send(200, "text/plain", s);
}

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
  server.on("/distance", handleDistance);
  server.begin();
}

void loop() {
  server.handleClient();
}
