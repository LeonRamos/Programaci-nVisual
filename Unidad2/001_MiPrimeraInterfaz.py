
import tkinter as tk

ventana = tk.Tk()
ventana.title("La GUI más sencilla")
etiqueta = tk.Label(ventana, text="¡Hola Mundo!")
etiqueta.pack()
ventana.mainloop()