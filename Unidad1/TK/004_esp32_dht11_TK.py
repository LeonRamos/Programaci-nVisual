import serial, tkinter as tk, re

ser = serial.Serial('COM3', 115200)  # Ajusta puerto

root = tk.Tk()
root.title("DHT11 - ESP32")

lbl_temp = tk.Label(root, text="Temp: -- °C", font=("Arial", 24), fg="green")
lbl_temp.pack(pady=10)

lbl_hum = tk.Label(root, text="Hum: -- %", font=("Arial", 24), fg="blue")
lbl_hum.pack(pady=10)

def leer_datos():
    linea = ser.readline().decode(errors="ignore").strip()
    m = re.findall(r"[-+]?\d+\.?\d*", linea)
    if len(m) >= 2:
        temp = float(m[1])
        hum  = float(m[0])
        lbl_temp.config(text=f"Temp: {temp:.1f} °C")
        lbl_hum.config(text=f"Hum: {hum:.1f} %")
        # Ejemplo sencillo de color según temperatura
        if temp >= 30:
            lbl_temp.config(fg="red")
        elif temp >= 20:
            lbl_temp.config(fg="orange")
        else:
            lbl_temp.config(fg="green")
    root.after(1000, leer_datos)

leer_datos()
root.mainloop()
