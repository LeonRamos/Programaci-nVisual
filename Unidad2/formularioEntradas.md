***

## 1. Campos de texto: Entry

El widget `Entry` permite ingresar datos de una sola línea, como valores de sensores, contraseñas o claves de acceso.

**Ejemplo: Entrada de valor y validación**

```python
import tkinter as tk

def enviar():
    valor = entry.get()
    if valor.isdigit():
        label_estado.config(text=f"Valor almacenado: {valor}")
    else:
        label_estado.config(text="Solo números permitidos")

root = tk.Tk()
root.title("Entrada y validación de datos")

entry = tk.Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
boton = tk.Button(root, text="Enviar", command=enviar)
boton.grid(row=0, column=1, padx=5, pady=5)

label_estado = tk.Label(root, text="Esperando datos...")
label_estado.grid(row=1, column=0, columnspan=2)

root.mainloop()
```

Este código valida que sólo se acepten valores numéricos, útil para formularios de configuración de sensores.

***

## 2. Spinbox: Selección numérica rápida

`Spinbox` permite seleccionar rápidamente valores de un rango, ideal para configurar parámetros como tiempos, frecuencias o canales.

**Ejemplo: Selección de canal digital**

```python
import tkinter as tk

def seleccionar_canal():
    canal = spin.get()
    label.set(f"Canal digital seleccionado: {canal}")

root = tk.Tk()
root.title("Configuración de canal")

spin = tk.Spinbox(root, from_=1, to=8)
spin.pack(pady=5)
tk.Button(root, text="Seleccionar", command=seleccionar_canal).pack()
label = tk.StringVar()
tk.Label(root, textvariable=label).pack(pady=5)

root.mainloop()
```

Perfecto para elegir canales electrónicos en embebidos o IoT.

***

## 3. Combobox: Selección de lista predeterminada

`Combobox` (de `ttk`) muestra un desplegable para elegir opciones, útil para seleccionar tipo de sensor, modo de operación o país.

**Ejemplo: Selección de tipo de sensor**

```python
import tkinter as tk
from tkinter import ttk

def elegir_sensor(event=None):
    seleccion = combo.get()
    etiqueta.set(f"Tipo de sensor: {seleccion}")

root = tk.Tk()
root.title("Selección de sensor")

lista = ["Temperatura", "Luminosidad", "Humedad", "Movimiento"]
combo = ttk.Combobox(root, values=lista, state="readonly")
combo.pack(pady=5)
combo.bind("<<ComboboxSelected>>", elegir_sensor)
etiqueta = tk.StringVar()
ttk.Label(root, textvariable=etiqueta).pack(pady=5)

root.mainloop()
```

Ideal para formularios donde se elige el dispositivo conectado.

***

## 4. Mensajes informativos y retroalimentación

Puedes usar `showinfo`, `showerror` de `tkinter.messagebox` para mostrar alertas y feedback al usuario en formularios.

**Ejemplo: Mensaje al guardar configuración**

```python
import tkinter as tk
from tkinter import messagebox

def guardar():
    messagebox.showinfo("Configuración", "La configuración se guardó correctamente.")

root = tk.Tk()
root.title("Formulario IoT")
tk.Button(root, text="Guardar", command=guardar).pack(pady=20)

root.mainloop()
```


***

## 5. Validación avanzada en tiempo real

Con `validatecommand` puedes restringir directamente lo que el usuario ingresa (ideal para entradas críticas en hardware digital).

**Ejemplo: Entrada numérica restringida**

```python
import tkinter as tk

def solo_numeros(P):
    return P.isdigit()

root = tk.Tk()
root.title("Validación en tiempo real")

vcmd = (root.register(solo_numeros), "%P")
entry = tk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(padx=10, pady=10)

root.mainloop()
```

Se evita que el usuario ingrese caracteres no válidos desde el inicio.

***

### Aplicaciones típicas en electrónica, embebidos e IoT

- Configuración de sensores y canales digitales.
- Selección de modo de operación y tipo de dispositivo.
- Validación de parámetros críticos para evitar fallos de hardware.
- Formularios de acceso y registro en aplicaciones IoT.

Estos componentes y técnicas permiten crear formularios robustos, intuitivos y seguros en proyectos reales de electrónica digital y sistemas embebidos.