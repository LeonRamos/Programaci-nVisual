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