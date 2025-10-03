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