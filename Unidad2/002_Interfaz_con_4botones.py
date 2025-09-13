# Importar la librería Tkinter y los cuadros de mensaje
import tkinter as tk
from tkinter import messagebox

# Función que se llama cuando un botón es presionado
def manejar_boton(numero_dispositivo):
    # Muestra un cuadro pidiendo confirmación al usuario
    respuesta = messagebox.askyesno("Confirmar acción",
                                    f"¿Deseas activar el dispositivo {numero_dispositivo}?")
    if respuesta:
        # Si el usuario confirma, muestra otro cuadro notificando la acción
        messagebox.showinfo("Acción realizada",
                            f"Dispositivo {numero_dispositivo} activado correctamente.")
    else:
        # Si el usuario cancela, muestra una notificación de cancelación (opcional)
        messagebox.showinfo("Acción cancelada",
                            f"No se activó el dispositivo {numero_dispositivo}.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Control Electrónico (Simulación)")
ventana.geometry("350x250")

# Crear cuatro botones para dispositivos
boton1 = tk.Button(ventana, text="Activar Dispositivo 1",
                   command=lambda: manejar_boton(1))
boton1.pack(pady=10)

boton2 = tk.Button(ventana, text="Activar Dispositivo 2",
                   command=lambda: manejar_boton(2))
boton2.pack(pady=10)

boton3 = tk.Button(ventana, text="Activar Dispositivo 3",
                   command=lambda: manejar_boton(3))
boton3.pack(pady=10)

boton4 = tk.Button(ventana, text="Activar Dispositivo 4",
                   command=lambda: manejar_boton(4))
boton4.pack(pady=10)

# Ejecutar la ventana principal
ventana.mainloop()
