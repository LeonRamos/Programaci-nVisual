La librería estándar de Python para GUI, **Tkinter**, incluye soporte nativo para barras de progreso a través del widget `ttk.Progressbar`. 
### Usar barra de progreso con ttk.Progressbar

- **Modo determinado**: Se utiliza cuando conoces el progreso total de una tarea. El valor se establece manualmente según el avance.
- **Modo indeterminado**: Indica que una operación está en curso sin saber su duración exacta; la barra se anima constantemente.

#### Ejemplo básico en modo determinado

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Barra de Progreso")

progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=20)

def iniciar():
    progress['value'] = 0
    root.update_idletasks()
    for i in range(0, 101, 10):
        progress['value'] = i
        root.update_idletasks()
        root.after(200)

ttk.Button(root, text='Iniciar', command=iniciar).pack(pady=10)
root.mainloop()
```


#### Ejemplo en modo indeterminado

```python
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
progress = ttk.Progressbar(root, mode='indeterminate')
progress.pack(pady=20)
progress.start(50) # Intervalo en milisegundos
root.mainloop()
```


### Métodos y opciones útiles

- **start([interval])**: Comienza la animación automáticamente.[3]
- **stop()**: Detiene la animación de la barra de progreso.[3]
- **step([amount])**: Incrementa el valor de la barra por una cantidad específica.[3]
- Se puede ligar a una variable (`variable=mi_var`) para controlar el valor mediante funciones u otras operaciones.[1]

### Recursos adicionales
La documentación oficial de Python y varios tutoriales en español (como Recursospython, Stack Overflow y videos en YouTube) ofrecen ejemplos prácticos, personalización de estilos y casos de uso típicos para el aula o scripts educativos.[4][5][1][3]

