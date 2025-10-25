"""
ESP32 + Tkinter: Control de LED con GUI
Autor: Proyecto Educativo LEÓN RAMOS
Requiere: pip install pyserial
"""

import tkinter as tk
from tkinter import ttk
import serial
import serial.tools.list_ports
import threading
import time

class ESP32Controller:
    def __init__(self, root):
        self.root = root
        self.root.title("🎛️ Control ESP32 - LED Controller")
        self.root.geometry("500x400")
        self.root.resizable(False, False)
        
        # Variables
        self.serial_port = None
        self.is_connected = False
        self.led_state = False
        
        # Crear interfaz
        self.create_widgets()
        
        # Hilo para lectura serial
        self.reading_thread = None
        self.stop_reading = False
        
    def create_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # ===== SECCIÓN DE CONEXIÓN =====
        connection_frame = ttk.LabelFrame(main_frame, text="Conexión Serial", padding="10")
        connection_frame.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Label(connection_frame, text="Puerto COM:").grid(row=0, column=0, sticky=tk.W)
        
        # ComboBox para seleccionar puerto
        self.port_combo = ttk.Combobox(connection_frame, width=15, state="readonly")
        self.port_combo.grid(row=0, column=1, padx=5)
        self.refresh_ports()
        
        # Botón refrescar puertos
        ttk.Button(connection_frame, text="🔄 Refrescar", 
                  command=self.refresh_ports).grid(row=0, column=2, padx=5)
        
        # Botón conectar/desconectar
        self.connect_btn = ttk.Button(connection_frame, text="Conectar", 
                                      command=self.toggle_connection)
        self.connect_btn.grid(row=0, column=3, padx=5)
        
        # Label de estado
        self.status_label = ttk.Label(connection_frame, text="● Desconectado", 
                                     foreground="red")
        self.status_label.grid(row=0, column=4, padx=10)
        
        # ===== SECCIÓN DE CONTROL LED =====
        led_frame = ttk.LabelFrame(main_frame, text="Control de LED", padding="20")
        led_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        # Estado visual del LED
        self.led_canvas = tk.Canvas(led_frame, width=100, height=100, bg="white")
        self.led_canvas.grid(row=0, column=0, rowspan=2, padx=20)
        self.led_circle = self.led_canvas.create_oval(10, 10, 90, 90, fill="gray", outline="black")
        
        # Botones de control
        control_frame = ttk.Frame(led_frame)
        control_frame.grid(row=0, column=1, padx=20)
        
        self.on_btn = ttk.Button(control_frame, text="🟢 Encender LED", 
                                 command=self.turn_on_led, width=20, state="disabled")
        self.on_btn.grid(row=0, column=0, pady=5)
        
        self.off_btn = ttk.Button(control_frame, text="🔴 Apagar LED", 
                                  command=self.turn_off_led, width=20, state="disabled")
        self.off_btn.grid(row=1, column=0, pady=5)
        
        self.toggle_btn = ttk.Button(control_frame, text="🔄 Alternar LED", 
                                     command=self.toggle_led, width=20, state="disabled")
        self.toggle_btn.grid(row=2, column=0, pady=5)
        
        # ===== SECCIÓN DE MONITOREO =====
        monitor_frame = ttk.LabelFrame(main_frame, text="Monitor de Datos", padding="10")
        monitor_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=5)
        
        # Temperatura
        ttk.Label(monitor_frame, text="Temperatura:").grid(row=0, column=0, sticky=tk.W)
        self.temp_label = ttk.Label(monitor_frame, text="-- °C", font=("Arial", 12, "bold"))
        self.temp_label.grid(row=0, column=1, padx=10)
        
        # Contador
        ttk.Label(monitor_frame, text="Contador:").grid(row=1, column=0, sticky=tk.W)
        self.count_label = ttk.Label(monitor_frame, text="0", font=("Arial", 12, "bold"))
        self.count_label.grid(row=1, column=1, padx=10)
        
        # ===== CONSOLA DE MENSAJES =====
        console_frame = ttk.LabelFrame(main_frame, text="Consola Serial", padding="5")
        console_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        # Text widget con scrollbar
        self.console_text = tk.Text(console_frame, height=8, width=60, state="disabled")
        scrollbar = ttk.Scrollbar(console_frame, orient="vertical", command=self.console_text.yview)
        self.console_text.configure(yscrollcommand=scrollbar.set)
        
        self.console_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        
        # Botón limpiar consola
        ttk.Button(console_frame, text="Limpiar Consola", 
                  command=self.clear_console).grid(row=1, column=0, pady=5)
    
    def refresh_ports(self):
        """Actualiza la lista de puertos COM disponibles"""
        ports = serial.tools.list_ports.comports()
        port_list = [port.device for port in ports]
        self.port_combo['values'] = port_list
        if port_list:
            self.port_combo.current(0)
        self.log_message(f"Puertos encontrados: {len(port_list)}")
    
    def toggle_connection(self):
        """Conectar o desconectar del puerto serial"""
        if not self.is_connected:
            self.connect()
        else:
            self.disconnect()
    
    def connect(self):
        """Conectar al puerto serial"""
        try:
            port = self.port_combo.get()
            if not port:
                self.log_message("❌ Error: Selecciona un puerto COM")
                return
            
            # Abrir puerto serial
            self.serial_port = serial.Serial(port, 115200, timeout=1)
            time.sleep(2)  # Esperar reset del ESP32
            
            self.is_connected = True
            self.status_label.config(text="● Conectado", foreground="green")
            self.connect_btn.config(text="Desconectar")
            
            # Habilitar botones
            self.on_btn.config(state="normal")
            self.off_btn.config(state="normal")
            self.toggle_btn.config(state="normal")
            
            self.log_message(f"✓ Conectado a {port}")
            
            # Iniciar hilo de lectura
            self.stop_reading = False
            self.reading_thread = threading.Thread(target=self.read_serial, daemon=True)
            self.reading_thread.start()
            
        except Exception as e:
            self.log_message(f"❌ Error de conexión: {str(e)}")
    
    def disconnect(self):
        """Desconectar del puerto serial"""
        self.stop_reading = True
        
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
        
        self.is_connected = False
        self.status_label.config(text="● Desconectado", foreground="red")
        self.connect_btn.config(text="Conectar")
        
        # Deshabilitar botones
        self.on_btn.config(state="disabled")
        self.off_btn.config(state="disabled")
        self.toggle_btn.config(state="disabled")
        
        self.log_message("✓ Desconectado")
    
    def send_command(self, command):
        """Enviar comando al ESP32"""
        if self.is_connected and self.serial_port:
            try:
                self.serial_port.write(command.encode())
                self.log_message(f"→ Enviado: {command}")
            except Exception as e:
                self.log_message(f"❌ Error al enviar: {str(e)}")
    
    def read_serial(self):
        """Leer datos del puerto serial en segundo plano"""
        while not self.stop_reading and self.is_connected:
            try:
                if self.serial_port and self.serial_port.in_waiting > 0:
                    line = self.serial_port.readline().decode('utf-8', errors='ignore').strip()
                    if line:
                        self.process_received_data(line)
            except Exception as e:
                self.log_message(f"❌ Error de lectura: {str(e)}")
                break
            time.sleep(0.1)
    
    def process_received_data(self, data):
        """Procesar datos recibidos del ESP32"""
        self.log_message(f"← {data}")
        
        # Procesar diferentes tipos de mensajes
        if "LED:ON" in data:
            self.update_led_visual(True)
        elif "LED:OFF" in data:
            self.update_led_visual(False)
        elif data.startswith("DATA|"):
            # Formato: DATA|temperatura|contador|estado
            parts = data.split("|")
            if len(parts) >= 4:
                temp = parts[1]
                count = parts[2]
                status = parts[3]
                self.temp_label.config(text=f"{temp} °C")
                self.count_label.config(text=count)
                self.update_led_visual(status == "ON")
        elif data.startswith("TEMP:"):
            temp = data.split(":")[1]
            self.temp_label.config(text=f"{temp} °C")
    
    def update_led_visual(self, is_on):
        """Actualizar representación visual del LED"""
        self.led_state = is_on
        color = "yellow" if is_on else "gray"
        self.led_canvas.itemconfig(self.led_circle, fill=color)
    
    def turn_on_led(self):
        """Encender LED"""
        self.send_command('H')
    
    def turn_off_led(self):
        """Apagar LED"""
        self.send_command('L')
    
    def toggle_led(self):
        """Alternar estado del LED"""
        if self.led_state:
            self.turn_off_led()
        else:
            self.turn_on_led()
    
    def log_message(self, message):
        """Añadir mensaje a la consola"""
        self.console_text.config(state="normal")
        self.console_text.insert(tk.END, f"{message}\n")
        self.console_text.see(tk.END)
        self.console_text.config(state="disabled")
    
    def clear_console(self):
        """Limpiar consola de mensajes"""
        self.console_text.config(state="normal")
        self.console_text.delete(1.0, tk.END)
        self.console_text.config(state="disabled")
    
    def on_closing(self):
        """Manejar cierre de ventana"""
        self.disconnect()
        self.root.destroy()


# ===== PROGRAMA PRINCIPAL =====
if __name__ == "__main__":
    root = tk.Tk()
    app = ESP32Controller(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
