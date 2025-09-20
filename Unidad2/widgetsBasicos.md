## 1. Definición de los principales widgets básicos

- **Label**: Muestra texto o imágenes fijas en la interfaz. Ideal para títulos, descripciones o valores en tiempo real.
- **Button**: Botón que ejecuta una acción cuando se presiona. Fundamental para enviar comandos o controlar dispositivos.
- **Entry**: Caja de texto de una sola línea para entrada de datos (nombres, contraseñas, valores numéricos).
- **Frame**: Contenedor para organizar y agrupar otros widgets. Útil para secciones de la UI y paneles lógicos.

***

## 2. Métodos de colocación: pack, grid y place

- **pack()**
    - Organiza widgets en bloques, uno tras otro (vertical u horizontal).
    - Rápido para layouts simples como columnas/barras laterales.
    - Ejemplo:

```python
etiqueta.pack(side="top")
boton.pack(side="left")
```

- **grid()**
    - Distribuye widgets en una cuadrícula (filas y columnas).
    - Preciso para formularios, paneles de control o dashboards electrónicos.
    - Ejemplo:

```python
entrada.grid(row=0, column=0)
boton.grid(row=0, column=1)
```

- **place()**
    - Permite ubicar widgets en coordenadas absolutas o relativas dentro de la ventana.
    - Útil para UIs personalizadas, mapas o displays gráficos.
    - Ejemplo:

```python
etiqueta.place(x=50, y=30)
```


***

## 3. Ejercicios prácticos

### Ejercicio 1: Mostrar datos de un sensor

```python
import tkinter as tk

root = tk.Tk()
root.title("Monitor de Sensor Embebido")
# Simula la lectura de un sensor
valor_sensor = 36.8

etiqueta = tk.Label(root, text=f"Valor del sensor: {valor_sensor} °C", font=("Arial", 14))
etiqueta.pack(pady=10)

root.mainloop()
```

Este ejemplo muestra cómo usar un Label para visualizar el valor leído por un sensor embebido.

***

### Ejercicio 2: Entrada y envío de comandos

```python
import tkinter as tk

def send_command():
    comando = entry.get()
    label_status.config(text=f"Comando enviado: {comando}")

root = tk.Tk()
root.title("Control Electrónico")

entry = tk.Entry(root, width=20)
entry.grid(row=0, column=0, padx=5, pady=5)

btn_send = tk.Button(root, text="Enviar", command=send_command)
btn_send.grid(row=0, column=1, padx=5, pady=5)

label_status = tk.Label(root, text="Esperando comando...")
label_status.grid(row=1, column=0, columnspan=2, pady=5)

root.mainloop()
```

Este ejercicio dice cómo capturar datos con Entry y accionar un Button en una interfaz de control.

***

### Ejercicio 3: Agrupar botones para selección rápida usando Frame

```python
import tkinter as tk

root = tk.Tk()
root.title("Selección de Modo de Operación")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack(pady=10)

tk.Label(frame, text="Selecciona el modo:").pack()

btn_manual = tk.Button(frame, text="Manual")
btn_manual.pack(side="left", padx=5)
btn_auto = tk.Button(frame, text="Automático")
btn_auto.pack(side="left", padx=5)

root.mainloop()
```

Aquí se utiliza Frame para organizar varios botones relacionados, típico en paneles de control.

***

## 4. Personalización UI para electrónica y embebidos

- Utiliza colores de fondo neutros u oscuros para reducir el cansancio visual en displays de laboratorio.
- Ajusta fuentes (tipo y tamaño) para buena legibilidad en ambientes técnicos y displays pequeños.
- Usa Frames y cuadrículas (`grid`) para separar controles críticos (ej. comando de emergencia vs. información del sistema).
- Apóyate en imágenes o íconos en botones y etiquetas para identificación rápida (ej. iconos de encendido/apagado o alarma).
- Considera el tamaño de botones/gráficos acorde a pantallas táctiles, muy comunes en sistemas embebidos.

Estos conceptos garantizan que tu interfaz sea funcional, estética y segura para aplicaciones de ingeniería electrónica y sistemas embebidos.

---