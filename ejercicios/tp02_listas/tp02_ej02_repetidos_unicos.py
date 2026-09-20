from random import randint 

def generar_lista(n: int) -> list[int]:
    """Genera una lista con n cantidad de números random
    Pre: n debe ser un número entero positivo
    Post: retorna una lista con n cantidad de números random entre 1 y 100
    """
    return [randint(1, 100) for c in range(n)]

def elemento_repetido(lista: list[int]) -> bool:
    """Verifica si hay elementos repetidos en la lista
    Pre: lista debe contener números enteros positivos
    Post: Si la lista contiene números repetidos, retorna True, sino, retorna False
    """
    repetido = 0
    for e in lista:
        repetido = lista.count(e)
        if repetido > 1:
            return True
    return False

def lista_elementos_unicos(lista: list[int]) -> list[int]:
    """Crea una lista con números sin repetir
    Pre: lista debe contener números enteros positivos
    Post: Retorna una lista con números únicos(sin repetir)
    """
    lista_unica = []
    repetido = 0
    for e in (lista):
        if e not in lista_unica:
            lista_unica.append(e)
    return lista_unica


def main() -> None:
    n = int(input("Ingrese la cantidad de elementos: "))
    lista = generar_lista(n)
    print(f"\n Lista generada: {lista}")

    if elemento_repetido(lista):
        print("\nLa lista tiene elementos repetidos.")
    else:
        print("\nLa lista no tiene elementos repetidos")

    lista_unicos = lista_elementos_unicos(lista)
    print(f"\nLista con números únicos(sin duplicar): {lista_unicos}")

if __name__ == "__main__":
    main()