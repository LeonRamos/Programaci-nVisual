# formularios y entradas avanzadas

La creación de **formularios y entradas avanzadas** con Tkinter es una competencia clave para estudiantes de electrónica en su formación y en el desarrollo profesional. Los formularios permiten diseñar interfaces gráficas a través de las cuales los usuarios pueden ingresar, validar y procesar datos esenciales para la configuración, calibración y control de sistemas electrónicos, diseñar y documentar circuitos o gestionar el testing de hardware.

Tkinter hace posible implementar formularios robustos y visualmente intuitivos sin la necesidad de conocimientos profundos de frameworks complejos, facilitando el diseño de aplicaciones multiplataforma rápidas y ligeras. En electrónica y tecnologías emergentes, la capacidad de crear formularios facilita desde la configuración de parámetros en microcontroladores, selección de modos de trabajo para equipos, hasta el registro y validación de componentes y condiciones de prueba en entornos de laboratorio.

Dominar estos conceptos con Tkinter permite a los estudiantes:
- Interactuar profesionalmente con sistemas y prototipos embebidos desde una interfaz amigable.
- Disminuir errores humanos por validaciones en tiempo real.
- Integrar parámetros críticos, selección de modos y almacenamiento de configuraciones, todo desde una sola aplicación.
- Optimizar tareas de testing, diagnóstico y diseño digital, logrando resultados reproducibles y documentados de manera formal.

***

## Ejemplo 1: Configuración de un termostato digital (Spinbox + Validación)

```python
import tkinter as tk
from tkinter import ttk, messagebox

def configurar():
    temp = int(spin_temp.get())
    if temp < 10 or temp > 30:
        messagebox.showerror("Error", "Temperatura fuera del rango permitido (10-30°C)")
    else:
        if temp < 18:
            consumo = "Bajo"
        elif temp < 25:
            consumo = "Medio"
        else:
            consumo = "Alto"
        label_consumo.config(text=f"Consumo energético: {consumo}", fg={"Bajo":"green", "Medio":"orange", "Alto":"red"}[consumo])

root = tk.Tk()
root.title("Termostato digital embebido")

ttk.Label(root, text="Selecciona temperatura (°C):").grid(row=0, column=0, padx=8, pady=8)
spin_temp = ttk.Spinbox(root, from_=10, to=30, width=5)
spin_temp.set(22)
spin_temp.grid(row=0, column=1, padx=8, pady=8)

ttk.Button(root, text="Configurar", command=configurar).grid(row=1, column=0, columnspan=2, pady=8)
label_consumo = tk.Label(root, text="Consumo energético: --")
label_consumo.grid(row=2, column=0, columnspan=2, pady=8)

root.mainloop()
```

Aplicación en circuitos embebidos para configurar el punto de trabajo y validar condiciones críticas.

***

## Ejemplo 2: Selección de modo de test de hardware (Combobox)

```python
import tkinter as tk
from tkinter import ttk

def seleccionar_modo(event=None):
    modo = combo.get()
    label_resultado.config(text=f"Modo de test seleccionado: {modo}")

root = tk.Tk()
root.title("Selector de test electrónico")

ttk.Label(root, text="Modo de test:").pack(pady=5)
combo = ttk.Combobox(root, values=["Continuidad", "Voltaje", "Corriente", "Capacitancia"], state="readonly")
combo.pack(pady=5)
combo.current(0)
combo.bind("<<ComboboxSelected>>", seleccionar_modo)

label_resultado = ttk.Label(root, text="Modo de test seleccionado: --")
label_resultado.pack(pady=10)

root.mainloop()
```

Uso habitual en bancos de pruebas para seleccionar diferentes protocolos o técnicas de testeo electrónico.

***

## Ejemplo 3: Validación en tiempo real para entrada de componentes (Entry)

