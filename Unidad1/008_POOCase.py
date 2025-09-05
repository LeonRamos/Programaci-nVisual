# Ejemplo de Programación Orientada a Objetos en Python:
# Gestión de cuentas bancarias

# 1. Definimos la clase principal 'CuentaBancaria'.
class CuentaBancaria:
    # 2. El método __init__ se ejecuta al crear una nueva cuenta. Aquí se inicializan los atributos.
    def __init__(self, titular, saldo=0):
        self.titular = titular  # 3. Guardamos el nombre de la persona propietaria de la cuenta
        self.saldo = saldo      # 4. Guardamos el saldo actual de la cuenta
    
    # 5. Método para depositar dinero
    def depositar(self, cantidad):
        self.saldo += cantidad  # 6. Sumamos la cantidad al saldo
        print(f"{self.titular} depositó ${cantidad}. Saldo actual: ${self.saldo}")
    
    # 7. Método para retirar dinero, con validación (encapsulamiento)
    def retirar(self, cantidad):
        if cantidad > self.saldo:  # 8. Verificamos que haya suficiente saldo
            print("Fondos insuficientes.")
        else:
            self.saldo -= cantidad
            print(f"{self.titular} retiró ${cantidad}. Saldo actual: ${self.saldo}")
    
    # 9. Método para consultar el saldo
    def consultar_saldo(self):
        print(f"Saldo actual de {self.titular}: ${self.saldo}")

# 10. Herencia: Definimos una clase hija para cuentas especiales
class CuentaPremium(CuentaBancaria):
    # 11. Nueva característica: la cuenta premium puede tener un sobregiro autorizado
    def __init__(self, titular, saldo=0, sobregiro=500):
        super().__init__(titular, saldo)   # 12. Llamamos al constructor de la clase padre
        self.sobregiro = sobregiro         # 13. Límites de sobregiro permitidos
    
    # 14. Reescribimos el método retirar para considerar el sobregiro
    def retirar(self, cantidad):
        if cantidad > self.saldo + self.sobregiro:
            print("Fondos insuficientes, incluso con sobregiro.")
        else:
            self.saldo -= cantidad
            print(f"{self.titular} retiró ${cantidad}. Saldo: ${self.saldo}, Sobregiro disponible: ${self.sobregiro+(self.saldo if self.saldo<0 else 0)}")

# 15. Uso del sistema: crear objetos representa cuentas reales
cuenta1 = CuentaBancaria("Ana Ruiz", saldo=1000)
cuenta1.depositar(200)
cuenta1.retirar(1500)
cuenta1.consultar_saldo()

cuenta2 = CuentaPremium("Carlos Gómez", saldo=500)
cuenta2.retirar(800)
cuenta2.consultar_saldo()

#Explicación paso a paso
#Clase: Es un molde para crear objetos del mismo tipo. Aquí, CuentaBancaria describe cómo debe ser y funcionar una cuenta bancaria.

#Objeto: Es una instancia de una clase. Por ejemplo, cuenta1 y cuenta2 son objetos creados a partir de las clases.

#Atributos: Son datos asociados al objeto, como el titular o el saldo.

#Métodos: Son acciones que puede hacer el objeto, como depositar, retirar, o consultar saldo.

#Encapsulamiento: Protege los datos internos, asegurando que sólo los métodos pueden cambiar el saldo de forma controlada.

#Herencia: CuentaPremium hereda de CuentaBancaria, añadiendo la funcionalidad de sobregiro.

#Polimorfismo: El método retirar se comporta diferente en la clase hija.