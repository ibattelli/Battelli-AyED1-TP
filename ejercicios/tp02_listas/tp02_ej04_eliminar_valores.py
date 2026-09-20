lista = [1, 2, 3, 4, 5]
lista2 = [5, 8, 7, 2, 6]

print(f"La lista original es: {lista}")
print(f"\nLa segunda lista es: {lista2}")

for p, v in reversed(list(enumerate(lista))):
    if v in lista2:
        del lista[p]

print(f"\nLa lista sin elementos de la lista 2 queda así: {lista}")
