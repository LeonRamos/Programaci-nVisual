
import tkinter as tk

# Función que agrega el texto de los botones a la pantalla
def click(boton):
    actual = entrada.get()
    entrada.delete(0, tk.END)
    entrada.insert(0, actual + str(boton))

# Función para limpiar la pantalla
def limpiar():
    entrada.delete(0, tk.END)

# Función para evaluar la operación
def calcular():
    try:
        expresion = entrada.get()
        resultado = eval(expresion)  # cuidado, eval evalúa expresiones directamente
        entrada.delete(0, tk.END)
        entrada.insert(0, str(resultado))
    except:
        entrada.delete(0, tk.END)
        entrada.insert(0, "Error")

#ventana principal
ventana = tk.Tk()
ventana.title("Calculadora")

# Pantalla de calculadora 
entrada = tk.Entry(ventana, width=20, font=("Arial", 18), bd=5, relief="sunken", justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

# Botones de la calculadora
botones = [
    ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
]

for (texto, fila, col) in botones:
    if texto == "=":
        b = tk.Button(ventana, text=texto, width=5, height=2, command=calcular)
    else:
        b = tk.Button(ventana, text=texto, width=5, height=2, command=lambda t=texto: click(t))
    b.grid(row=fila, column=col, padx=5, pady=5)

# Botón para limpiar pantalla
btn_clear = tk.Button(ventana, text="C", width=5, height=2, command=limpiar)
btn_clear.grid(row=5, column=0, columnspan=4, sticky="we", padx=5, pady=5)

# Ejecutar el bucle principal
ventana.mainloop()
