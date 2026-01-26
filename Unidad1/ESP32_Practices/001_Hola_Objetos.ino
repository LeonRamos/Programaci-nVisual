#include <WiFi.h>
#include <WebServer.h>

const char* ssid     = "TU_SSID";
const char* password = "TU_PASSWORD";

WebServer server(80);

// Página HTML sencilla
const char MAIN_page[] PROGMEM = R"=====(
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ESP32 Web</title>
</head>
<body>
  <h1>Hola desde ESP32</h1>
  <p>Esta es una ventana HTML sencilla.</p>
  <button onclick="alert('Botón presionado')">Click</button>
</body>
</html>
)=====";

void handleRoot() {
  server.send(200, "text/html", MAIN_page);
}

void setup() {
  Serial.begin(115200);

  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP()); // Abre esta IP en el navegador

  server.on("/", handleRoot);     // Ruta principal
  server.begin();
}

void loop() {
  server.handleClient();          // Atiende peticiones HTTP
}
