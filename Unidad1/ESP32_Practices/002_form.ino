#include <WiFi.h>
#include <WebServer.h>

const char* ssid     = "TU_SSID";
const char* password = "TU_PASSWORD";

WebServer server(80);

// Página HTML con formulario y dos botones
const char MAIN_page[] PROGMEM = R"=====(
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>ESP32 Formulario</title>
</head>
<body>
  <h1>Control ESP32</h1>
  <p>Selecciona una acción y envía el formulario.</p>

  <form action="/accion" method="GET">
    <label>Valor:</label>
    <input type="number" name="valor">

    <br><br>

    <!-- Dos botones que envían el mismo formulario -->
    <button type="submit" name="accion" value="encender">Encender</button>
    <button type="submit" name="accion" value="apagar">Apagar</button>
  </form>
</body>
</html>
)=====";

// Pin de ejemplo a controlar
const int ledPin = 2;

void handleRoot() {
  server.send(200, "text/html", MAIN_page);
}

// Maneja la ruta /accion (cuando se envía el formulario)
void handleAccion() {
  String accion = "";
  String valor  = "";

  if (server.hasArg("accion")) {
    accion = server.arg("accion");
  }
  if (server.hasArg("valor")) {
    valor = server.arg("valor");
  }

  Serial.print("Accion: ");
  Serial.println(accion);
  Serial.print("Valor: ");
  Serial.println(valor);

  // Ejemplo de uso: encender/apagar LED
  if (accion == "encender") {
    digitalWrite(ledPin, HIGH);
  } else if (accion == "apagar") {
    digitalWrite(ledPin, LOW);
  }

  // Respuesta simple al navegador
  String message = "<html><body>";
  message += "<h1>Accion recibida</h1>";
  message += "<p>Accion: " + accion + "</p>";
  message += "<p>Valor: " + valor + "</p>";
  message += "<p><a href=\"/\">Volver</a></p>";
  message += "</body></html>";

  server.send(200, "text/html", message);
}

void setup() {
  Serial.begin(115200);
  pinMode(ledPin, OUTPUT);

  WiFi.begin(ssid, password);
  Serial.print("Conectando a WiFi");
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWiFi conectado");
  Serial.print("IP: ");
  Serial.println(WiFi.localIP());

  // Rutas
  server.on("/", handleRoot);          // Página principal con formulario
  server.on("/accion", handleAccion);  // Procesa el formulario

  server.begin();
  Serial.println("Servidor HTTP iniciado");
}

void loop() {
  server.handleClient();
}
