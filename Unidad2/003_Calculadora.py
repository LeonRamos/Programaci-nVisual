# Importar la librería Tkinter para la interfaz gráfica
import tkinter as tk

# Definir la función que realiza la operación según la selección del usuario
def calcular(operacion):
    try:
        num1 = float(entry_num1.get())  # Tomar el primer número del campo de texto
        num2 = float(entry_num2.get())  # Tomar el segundo número del campo de texto

        # Verificar la operación seleccionada y calcular el resultado
        if operacion == "sumar":
            resultado = num1 + num2
        elif operacion == "restar":
            resultado = num1 - num2
        elif operacion == "multiplicar":
            resultado = num1 * num2
        elif operacion == "dividir":
            # Prevenir división entre cero
            if num2 == 0:
                resultado = "Error: División por cero"
            else:
                resultado = num1 / num2

        # Mostrar el resultado en la etiqueta
        label_resultado.config(text=f"Resultado: {resultado}")
    except ValueError:
        # Mensaje de error si algún dato no es numérico
        label_resultado.config(text="Error: Ingresa solo números")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Calculadora Básica")

# Etiqueta y caja de texto para el primer número
tk.Label(ventana, text="Primer número:").grid(row=0, column=0, padx=5, pady=5)
entry_num1 = tk.Entry(ventana)
entry_num1.grid(row=0, column=1, padx=5, pady=5)

# Etiqueta y caja de texto para el segundo número
tk.Label(ventana, text="Segundo número:").grid(row=1, column=0, padx=5, pady=5)
entry_num2 = tk.Entry(ventana)
entry_num2.grid(row=1, column=1, padx=5, pady=5)

# Botones para cada operación
btn_sumar = tk.Button(ventana, text="Sumar", command=lambda: calcular("sumar"))
btn_sumar.grid(row=2, column=0, padx=10, pady=10)

btn_restar = tk.Button(ventana, text="Restar", command=lambda: calcular("restar"))
btn_restar.grid(row=2, column=1, padx=10, pady=10)

btn_multiplicar = tk.Button(ventana, text="Multiplicar", command=lambda: calcular("multiplicar"))
btn_multiplicar.grid(row=3, column=0, padx=10, pady=10)

btn_dividir = tk.Button(ventana, text="Dividir", command=lambda: calcular("dividir"))
btn_dividir.grid(row=3, column=1, padx=10, pady=10)

# Etiqueta para el resultado
label_resultado = tk.Label(ventana, text="Resultado: ")
label_resultado.grid(row=4, column=0, columnspan=2, padx=5, pady=20)

# Ejecutar el bucle principal para mostrar la ventana
ventana.mainloop()
