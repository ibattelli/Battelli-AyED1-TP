from random import randint
cantidad = 10
lista = [randint(1, 100) for i in range(cantidad)]

lista_impares = list(filter(lambda n: n % 2 != 0, lista))

print(f"La lista original es: {lista}")

print(f"La lista con números impares: {lista_impares}")