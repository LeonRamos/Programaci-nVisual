
## Ejemplo base 1: Tkinter (estilo secuencial)

```python
import tkinter as tk
from tkinter import ttk

# Ventana principal
ventana = tk.Tk()
ventana.title("Formulario básico")

# ------- Etiquetas y cuadros de texto -------
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entrada_nombre = tk.Entry(ventana)
entrada_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Correo:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entrada_correo = tk.Entry(ventana)
entrada_correo.grid(row=1, column=1, padx=5, pady=5)

# ------- Lista desplegable (Combobox) -------
tk.Label(ventana, text="País:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
combo_pais = ttk.Combobox(ventana, values=["México", "España", "Argentina"])
combo_pais.grid(row=2, column=1, padx=5, pady=5)
combo_pais.current(0)

# ------- Checkbutton y Radiobutton -------
suscrito = tk.BooleanVar()
tk.Checkbutton(ventana, text="Suscribirse al boletín", variable=suscrito).grid(
    row=3, column=0, columnspan=2, padx=5, pady=5
)

tipo_cuenta = tk.StringVar(value="basica")
tk.Radiobutton(ventana, text="Básica", value="basica", variable=tipo_cuenta).grid(
    row=4, column=0, padx=5, pady=5
)
tk.Radiobutton(ventana, text="Premium", value="premium", variable=tipo_cuenta).grid(
    row=4, column=1, padx=5, pady=5
)

# ------- Botones -------
def guardar():
    print("Guardando datos...")

def cancelar():
    ventana.destroy()

tk.Button(ventana, text="Guardar", command=guardar).grid(
    row=5, column=0, padx=5, pady=10
)
tk.Button(ventana, text="Cancelar", command=cancelar).grid(
    row=5, column=1, padx=5, pady=10
)

# ------- Barra de estado (simple) -------
barra_estado = tk.Label(ventana, text="Listo", anchor="w", relief="sunken")
barra_estado.grid(row=6, column=0, columnspan=2, sticky="we")

ventana.mainloop()
```

Agreguen: menú, pestañas (`ttk.Notebook`), `Scrollbar`, `Progressbar`, etc. sobre esta base. [guia-tkinter.readthedocs](http://guia-tkinter.readthedocs.org/es/develop/chapters/6-widgets/6.1-Intro.html)

***

## Ejemplo base 2: HTML sencillo

```html
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <title>Formulario básico</title>
  <style>
    body { font-family: Arial, sans-serif; }
    .contenedor { width: 400px; margin: 20px auto; border: 1px solid #ccc; padding: 15px; }
    .fila { margin-bottom: 10px; }
    label { display: inline-block; width: 100px; }
    .barra-estado { margin-top: 10px; font-size: 0.9em; color: #555; border-top: 1px solid #ccc; padding-top: 5px; }
  </style>
</head>
<body>
  <div class="contenedor">
    <h2>Registro básico</h2>

    <div class="fila">
      <label for="nombre">Nombre:</label>
      <input type="text" id="nombre" name="nombre">
    </div>

    <div class="fila">
      <label for="correo">Correo:</label>
      <input type="email" id="correo" name="correo">
    </div>

    <div class="fila">
      <label for="pais">País:</label>
      <select id="pais" name="pais">
        <option value="mx">México</option>
        <option value="es">España</option>
        <option value="ar">Argentina</option>
      </select>
    </div>

    <div class="fila">
      <span>Tipo de cuenta:</span>
      <input type="radio" id="basica" name="tipo" value="basica" checked>
      <label for="basica">Básica</label>
      <input type="radio" id="premium" name="tipo" value="premium">
      <label for="premium">Premium</label>
    </div>

    <div class="fila">
      <input type="checkbox" id="boletin" name="boletin">
      <label for="boletin">Suscribirse al boletín</label>
    </div>

    <div class="fila">
      <button type="submit">Enviar</button>
      <button type="reset">Cancelar</button>
    </div>

    <div class="barra-estado">
      Estado: listo
    </div>
  </div>
</body>
</html>
```

Extenderlo con más campos, menús de navegación, barras de desplazamiento (contenedor con más contenido), pestañas con CSS/JS, etc. [youtube](https://www.youtube.com/watch?v=_Wawz9Lh7m8)

