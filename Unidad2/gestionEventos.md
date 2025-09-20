***

## Introducción: ¿Qué es la gestión de eventos?

Una aplicación gráfica reacciona a acciones del usuario: hacer clic, escribir, mover el ratón, etc. En Tkinter, los eventos se manejan asociando funciones (“handlers”) a botones, campos de texto y otros widgets. Así, se puede capturar un comando, leer un dato en tiempo real o actualizar la información de la UI.

***

## 1. Asociando funciones a botones – parámetro command

El método más directo para eventos es el parámetro `command`:

```python
import tkinter as tk

def encender_led():
    label_estado.config(text="LED encendido")

root = tk.Tk()
root.title("Panel de control electrónico")

label_estado = tk.Label(root, text="LED apagado")
label_estado.pack(pady=10)

btn_encender = tk.Button(root, text="Encender LED", command=encender_led)
btn_encender.pack(pady=5)

root.mainloop()
```

**Explicación:**
Cuando se pulsa el botón, se ejecuta la función encender_led. Esto actualiza el texto de la etiqueta de estado. Este patrón es fundamental para GUIs de control en electrónica.

***

## 2. Uso de StringVar e IntVar para entrada/salida

Las variables especiales `StringVar` o `IntVar` permiten que el contenido del widget cambie automáticamente según la variable y viceversa:

```python
import tkinter as tk

def actualizar_temperatura():
    valor = entrada_temp.get()
    etiqueta_temp.set(f"Temperatura registrada: {valor} °C")

root = tk.Tk()
root.title("Monitor de temperatura")

etiqueta_temp = tk.StringVar()
etiqueta_temp.set("Temperatura registrada: -- °C")

tk.Label(root, textvariable=etiqueta_temp).pack(pady=10)
entrada_temp = tk.Entry(root)
entrada_temp.pack(pady=5)
tk.Button(root, text="Actualizar", command=actualizar_temperatura).pack()

root.mainloop()
```

**Explicación:**
El usuario introduce un valor en el Entry y, al pulsar el botón, ese valor alimenta una etiqueta gracias al uso de `StringVar`. Este concepto facilita la interacción en interfaces embebidas con datos dinámicos.

***

## 3. Captura de eventos personalizados (bind)

Para interactuar en tiempo real (clic, teclado, etc.) se usa `bind`:

```python
import tkinter as tk

def mostrar_coordenadas(event):
    mensaje.set(f"Coordenadas del clic: x={event.x}, y={event.y}")

root = tk.Tk()
root.title("Lectura de clic en pantalla")

mensaje = tk.StringVar()
tk.Label(root, textvariable=mensaje, font=("Arial", 14)).pack(pady=10)

panel = tk.Frame(root, width=200, height=100, bg="#e0f2f1")
panel.pack(pady=10)
panel.bind("<Button-1>", mostrar_coordenadas)  # Captura clic izquierdo

root.mainloop()
```

**Explicación:**
El `bind` permite capturar eventos en cualquier widget. El ejemplo muestra cómo un clic en el panel actualiza las coordenadas en la interfaz, útil en proyectos donde se requiere interacción precisa como calibración de touchscreens o mapas de sensores.

***

## 4. Validar y actualizar automáticamente valores

Usando `StringVar`, se puede detectar y validar interacciones (muy usado para asegurar entradas numéricas):

```python
import tkinter as tk

def validar_numero(*args):
    valor = v_numero.get()
    if not valor.isdigit():
        estado.set("Solo números permitidos")
    else:
        estado.set("Valor válido")

root = tk.Tk()
root.title("Validación de entrada numérica")

v_numero = tk.StringVar()
v_numero.trace("w", validar_numero)  # Actualiza en cada cambio

tk.Entry(root, textvariable=v_numero).pack(pady=5)
estado = tk.StringVar(value="Esperando entrada...")
tk.Label(root, textvariable=estado).pack()

root.mainloop()
```

**Explicación:**
Cada vez que el usuario escribe, se ejecuta `validar_numero` porque la variable `v_numero` tiene un “trace”. Así se pueden prevenir fallos en entradas para sistemas embebidos sensibles.

***

## Aplicaciones típicas en electrónica y embebidos

- Pulsar botones virtuales para encender/apagar dispositivos reales.
- Introducir valores de calibración para sensores y ver validaciones inmediatas.
- Leer inmediato de coordenadas o estados usando paneles interactivos para simuladores o diagnósticos embebidos.

Estos mecanismos son la base de toda interfaz controlada por eventos, esencial en desarrollo de hardware con interacción gráfica.

 # Prácticas:
 1. Panel de encendido de salidas digitales
Caso: Diseña una interfaz con cuatro botones, cada uno controla el encendido de una salida digital (relé, LED, motor, etc.). Al presionar cada botón debe cambiar el estado mostrado en un Label (encendido/apagado) correspondiente. Simula el feedback típico de un panel de control embebido.

2. Lector e ingreso de valores analógicos de sensor
Caso: Crea una GUI con un Entry para ingresar el valor simulado de un sensor analógico (temperatura, luz, humedad). Un botón debe permitir capturar el valor, mostrarlo en una etiqueta y validar si está en un rango de operación seguro. Notifica alarmas si el valor está fuera del rango esperado (por ejemplo: 10°C-80°C).

3. Simulador básico de autenticación IoT
Caso: Implementa una pequeña pantalla donde el usuario debe ingresar una “clave” usando Entry y un botón para verificar. Si la clave coincide con una predefinida (por ejemplo, “iot2025”), muestra acceso concedido; si no, acceso denegado. Útil como interfaz de acceso simple para dispositivos conectados.

4. Selector de modo de operación con RadioButtons
Caso: Con una interfaz, permite al operador escoger entre varios modos de un sistema embebido (Manual, Automático, Mantenimiento) usando RadioButtons. Al cambiar el modo se actualiza una etiqueta con la descripción del estado seleccionado. Este patrón es común para elegir modos en PLCs, PLCs virtuales y sistemas de control.

5. Mini-monitor de estado de red o nodo IoT
Caso: Desarrolla una GUI que tenga un botón “Consultar estado” y un Label. Cada vez que se pulse, debe simular la consulta de un nodo/red IoT y mostrar un estado aleatorio (“En línea”, “Desconectado”, “Alerta”). Emplea eventos simples y actualización dinámica, como pantalla de monitoreo de dispositivos distribuidos.