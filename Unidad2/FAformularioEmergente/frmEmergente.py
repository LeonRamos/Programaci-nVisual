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