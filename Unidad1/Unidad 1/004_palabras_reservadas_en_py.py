```python
import keyword

# --- PALABRAS RESERVADAS ---
print("Palabras reservadas en Python:")
print(keyword.kwlist)
print()

# --- LISTAS Y FUNCIONES INTERNAS ---
# Convertir una cadena en lista de caracteres
a = list("letras")
print("Lista creada:", a)  # ['l', 'e', 't', 'r', 'a', 's']
print()

# --- CONDICIONALES ---
lenguaje = "Python"

if lenguaje == "Python":
    print("Estoy de acuerdo, Python es el mejor")
elif lenguaje == "Java":
    print("No me gusta, Java no mola")
else:
    print("Ningún otro lenguaje supera a Python")
print()

# --- BUCLES WHILE Y FOR ---
print("Ejemplo while:")
x = 0
while x < 3:
    print(x)
    x += 1

print("Ejemplo for:")
for i in range(3):
    print(i)

print("Ejemplo for con continue:")
for i in range(3):
    if i == 1:
        continue
    print(i)

print("Ejemplo while con break:")
x = 0
while True:
    print(x)
    if x == 2:
        break
    x += 1
print()

# --- OPERADORES LÓGICOS Y BOOLEANOS ---
x = (5 == 1)
print("¿5 == 1?:", x)  # False

x = True
if x:
    print("Python!")  # Se ejecuta porque x es True
print()

print("True and False:", True and False)  # False
print("True or False:", True or False)    # True
print("not True:", not True)              # False
print()

# --- FUNCIONES ---
def mi_funcion():
    pass

print("Resultado de mi_funcion():", mi_funcion())  # None
print()

# Función que solo imprime el resultado
def funcion_suma_imprime(a, b):
    print("La suma es", a + b)

funcion_suma_imprime(3, 5)  # Salida: La suma es 8
print()

# Función que devuelve el resultado con return
def funcion_suma(a, b):
    return a + b

suma = funcion_suma(3, 5)
print("La suma es", suma)  # Salida: La suma es 8
print()

# Función lambda equivalente
print("La suma es", (lambda a, b: a + b)(3, 5))
print()
```
