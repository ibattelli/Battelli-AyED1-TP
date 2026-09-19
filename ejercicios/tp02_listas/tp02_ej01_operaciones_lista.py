from random import randint
from functools import reduce

def opciones() -> None:
    """Imprime la opciones para ejecutar"""
    print("\n--Menu--")
    print("1. Generar una lista con números al azar de cuatro dígitos.")
    print("2. Calcular y devolver el producto de todos los elementos de la lista.")
    print("3. Eliminar todas las apariciones de un valor en la lista.")
    print("4. Determinar si el contenido de una lista cualquiera es capicúa.")
    print("0. Salir.\n")

def crear_lista():
    """Crea una lista con número random
    Pre: nada
    Post: Retorna una lista que contiene números random
    """
    cantidad = randint(10, 99)
    return [randint(1000, 9999) for c in range(cantidad)]

def lista_productos(lista: list[int]) -> int:
    """Calcula el producto de todos los elemento de una lista
    Pre: lista debe contener números enteros
    Post: Retorna el producto de todos los elementos de la lista
    """
    if not lista:
        print("\nPrimero ejecute la primera opcion para generar una lista\n")
        return False
    
    producto = reduce((lambda acumulador, elemento: acumulador * elemento), lista)

    return producto

def eliminar_valores(lista: list[int], valor: int) -> list[int]:
    """Elimina el valor ingresado de una lista
    Pre: lista debe contener números enteros y valor debe ser un número entero
    Post: Retorna la lista modifica sin el valor ingresado
    """
    if not lista:
        print("\nPrimero ejecute la primera opcion para generar una lista\n")
        return lista
    if valor in lista:
        while valor in lista:
            lista.remove(valor)
        return lista
    else:
        print("Ese valor no se encontraba en la lista")
        return lista
    
        

def capicua(lista: list) -> bool:
    """Informa si la lista es capicúa o no
    Pre: lista debe contener números enteros
    Post: Si lista no es capicúa retorna False, si lo es, retorna True
    """
    if not lista:
        print("\nPrimero ejecute la primera opcion para generar una lista\n")
        return False
    for i in range(len(lista) // 2):
        if lista[i] != lista[-(i+1)]:
            return False
    return True

def main() -> None:
    lista = []
  
    while True:
        opciones()
        op = input("Ingrese la opción que desea ejecutar: ")
        if op == "1":
            lista = crear_lista()
            print(lista)
        elif op == "2":
            producto = lista_productos(lista)
            print(f"El producto de la lista es: {producto}")
        elif op == "3":
            valor = int(input("Ingresar un valor: "))
            lista = eliminar_valores(lista, valor)
        elif op == "4":
            if capicua(lista):
                print("La lista es capicua")
            else:
                print("La lista no es capicua")
        elif op == "0":
            print("Adios!")
            break
        else:
            print("Opción incorrecta")

if __name__ == "__main__":
    main()