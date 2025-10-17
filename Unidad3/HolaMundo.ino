void setup() {
  Serial.begin(115200);              // Inicia la comunicación serial a 115200 baudios
  Serial.println("Hola Mundo!");    // Imprime el mensaje en la terminal
}

void loop() {
  Serial.println("Hola Mundo!");    // Muestra el mensaje repetidamente
  delay(1000);                      // Espera 1 segundo antes de repetir
}