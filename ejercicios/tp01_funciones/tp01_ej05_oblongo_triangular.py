def opciones() -> None:
    """ Imprime el menú con opciones para ejecutar"""
    print("\n---Menu---\n")
    print("a. Número Oblongo")
    print("b. Número Triangular\n")

oblongo = lambda n: any(i * (i + 1) == n for i in range(1, n))
""" Pre: Recibe como parámetro un número entero positivo
    Post: Devuelve True o False dependiendo de si el numero es oblongo o no
"""

triangular = lambda a: any(sum(range(1, i + 1)) == a for i in range(1, a))
""" Pre: Recibe como parámetro un número entero positivo
    Post: Devuelve True o False dependiendo de si el numero es triangular o no
"""

def main() -> None:
    opciones()
    op = input("Ingrese la opciones que desea ejecutar: ")
    if op == "a":
        n = int(input("Ingrese el numero: "))
        print(oblongo(n))
    elif op == "b":
        n = int(input("Ingrese el numero: "))
        print(triangular(n))
    else:
        print("Opción incorrecta.")

assert oblongo(6) == True
assert oblongo(7) == False

assert triangular(6) == True
assert triangular(11) == False

if __name__ == "__main__":
    main()