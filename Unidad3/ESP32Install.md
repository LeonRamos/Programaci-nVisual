[![Arduino IDE](https://img.shields.io/badge/Arduino-IDE-blue?logo=arduino)](https://www.arduino.cc/en/software)
[![ESP32](https://img.shields.io/badge/ESP32-supported-brightgreen?logo=espressif)](https://www.espressif.com/en/products/socs/esp32)
[![Windows 11](https://img.shields.io/badge/Windows-11-informational?logo=windows)](https://www.microsoft.com/es-mx/windows/windows-11)

# Tutorial: Instala Arduino IDE y comunica tu ESP32

Este tutorial te guiará **paso a paso** para instalar el Arduino IDE y preparar tu placa ESP32 en Windows 11. ¡Está pensado para primaria! Al final, tendrás tu programa "Hola Mundo" funcionando en el monitor serial.

***
## 1. Descarga e instala Arduino IDE

- Ve a la página oficial y descarga el instalador para Windows 10 o superior.
  - [Descargar Arduino IDE](https://www.arduino.cc/en/software)
- Ejecuta el archivo `.exe` descargado.
- Haz clic en "Acepto" y sigue el asistente (puedes elegir instalar para todos los usuarios).
- Espera que termine la instalación. ¡Listo!

> **TIP:** Si tienes dudas, mira [este tutorial en video](https://www.youtube.com/watch?v=kbHthBL8LW8).

***
## 2. Instala los drivers USB para ESP32

La mayoría de ESP32 usan el chip **CP210x** (de Silicon Labs). Sin el driver, Windows no verá la placa.

- Descarga el driver de Silicon Labs: [Driver CP210x USB para Windows](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
- Descomprime el archivo (si está en ZIP).
- Haz doble clic en `CP210xVCPInstaller_x64.exe` para instalar.
- Sigue los pasos del asistente y acepta los términos.

> Si tu placa usa otro chip (p.ej. CH340), busca ese driver específico.

***
## 3. Conecta el ESP32

- Usa un cable USB **de datos** (no solo carga).
- Abre el "Administrador de dispositivos".
- Busca el puerto COM (debería llamarse "Silicon Labs CP210x USB to UART Bridge", por ejemplo COM5).

Si no aparece ningún puerto:
- Prueba otro cable USB.
- Reinicia el ordenador.
- Verifica que la placa y el cable funcionan en otro PC.

***
## 4. Instala el soporte para ESP32 en Arduino IDE

- Abre Arduino IDE.
- Ve a **Herramientas > Placa > Gestor de placas...**
- Busca "ESP32" y haz clic en "Instalar".
- Luego, en **Herramientas > Placa**, selecciona tu modelo de ESP32 (p.ej. "ESP32 Dev Module").

***
## 5. Selecciona el puerto correcto

- Ve a **Herramientas > Puerto** y elige el puerto COM que ves en el Administrador de dispositivos.

***
## 6. Escribe tu programa "Hola Mundo"

Copía este ejemplo y pégalo en Arduino IDE:

```cpp
void setup() {
  Serial.begin(115200);
  Serial.println("Saludos – Mi primer programa en ESP32");
}

void loop() {
  Serial.println("Hola Mundo");
  delay(1000);
}
```

***
## 7. Carga el programa y abre el monitor serial

- Haz clic en **Verificar** (√) para compilar.
- Haz clic en **Cargar** (→) para grabar el código.
- Abre **Herramientas > Monitor serial**.
- Elige la velocidad de 115200 baudios.
- Deberías ver que aparece "Saludos – Mi primer programa en ESP32" y luego "Hola Mundo" cada segundo.

***
## 8. ¡Listo! Revisa problemas

Si no ves mensajes:
- Revisa el puerto y la velocidad.
- Presiona el botón **RESET** en la placa ESP32.
- Revisa los pasos anteriores de drivers y cables.

***
## Enlaces útiles
- [Arduino IDE oficial](https://www.arduino.cc/en/software)
- [Driver CP210x USB](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers)
- [Tutorial “Hola Mundo” ESP32](https://acortes.co/esp32-hola-mundo-2/)

*