class Calculadora:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def sumar(self):
        return self.a + self.b

    def restar(self):
        return self.a - self.b

    def multiplicar(self):
        return self.a * self.b

    def dividir(self):
        if self.b == 0:
            return "Error: división entre cero"
        return self.a / self.b


if __name__ == "__main__":
    numero1 = int(input("Introduce el primer entero: "))
    numero2 = int(input("Introduce el segundo entero: "))

    calc = Calculadora(numero1, numero2)

    print(f"Suma: {calc.sumar()}")
    print(f"Resta: {calc.restar()}")
    print(f"Multiplicación: {calc.multiplicar()}")
    print(f"División: {calc.dividir()}")
