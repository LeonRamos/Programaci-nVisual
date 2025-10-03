import tkinter as tk
from tkinter import ttk, messagebox

def ventana_entry():
    def enviar():
        valor = entry.get()
        if valor.isdigit():
            label_estado.config(text=f"Valor almacenado: {valor}")
        else:
            label_estado.config(text="Solo números permitidos")
    v = tk.Toplevel()
    v.title("Práctica: Entry con Validación")
    entry = tk.Entry(v)
    entry.grid(row=0, column=0, padx=5, pady=5)
    boton = tk.Button(v, text="Enviar", command=enviar)
    boton.grid(row=0, column=1, padx=5, pady=5)
    label_estado = tk.Label(v, text="Esperando datos...")
    label_estado.grid(row=1, column=0, columnspan=2)

def ventana_spinbox():
    def seleccionar_canal():
        canal = spin.get()
        label.set(f"Canal digital seleccionado: {canal}")
    v = tk.Toplevel()
    v.title("Práctica: Spinbox (Canal Digital)")
    spin = tk.Spinbox(v, from_=1, to=8)
    spin.pack(pady=5)
    tk.Button(v, text="Seleccionar", command=seleccionar_canal).pack()
    label = tk.StringVar()
    tk.Label(v, textvariable=label).pack(pady=5)

def ventana_combobox():
    def elegir_sensor(event=None):
        seleccion = combo.get()
        etiqueta.set(f"Tipo de sensor: {seleccion}")
    v = tk.Toplevel()
    v.title("Práctica: Combobox")
    lista = ["Temperatura", "Luminosidad", "Humedad", "Movimiento"]
    combo = ttk.Combobox(v, values=lista, state="readonly")
    combo.pack(pady=5)
    combo.bind("<<ComboboxSelected>>", elegir_sensor)
    etiqueta = tk.StringVar()
    ttk.Label(v, textvariable=etiqueta).pack(pady=5)

def ventana_mensajes():
    def guardar():
        messagebox.showinfo("Configuración", "La configuración se guardó correctamente.")
    v = tk.Toplevel()
    v.title("Práctica: Mensajes informativos")
    tk.Button(v, text="Guardar", command=guardar).pack(pady=20)

def ventana_validacion_avanzada():
    def solo_numeros(P):
        return P.isdigit()
    v = tk.Toplevel()
    v.title("Práctica: Validación en tiempo real")
    vcmd = (v.register(solo_numeros), "%P")
    entry = tk.Entry(v, validate="key", validatecommand=vcmd)
    entry.pack(padx=10, pady=10)

root = tk.Tk()
root.title("Menú de Prácticas TK - Electrónica Embebida")

tk.Label(root, text="Seleccione la práctica para abrir:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="1. Entry con validación", width=30, command=ventana_entry).pack(pady=4)
tk.Button(root, text="2. Selección de canal (Spinbox)", width=30, command=ventana_spinbox).pack(pady=4)
tk.Button(root, text="3. Selección de tipo de sensor (Combobox)", width=30, command=ventana_combobox).pack(pady=4)
tk.Button(root, text="4. Mensajes informativos", width=30, command=ventana_mensajes).pack(pady=4)
tk.Button(root, text="5. Validación avanzada en tiempo real", width=30, command=ventana_validacion_avanzada).pack(pady=4)

root.mainloop()
