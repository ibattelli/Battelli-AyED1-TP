def verificar(numero: int)-> bool:
    """ Verifica si el número es positivo
    Pre: recibe un número entero
    Post: Devuelve False si el número es positivo o devuelve True si es negativo o cero
    """
    if numero > 0:
        return False
    return True

def mayor_num(a: int, b: int, c: int) -> int:
    """ Busca el mayor número
    Pre: a, b y c deben ser número enteros
    Post: Devuelve el mayor número de los 3
    """
    if a > b:
        if a > c:
            return a
    if b > a:
        if b > c:
            return b
    if c > a:
        if c > b:
            return c
    return -1       

def main() -> None:
    primer = int(input("Ingrese el primer número: "))
    while verificar(primer):
        primer = int(input("Reingrese el primer número: "))
    segundo = int(input("Ingrese el segundo número: "))
    while verificar(segundo):
        segundo = int(input("Reingrese el segundo número: "))
    tercero = int(input("Ingrese el tercer número: "))
    while verificar(tercero):
        tercero = int(input("Reingrese el tercer número: "))
    
    mayor = mayor_num(primer, segundo, tercero)

    if mayor != -1:
        print(f"El mayor número es: {mayor}")
    else:
        print("El mayor número no existe.")
        

assert verificar(0) == True
assert verificar(-5) == True
assert verificar(2) == False
assert verificar(5) == False

assert mayor_num(2, 5, 6) == 6 
assert mayor_num(8, 5, 7) == 8
assert mayor_num(2, 5, 5) == -1
assert mayor_num(3, 3, 2) == -1

if __name__ == "__main__":
    main()