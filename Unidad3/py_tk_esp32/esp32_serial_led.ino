/*
 * ESP32-WROOM-32: Control Serial de LED
 * Comunicación con Python Tkinter vía Puerto Serial
 * Autor: Proyecto Educativo
 * 
 * Comandos aceptados:
 * - 'H' o '1' → Encender LED
 * - 'L' o '0' → Apagar LED
 * - 'S' → Solicitar estado del LED
 * - 'T' → Solicitar temperatura simulada
 * - 'C' → Solicitar contador
 */

#define LED_PIN 2  // LED integrado del ESP32

bool ledState = false;
unsigned long lastUpdate = 0;
int contador = 0;

void setup() {
  // Inicializar comunicación serial a 115200 baudios
  Serial.begin(115200);
  
  // Configurar LED como salida
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  
  // Esperar un momento para estabilizar la conexión
  delay(1000);
  
  // Mensaje de bienvenida
  Serial.println("ESP32 READY");
  Serial.println("Commands: H=ON, L=OFF, S=Status, T=Temp, C=Count");
}

void loop() {
  // Verificar si hay datos disponibles en el puerto serial
  if (Serial.available() > 0) {
    char comando = Serial.read();
    procesarComando(comando);
  }
  
  // Enviar datos periódicamente cada 2 segundos
  if (millis() - lastUpdate >= 2000) {
    lastUpdate = millis();
    contador++;
    enviarDatosPeriodicos();
  }
}

/**
 * Procesa los comandos recibidos desde Python
 */
void procesarComando(char cmd) {
  switch (cmd) {
    case 'H':  // High - Encender LED
    case '1':
      digitalWrite(LED_PIN, HIGH);
      ledState = true;
      Serial.println("LED:ON");
      break;
      
    case 'L':  // Low - Apagar LED
    case '0':
      digitalWrite(LED_PIN, LOW);
      ledState = false;
      Serial.println("LED:OFF");
      break;
      
    case 'S':  // Status - Consultar estado del LED
      if (ledState) {
        Serial.println("STATUS:ON");
      } else {
        Serial.println("STATUS:OFF");
      }
      break;
      
    case 'T':  // Temperature - Enviar temperatura simulada
      {
        float tempSimulada = 20.0 + random(0, 100) / 10.0;
        Serial.print("TEMP:");
        Serial.println(tempSimulada, 1);
      }
      break;
      
    case 'C':  // Counter - Enviar contador
      Serial.print("COUNT:");
      Serial.println(contador);
      break;
      
    default:
      Serial.println("ERROR:Unknown command");
      break;
  }
}

/**
 * Envía datos periódicamente para monitoreo en tiempo real
 */
void enviarDatosPeriodicos() {
  // Temperatura simulada (20-30°C)
  float temp = 20.0 + random(0, 100) / 10.0;
  
  // Formato: DATA|temperatura|contador|estado_led
  Serial.print("DATA|");
  Serial.print(temp, 1);
  Serial.print("|");
  Serial.print(contador);
  Serial.print("|");
  Serial.println(ledState ? "ON" : "OFF");
}
