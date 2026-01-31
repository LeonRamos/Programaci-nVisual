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
    while True:
        print("\n--- CALCULADORA ---")
        print("1) Sumar")
        print("2) Restar")
        print("3) Multiplicar")
        print("4) Dividir")
        print("5) Salir")

        opcion = input("Elige una opción: ")

        if opcion == "5":
            print("Saliendo...")
            break

        a = int(input("Primer número: "))
        b = int(input("Segundo número: "))
        calc = Calculadora(a, b)

        if opcion == "1":
            print("Resultado:", calc.sumar())
        elif opcion == "2":
            print("Resultado:", calc.restar())
        elif opcion == "3":
            print("Resultado:", calc.multiplicar())
        elif opcion == "4":
            print("Resultado:", calc.dividir())
        else:
            print("Opción no válida")
