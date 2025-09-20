import tkinter as tk

root = tk.Tk()
root.title("Monitor de Sensor Embebido")
# Simula la lectura de un sensor
valor_sensor = 36.8

etiqueta = tk.Label(root, text=f"Valor del sensor: {valor_sensor} °C", font=("Arial", 14))
etiqueta.pack(pady=10)

root.mainloop()