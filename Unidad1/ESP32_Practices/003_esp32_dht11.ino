#include "DHT.h"

#define DHTPIN 4        // Pin donde conectas DATA
#define DHTTYPE DHT11   // Tipo de sensor

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(115200);
  Serial.println("Lectura DHT11 con ESP32");
  dht.begin();
}

void loop() {
  delay(2000); // El DHT11 es lento

  float humedad = dht.readHumidity();
  float temperatura = dht.readTemperature(); // Celsius

  if (isnan(humedad) || isnan(temperatura)) {
    Serial.println("Error al leer el sensor DHT11");
    return;
  }

  Serial.print("Humedad: ");
  Serial.print(humedad);
  Serial.print(" %\t");

  Serial.print("Temperatura: ");
  Serial.print(temperatura);
  Serial.println(" °C");
}
