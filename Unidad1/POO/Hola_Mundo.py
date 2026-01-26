class HolaMundo:
    def __init__(self, mensaje):
        self.mensaje = mensaje  # atributo de instancia

    def saludar(self):
        print(self.mensaje)     # método de instancia


if __name__ == "__main__":
    saludo = HolaMundo("Hola mundo desde POO")
    saludo.saludar()
