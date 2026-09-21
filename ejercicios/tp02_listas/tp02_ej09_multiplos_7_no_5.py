a = int(input("Ingrese el primer valor: "))
b = int(input("Ingrese el segundo valor: "))

lista = [i for i in range(a, b) if i % 7 == 0 and i % 5 != 0]

print(lista)