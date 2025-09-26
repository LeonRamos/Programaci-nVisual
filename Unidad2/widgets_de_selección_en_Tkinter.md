
# interfaces gráficas de usuario (GUI)

Tkinter es la biblioteca estándar de Python para la creación de **interfaces gráficas de usuario (GUI)** en aplicaciones de escritorio, ampliamente empleada en electrónica, sistemas embebidos e IoT debido a su simplicidad y potencia. Gracias a sus widgets básicos y avanzados —como botones, etiquetas, cajas de texto, opciones de selección y menús desplegables— permite construir rápidamente formularios, paneles de control y herramientas visuales que facilitan la configuración, monitoreo y testing de hardware o tecnologías emergentes.

La facilidad para asociar eventos y responder al usuario a través de la UI convierte a Tkinter en una opción ideal para docentes, ingenieros y makers que buscan integrar software y hardware, gestionar dispositivos digitales, validar datos o automatizar pruebas directamente desde un entorno visual y portable. Su diseño por componentes permite organizar eficazmente la interfaz en proyectos complejos, mientras que su compatibilidad multiplataforma asegura el despliegue en diversos equipos y entornos de desarrollo.

En este contexto, aprender a manejar formularios, entradas avanzadas y widgets de selección con Tkinter constituye una herramienta clave para el desarrollo de aplicaciones modernas en electrónica digital, diseño de circuitos, laboratorios de prueba e integración de tecnologías emergentes.

## Ejemplo 1: Selección de modo de trabajo mediante RadioButton

Ideal para seleccionar un solo modo entre varias opciones exclusivas, como Manual/Automático en sistemas embebidos.

```python
import tkinter as tk

def actualizar_modo():
    label_resultado.config(text=f"Modo seleccionado: {modo.get()}")

root = tk.Tk()
root.title("Modo de operación - Electrónica")

modo = tk.StringVar(value="Manual")
tk.Label(root, text="Elige el modo de trabajo:").pack()
tk.Radiobutton(root, text="Manual", variable=modo, value="Manual", command=actualizar_modo).pack(anchor="w")
tk.Radiobutton(root, text="Automático", variable=modo, value="Automático", command=actualizar_modo).pack(anchor="w")
tk.Radiobutton(root, text="Diagnóstico", variable=modo, value="Diagnóstico", command=actualizar_modo).pack(anchor="w")
label_resultado = tk.Label(root, text="Modo seleccionado: Manual")
label_resultado.pack(pady=10)
root.mainloop()
```
Este patrón permite que el usuario seleccione un único estado operativo, esencial para PLCs virtuales o software de bancos de prueba.

***

## Ejemplo 2: Activar/desactivar canales digitales con CheckButton

Permite elegir múltiples canales a activar, ideal para paneles digitales de control.

```python
import tkinter as tk

def mostrar_canales():
    seleccionados = []
    if c1.get(): seleccionados.append("CH1")
    if c2.get(): seleccionados.append("CH2")
    if c3.get(): seleccionados.append("CH3")
    label_estado.config(text="Canales activos: " + ", ".join(seleccionados) if seleccionados else "Ninguno")

root = tk.Tk()
root.title("Activación de canales digitales")

c1, c2, c3 = tk.IntVar(), tk.IntVar(), tk.IntVar()
tk.Checkbutton(root, text="Canal 1", variable=c1, command=mostrar_canales).pack(anchor="w")
tk.Checkbutton(root, text="Canal 2", variable=c2, command=mostrar_canales).pack(anchor="w")
tk.Checkbutton(root, text="Canal 3", variable=c3, command=mostrar_canales).pack(anchor="w")
label_estado = tk.Label(root, text="Canales activos: Ninguno")
label_estado.pack(pady=5)
root.mainloop()
```
Este enfoque es habitual en sistemas embebidos para seleccionar múltiples rutas, líneas digitales, o recursos de hardware, y se puede ampliar a más canales fácilmente.
***

## Ejemplo 3: Selección rápida de perfiles/lotes con OptionMenu

Ideal para elegir entre varios perfiles de calibración, protocolos o identificadores de lote, muy frecuente en manufactura, pruebas y configuración de IoT.

```python
import tkinter as tk

def actualizar_perfil(*args):
    label.config(text=f"Perfil seleccionado: {perfil.get()}")

root = tk.Tk()
root.title("Selección de perfil/lote")

perfil = tk.StringVar(value="Test1")
opciones = ["Test1", "Test2", "Test3", "Personalizado"]
menu = tk.OptionMenu(root, perfil, *opciones)
menu.pack(pady=5)
perfil.trace("w", actualizar_perfil)
label = tk.Label(root, text="Perfil seleccionado: Test1")
label.pack(pady=5)
root.mainloop()
```
Con OptionMenu se facilita la integración de menús desplegables para flujos de testing automatizados y procesos de configuración desde la UI.

***

## Ejemplo 4: Selección compuesta (RadioButton + CheckButton)

Selecciona un modo principal y activa/desactiva funciones extra según el contexto del modo, útil para paneles de diagnóstico.

```python
import tkinter as tk

def actualizar_seleccion():
    modo_txt = modo.get()
    extras = []
    if selftst.get(): extras.append("Self-test")
    if logging.get(): extras.append("Logging")
    res = f"Modo: {modo_txt}"
    if extras: res += "; Extras: " + ", ".join(extras)
    label.config(text=res)

root = tk.Tk()
root.title("Configuración avanzada")

modo = tk.StringVar(value="Operación")
selftst = tk.IntVar()
logging = tk.IntVar()

tk.Radiobutton(root, text="Operación", variable=modo, value="Operación", command=actualizar_seleccion).pack(anchor="w")
tk.Radiobutton(root, text="Servicio", variable=modo, value="Servicio", command=actualizar_seleccion).pack(anchor="w")

tk.Checkbutton(root, text="Self-test avanzado", variable=selftst, command=actualizar_seleccion).pack(anchor="w")
tk.Checkbutton(root, text="Registro de actividad", variable=logging, command=actualizar_seleccion).pack(anchor="w")

label = tk.Label(root, text="Modo: Operación")
label.pack(pady=10)
root.mainloop()
```


***
