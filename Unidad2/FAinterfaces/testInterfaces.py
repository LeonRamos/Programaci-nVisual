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