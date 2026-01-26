import tkinter as tk
from tkinter import messagebox

# Funciones que se ejecutan al pulsar los botones
def encender():
    valor = entry_valor.get()
    print(f"Acción: encender, Valor: {valor}")
    label_estado.config(text=f"Estado: ENCENDIDO (valor = {valor})")

def apagar():
    valor = entry_valor.get()
    print(f"Acción: apagar, Valor: {valor}")
    label_estado.config(text=f"Estado: APAGADO (valor = {valor})")

# Crear ventana principal
root = tk.Tk()
root.title("Control ESP32 simulado")

# Etiqueta y campo de entrada (equivalente a <input type="number" name="valor">)
label_valor = tk.Label(root, text="Valor:")
label_valor.grid(row=0, column=0, padx=10, pady=10)

entry_valor = tk.Entry(root)
entry_valor.grid(row=0, column=1, padx=10, pady=10)

# Dos botones (equivalentes a los dos <button type="submit"...>)
btn_encender = tk.Button(root, text="Encender", command=encender)
btn_encender.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

btn_apagar = tk.Button(root, text="Apagar", command=apagar)
btn_apagar.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

# Etiqueta de estado, para mostrar qué se hizo
label_estado = tk.Label(root, text="Estado: ---")
label_estado.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Bucle principal
root.mainloop()
