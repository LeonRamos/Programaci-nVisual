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