```python
import tkinter as tk
from tkinter import ttk

def es_codigo_valido(codigo):
    return codigo.isalnum() and len(codigo) >= 5

def validar(P):
    estado.set("Válido" if es_codigo_valido(P) else "Código inválido")
    return True

root = tk.Tk()
root.title("Registro de componente electrónico")

ttk.Label(root, text="Código de componente (>=5 caracteres)").pack()
estado = tk.StringVar(value="Esperando...")
vcmd = (root.register(validar), "%P")

entry = ttk.Entry(root, validate="key", validatecommand=vcmd)
entry.pack(pady=5)
ttk.Label(root, textvariable=estado).pack(pady=5)

root.mainloop()
```

Ideal en sistemas inventario para test e identificación de piezas en laboratorios.

***

## Ejemplo 4: Formulario emergente de configuración de circuito (Entry + Spinbox + Combobox)

```python
import tkinter as tk
from tkinter import ttk

def guardar_configuracion():
    tipo = cb_tipo.get()
    valor = entry_valor.get()
    tolerancia = spin_tol.get()
    if not valor.isdigit():
        resultado.config(text="El valor debe ser numérico", fg="red")
        return
    resultado.config(
        text=f"Circuito: {tipo}, Valor: {valor}, Tolerancia: {tolerancia}%",
        fg="green"
    )

root = tk.Tk()
root.title("Configurador de circuitos electrónicos")

ttk.Label(root, text="Tipo de componente:").grid(row=0, column=0)
cb_tipo = ttk.Combobox(root, values=["Resistor", "Condensador", "Inductor"], state="readonly")
cb_tipo.grid(row=0, column=1)
cb_tipo.current(0)

ttk.Label(root, text="Valor nominal:").grid(row=1, column=0)
entry_valor = ttk.Entry(root)
entry_valor.grid(row=1, column=1)

ttk.Label(root, text="Tolerancia (%):").grid(row=2, column=0)
spin_tol = ttk.Spinbox(root, from_=1, to=20)
spin_tol.set(5)
spin_tol.grid(row=2, column=1)

ttk.Button(root, text="Guardar", command=guardar_configuracion).grid(row=3, column=0, columnspan=2, pady=8)
resultado = tk.Label(root, text="Esperando configuración...", fg="blue")
resultado.grid(row=4, column=0, columnspan=2)

root.mainloop()
```

Frecuente en diseño de circuitos electrónicos y plataformas de hardware configurable.

***

## Ejemplo 5: Interface para test automático de sensores (Spinbox + Entry + Combobox + Validación)

```python
import tkinter as tk
from tkinter import ttk, messagebox

def testear_sensor():
    tipo = cb_tipo.get()
    rango = int(spin_rango.get())
    unidad = entry_unidad.get()
    if not unidad or any(c.isdigit() for c in unidad):
        messagebox.showerror("Error", "Ingresa una unidad válida (sin números).")
        return
    messagebox.showinfo(
        "Test realizado",
        f"Sensor: {tipo}\nRango máximo: {rango} {unidad}\nTest finalizado correctamente."
    )

root = tk.Tk()
root.title("Test automático de sensores")

ttk.Label(root, text="Tipo de sensor:").grid(row=0, column=0)
cb_tipo = ttk.Combobox(root, values=["Temperatura", "Presión", "Humedad"], state="readonly")
cb_tipo.grid(row=0, column=1)
cb_tipo.current(0)

ttk.Label(root, text="Rango máximo:").grid(row=1, column=0)
spin_rango = ttk.Spinbox(root, from_=1, to=100)
spin_rango.set(50)
spin_rango.grid(row=1, column=1)

ttk.Label(root, text="Unidad:").grid(row=2, column=0)
entry_unidad = ttk.Entry(root)
entry_unidad.grid(row=2, column=1)

ttk.Button(root, text="Testear", command=testear_sensor).grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
```

Ideal para bancos de test de tecnologías emergentes en sensores digitales.

***

