def opciones() -> None:
    """ Imprime el menú con opciones para ejecutar"""
    print("\n---Menu---\n")
    print("a. Número Oblongo")
    print("b. Número Triangular\n")

def oblongo(a: int) -> bool:
    """ Verifica si el número ingresado es oblongo.
    Pre: "a" debe ser un entero positivo.
    Post: Devuelve True si "a" es oblongo, de lo contrario devuelve False.
    """
    for i in range(0, a):
        oblongo = i * (i+1)
        if oblongo == a:
            return True
    return False

def triangular(a: int) -> bool:
    """ Verifica si el número ingresado es triangular
    Pre: "a" debe ser un entero positivo.
    Post: Devuelve True si "a" es triangular, de lo contrario devuelve False.
    """
    triangular = 0
    incremento = 0
    
    while triangular < a:
        incremento += 1
        triangular += incremento
        if triangular == a:
            return True
    return False

assert oblongo(6) == True
assert oblongo(7) == False

assert triangular(6) == True
assert triangular(11) == False

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

if __name__ == "__main__":
    main()