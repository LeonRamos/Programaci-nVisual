import tkinter as tk
from tkinter import ttk
import time

# --- Configuración de Estilos ---
COLOR_FONDO = "#2C3E50"  # Gris Azulado Oscuro (Elegante y no agresivo)
COLOR_TEXTO = "#ECF0F1"  # Blanco / Gris Claro
COLOR_ALERTA = "#E74C3C" # Rojo (Para estados críticos)
COLOR_NORMAL = "#2ECC71" # Verde (Para estado Normal/Conectado)
COLOR_AFORO = "#F1C40F"  # Amarillo Brillante (Para destacar el número)

# --- Ventana Principal ---
root = tk.Tk()
root.title("SISTEMA CAJA NEGRA DE AFORO (MVP)")
root.geometry("800x450")
root.configure(bg=COLOR_FONDO)
root.mainloop()

# --- FUNCIÓN DE ACTUALIZACIÓN (Simulación de datos desde ESP32) ---
def actualizar_datos_mockup(aforo, entradas, salidas, conectado=True):
    """Simula la recepción de datos y actualiza la GUI."""
    
    # 1. Actualizar el Aforo Principal
    label_aforo_valor.config(text=str(aforo))
    
    # 2. Actualizar Indicadores Históricos
    label_entradas_valor.config(text=str(entradas))
    label_salidas_valor.config(text=str(salidas))
    
    # 3. Actualizar Estado de Conexión
    if conectado:
        estado_texto = "CONECTADO (AD HOC OK)"
        estado_color = COLOR_NORMAL
    else:
        estado_texto = "DESCONECTADO / ESP32 SIN DATOS"
        estado_color = COLOR_ALERTA

    label_estado_valor.config(text=estado_texto, fg=estado_color)
    
    # 4. Actualizar Timestamp
    label_timestamp_valor.config(text=time.strftime("%H:%M:%S"))


# --- DISPOSICIÓN DE LA INTERFAZ ---

# Frame superior para el título y estado
frame_header = tk.Frame(root, bg=COLOR_FONDO)
frame_header.pack(fill='x', pady=10)

label_titulo = tk.Label(frame_header, text="CAJA NEGRA DE AFORO PARA LA VIDA", font=("Arial", 16, "bold"), fg=COLOR_TEXTO, bg=COLOR_FONDO)
label_titulo.pack()

# --- PANEL CENTRAL: EL DATO CRÍTICO (AFORO) ---
frame_central = tk.Frame(root, bg=COLOR_FONDO)
frame_central.pack(pady=20, expand=True)

label_aforo_titulo = tk.Label(frame_central, text="AFORO NETO ACTUAL", font=("Arial", 24), fg=COLOR_TEXTO, bg=COLOR_FONDO)
label_aforo_titulo.pack(pady=(0, 5))

# EL NÚMERO MÁS GRANDE Y VISIBLE
label_aforo_valor = tk.Label(frame_central, text="0", font=("Arial", 120, "bold"), fg=COLOR_AFORO, bg=COLOR_FONDO)
label_aforo_valor.pack()

# --- PANEL INFERIOR: DETALLES Y ESTADO ---
frame_footer = tk.Frame(root, bg=COLOR_FONDO)
frame_footer.pack(fill='x', side='bottom', pady=15)

# 1. Estado de la Conexión
frame_estado = tk.Frame(frame_footer, bg=COLOR_FONDO)
frame_estado.pack(side='left', padx=20)
tk.Label(frame_estado, text="Estado Conexión:", font=("Arial", 12), fg=COLOR_TEXTO, bg=COLOR_FONDO).pack(anchor='w')
label_estado_valor = tk.Label(frame_estado, text="INICIANDO...", font=("Arial", 14, "bold"), fg=COLOR_ALERTA, bg=COLOR_FONDO)
label_estado_valor.pack(anchor='w')

# 2. Hora de Última Actualización
frame_timestamp = tk.Frame(frame_footer, bg=COLOR_FONDO)
frame_timestamp.pack(side='right', padx=20)
tk.Label(frame_timestamp, text="Última Actualización:", font=("Arial", 12), fg=COLOR_TEXTO, bg=COLOR_FONDO).pack(anchor='e')
label_timestamp_valor = tk.Label(frame_timestamp, text="00:00:00", font=("Arial", 14, "bold"), fg=COLOR_TEXTO, bg=COLOR_FONDO)
label_timestamp_valor.pack(anchor='e')

# 3. Indicadores Históricos (Entradas/Salidas)
frame_historico = tk.Frame(frame_footer, bg=COLOR_FONDO)
frame_historico.pack(side='right', padx=40)

# Columna Entradas
tk.Label(frame_historico, text="Entradas:", font=("Arial", 12), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=0, padx=10)
label_entradas_valor = tk.Label(frame_historico, text="0", font=("Arial", 14, "bold"), fg=COLOR_NORMAL, bg=COLOR_FONDO)
label_entradas_valor.grid(row=1, column=0, padx=10)

# Columna Salidas
tk.Label(frame_historico, text="Salidas:", font=("Arial", 12), fg=COLOR_TEXTO, bg=COLOR_FONDO).grid(row=0, column=1, padx=10)
label_salidas_valor = tk.Label(frame_historico, text="0", font=("Arial", 14, "bold"), fg=COLOR_ALERTA, bg=COLOR_FONDO)
label_salidas_valor.grid(row=1, column=1, padx=10)


# --- INICIO DE LA APLICACIÓN (Simulación de datos iniciales) ---
# Simulación: Aforo inicial de 58 personas, 100 entradas y 42 salidas
actualizar_datos_mockup(aforo=58, entradas=100, salidas=42, conectado=True)

# root.mainloop() # Descomentar para ejecutar la GUI real