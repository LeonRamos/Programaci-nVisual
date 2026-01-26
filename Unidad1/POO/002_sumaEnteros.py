class SumaEnteros:
    def __init__(self, a, b):
        self.a = a          # primer entero
        self.b = b          # segundo entero

    def sumar(self):
        return self.a + self.b


if __name__ == "__main__":
    numero1 = int(input("Introduce el primer entero: "))
    numero2 = int(input("Introduce el segundo entero: "))

    operacion = SumaEnteros(numero1, numero2)
    resultado = operacion.sumar()

    print(f"La suma de {numero1} y {numero2} es {resultado}")
