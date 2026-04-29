import tkinter as tk
from tkinter import ttk
import requests
import threading
import time

ESP32_IP = "192.168.1.50"   # <-- ajusta
UPDATE_INTERVAL = 1000       # ms

class DashboardApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dashboard ESP32 – FC-22 / HC-SR04 / DHT11 / KY-016")
        self.configure(bg="#0f172a")
        self.geometry("900x500")
        self.minsize(720, 400)

        self._create_styles()
        self._create_layout()
        self.after(500, self.update_data_loop)

    def _create_styles(self):
        style = ttk.Style(self)
        style.theme_use("clam")

        style.configure(
            "Card.TFrame",
            background="#111827",
            relief="flat"
        )
        style.configure(
            "Header.TLabel",
            background="#0f172a",
            foreground="#e5e7eb",
            font=("Segoe UI", 14, "bold")
        )
        style.configure(
            "SubHeader.TLabel",
            background="#0f172a",
            foreground="#9ca3af",
            font=("Segoe UI", 9)
        )
        style.configure(
            "Title.TLabel",
            background="#111827",
            foreground="#e5e7eb",
            font=("Segoe UI", 10, "bold")
        )
        style.configure(
            "Sub.TLabel",
            background="#111827",
            foreground="#9ca3af",
            font=("Segoe UI", 8)
        )
        style.configure(
            "Value.TLabel",
            background="#111827",
            foreground="#e5e7eb",
            font=("Segoe UI", 20, "bold")
        )
        style.configure(
            "Unit.TLabel",
            background="#111827",
            foreground="#9ca3af",
            font=("Segoe UI", 9)
        )
        style.configure(
            "Badge.TLabel",
            background="#1f2937",
            foreground="#e5e7eb",
            font=("Segoe UI", 8),
            padding=(6, 2)
        )
        style.configure(
            "Hint.TLabel",
            background="#111827",
            foreground="#9ca3af",
            font=("Segoe UI", 8)
        )

    def _create_layout(self):
        # Header
        header = tk.Frame(self, bg="#0f172a")
        header.pack(side=tk.TOP, fill=tk.X, padx=16, pady=(10, 4))

        ttk.Label(
            header,
            text="Dashboard ESP32",
            style="Header.TLabel"
        ).pack(side=tk.LEFT)

        self.last_update_label = ttk.Label(
            header,
            text="Sin datos",
            style="SubHeader.TLabel"
        )
        self.last_update_label.pack(side=tk.RIGHT)

        sub = ttk.Label(
            header,
            text="FC-22 · HC-SR04 · DHT11 · KY-016",
            style="SubHeader.TLabel"
        )
        sub.pack(side=tk.LEFT, padx=(10, 0))

        # Main grid
        main = tk.Frame(self, bg="#0f172a")
        main.pack(fill=tk.BOTH, expand=True, padx=16, pady=10)

        main.grid_columnconfigure(0, weight=1, uniform="col")
        main.grid_columnconfigure(1, weight=1, uniform="col")
        main.grid_rowconfigure(0, weight=1)
        main.grid_rowconfigure(1, weight=1)

        # Cards
        self._create_card_fc22(main, row=0, col=0)
        self._create_card_dist(main, row=0, col=1)
        self._create_card_ambiente(main, row=1, col=0)
        self._create_card_semaforo(main, row=1, col=1)

        # Footer
        footer = tk.Frame(self, bg="#0f172a")
        footer.pack(side=tk.BOTTOM, fill=tk.X, padx=16, pady=(0, 8))
        ttk.Label(
            footer,
            text="Actualización cada 1 s · Interfaz adaptada para lectura rápida",
            style="SubHeader.TLabel"
        ).pack(side=tk.LEFT)

    # --------- Cards ----------
    def _create_card_fc22(self, parent, row, col):
        frame = ttk.Frame(parent, style="Card.TFrame")
        frame.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
        frame.grid_columnconfigure(0, weight=1)

        header = tk.Frame(frame, bg="#111827")
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="Calidad de aire", style="Title.TLabel").pack(
            side=tk.LEFT
        )
        self.fc22_estado = ttk.Label(header, text="–", style="Badge.TLabel")
        self.fc22_estado.pack(side=tk.RIGHT, padx=4)

        ttk.Label(frame, text="Sensor FC‑22 (nivel relativo)", style="Sub.TLabel").grid(
            row=1, column=0, sticky="w"
        )

        value_row = tk.Frame(frame, bg="#111827")
        value_row.grid(row=2, column=0, sticky="w", pady=(8, 4))
        self.fc22_valor = ttk.Label(value_row, text="--", style="Value.TLabel")
        self.fc22_valor.pack(side=tk.LEFT)
        ttk.Label(value_row, text="%", style="Unit.TLabel").pack(
            side=tk.LEFT, anchor="s", pady=(0, 3), padx=(4, 0)
        )

        # Bar (simulada con canvas)
        bar_bg = tk.Canvas(frame, height=10, bg="#1f2937", highlightthickness=0)
        bar_bg.grid(row=3, column=0, sticky="ew")
        self.fc22_bar_fg = bar_bg.create_rectangle(
            0, 0, 0, 10, fill="#22c55e", width=0
        )
        self.fc22_bar_canvas = bar_bg

        self.fc22_hint = ttk.Label(
            frame, text="Esperando datos...", style="Hint.TLabel", wraplength=260
        )
        self.fc22_hint.grid(row=4, column=0, sticky="w", pady=(4, 0))

    def _create_card_dist(self, parent, row, col):
        frame = ttk.Frame(parent, style="Card.TFrame")
        frame.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
        frame.grid_columnconfigure(0, weight=1)

        header = tk.Frame(frame, bg="#111827")
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="Distancia", style="Title.TLabel").pack(side=tk.LEFT)
        self.dist_estado = ttk.Label(header, text="–", style="Badge.TLabel")
        self.dist_estado.pack(side=tk.RIGHT, padx=4)

        ttk.Label(frame, text="HC‑SR04 (control de proximidad)", style="Sub.TLabel").grid(
            row=1, column=0, sticky="w"
        )

        value_row = tk.Frame(frame, bg="#111827")
        value_row.grid(row=2, column=0, sticky="w", pady=(8, 4))
        self.dist_valor = ttk.Label(value_row, text="--", style="Value.TLabel")
        self.dist_valor.pack(side=tk.LEFT)
        ttk.Label(value_row, text="cm", style="Unit.TLabel").pack(
            side=tk.LEFT, anchor="s", pady=(0, 3), padx=(4, 0)
        )

        bar_bg = tk.Canvas(frame, height=10, bg="#1f2937", highlightthickness=0)
        bar_bg.grid(row=3, column=0, sticky="ew")
        self.dist_bar_fg = bar_bg.create_rectangle(
            0, 0, 0, 10, fill="#22c55e", width=0
        )
        self.dist_bar_canvas = bar_bg

        self.dist_hint = ttk.Label(
            frame,
            text="Usado para el semáforo KY‑016.",
            style="Hint.TLabel",
            wraplength=260,
        )
        self.dist_hint.grid(row=4, column=0, sticky="w", pady=(4, 0))

    def _create_card_ambiente(self, parent, row, col):
        frame = ttk.Frame(parent, style="Card.TFrame")
        frame.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
        frame.grid_columnconfigure(0, weight=1)

        header = tk.Frame(frame, bg="#111827")
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="Ambiente", style="Title.TLabel").pack(side=tk.LEFT)
        self.amb_estado = ttk.Label(header, text="–", style="Badge.TLabel")
        self.amb_estado.pack(side=tk.RIGHT, padx=4)

        ttk.Label(frame, text="Temperatura y humedad (DHT11)", style="Sub.TLabel").grid(
            row=1, column=0, sticky="w"
        )

        temp_row = tk.Frame(frame, bg="#111827")
        temp_row.grid(row=2, column=0, sticky="w", pady=(8, 2))
        self.temp_valor = ttk.Label(temp_row, text="--", style="Value.TLabel")
        self.temp_valor.pack(side=tk.LEFT)
        ttk.Label(temp_row, text="°C", style="Unit.TLabel").pack(
            side=tk.LEFT, anchor="s", pady=(0, 3), padx=(4, 0)
        )

        hum_row = tk.Frame(frame, bg="#111827")
        hum_row.grid(row=3, column=0, sticky="w")
        self.hum_valor = ttk.Label(
            hum_row, text="--", style="Value.TLabel"
        )  # mismo estilo por simplicidad
        self.hum_valor.pack(side=tk.LEFT)
        ttk.Label(hum_row, text="%", style="Unit.TLabel").pack(
            side=tk.LEFT, anchor="s", pady=(0, 3), padx=(4, 0)
        )

        self.amb_hint = ttk.Label(
            frame,
            text="Confort típico: ~20–26 °C y 40–60 %.",
            style="Hint.TLabel",
            wraplength=260,
        )
        self.amb_hint.grid(row=4, column=0, sticky="w", pady=(4, 0))

    def _create_card_semaforo(self, parent, row, col):
        frame = ttk.Frame(parent, style="Card.TFrame")
        frame.grid(row=row, column=col, sticky="nsew", padx=6, pady=6)
        frame.grid_columnconfigure(0, weight=1)

        header = tk.Frame(frame, bg="#111827")
        header.grid(row=0, column=0, sticky="ew")
        ttk.Label(header, text="Semáforo KY‑016", style="Title.TLabel").pack(
            side=tk.LEFT
        )
        self.sem_estado = ttk.Label(header, text="–", style="Badge.TLabel")
        self.sem_estado.pack(side=tk.RIGHT, padx=4)

        ttk.Label(
            frame, text="Estado visual según distancia", style="Sub.TLabel"
        ).grid(row=1, column=0, sticky="w")

        self.sem_color_label = ttk.Label(
            frame, text="–", style="Value.TLabel"
        )
        self.sem_color_label.grid(row=2, column=0, sticky="w", pady=(8, 4))

        bar_bg = tk.Canvas(frame, height=10, bg="#1f2937", highlightthickness=0)
        bar_bg.grid(row=3, column=0, sticky="ew")
        self.sem_bar_fg = bar_bg.create_rectangle(
            0, 0, bar_bg.winfo_reqwidth(), 10, fill="#22c55e", width=0
        )
        self.sem_bar_canvas = bar_bg

        self.sem_hint = ttk.Label(
            frame,
            text="Rojo: cerca · Amarillo: medio · Verde: lejos.",
            style="Hint.TLabel",
            wraplength=260,
        )
        self.sem_hint.grid(row=4, column=0, sticky="w", pady=(4, 0))

    # --------- Lógica de actualización ----------
    def update_data_loop(self):
        # Lanza un hilo para no bloquear la UI
        threading.Thread(target=self._fetch_and_update, daemon=True).start()
        self.after(UPDATE_INTERVAL, self.update_data_loop)

    def _fetch_and_update(self):
        try:
            url = f"http://{ESP32_IP}/data"
            r = requests.get(url, timeout=1.5)
            text = r.text.strip()
            parts = text.split(",")

            if len(parts) < 6:
                return

            gas = self._parse_float(parts[0])
            dist = self._parse_float(parts[1])
            temp = self._parse_float(parts[2])
            hum = self._parse_float(parts[3])
            sem_txt = parts[4].strip()
            sem_col = parts[5].strip() or "#22c55e"

            self.after(
                0,
                lambda: self._update_ui(gas, dist, temp, hum, sem_txt, sem_col),
            )
        except Exception:
            self.after(0, lambda: self.last_update_label.config(text="Sin conexión"))

    @staticmethod
    def _parse_float(s):
        try:
            return float(s)
        except Exception:
            return None

    def _update_ui(self, gas, dist, temp, hum, sem_txt, sem_col):
        # Marca tiempo
        self.last_update_label.config(
            text=time.strftime("Última actualización: %H:%M:%S")
        )

        # FC-22
        if gas is not None:
            g = max(0, min(100, gas))
            self.fc22_valor.config(text=f"{g:.0f}")
            w = self.fc22_bar_canvas.winfo_width()
            self.fc22_bar_canvas.coords(
                self.fc22_bar_fg, 0, 0, w * (g / 100.0), 10
            )

            if g < 30:
                estado, color, hint = "Buena", "#22c55e", "El ambiente se percibe limpio."
            elif g < 70:
                estado, color, hint = (
                    "Media",
                    "#facc15",
                    "Se recomienda ventilar la zona.",
                )
            else:
                estado, color, hint = (
                    "Mala",
                    "#ef4444",
                    "Ventila y revisa posibles fugas o humo.",
                )
            self.fc22_bar_canvas.itemconfig(self.fc22_bar_fg, fill=color)
            self.fc22_estado.config(text=estado)
            self.fc22_hint.config(text=hint)

        # Distancia
        if dist is not None:
            d_show = f"{dist:.1f}"
            self.dist_valor.config(text=d_show)
            d = max(0, min(200, dist))
            w = self.dist_bar_canvas.winfo_width()
            self.dist_bar_canvas.coords(
                self.dist_bar_fg, 0, 0, w * (d / 200.0), 10
            )
            if dist < 20:
                estado, color, hint = (
                    "Muy cerca",
                    "#ef4444",
                    "Precaución: distancia mínima.",
                )
            elif dist < 80:
                estado, color, hint = (
                    "Media",
                    "#facc15",
                    "Objeto a distancia intermedia.",
                )
            else:
                estado, color, hint = ("Lejos", "#22c55e", "Objeto alejado.")
            self.dist_bar_canvas.itemconfig(self.dist_bar_fg, fill=color)
            self.dist_estado.config(text=estado)
            self.dist_hint.config(text=hint)

        # Ambiente
        if temp is not None:
            self.temp_valor.config(text=f"{temp:.1f}")
        if hum is not None:
            self.hum_valor.config(text=f"{hum:.0f}")

        amb_estado = "Normal"
        amb_hint = "Dentro de un rango de confort aproximado."
        if temp is not None and (temp < 18 or temp > 28):
            amb_estado = "Fuera de confort térmico"
            amb_hint = "Considera ajustar climatización o ventilación."
        self.amb_estado.config(text=amb_estado)
        self.amb_hint.config(text=amb_hint)

        # Semáforo KY‑016
        if sem_txt:
            self.sem_estado.config(text=sem_txt)
            self.sem_color_label.config(text=sem_txt)
        w = self.sem_bar_canvas.winfo_width()
        self.sem_bar_canvas.coords(self.sem_bar_fg, 0, 0, w, 10)
        self.sem_bar_canvas.itemconfig(self.sem_bar_fg, fill=sem_col or "#22c55e")


if __name__ == "__main__":
    app = DashboardApp()
    app.mainloop()
