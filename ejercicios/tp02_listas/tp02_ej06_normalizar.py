def normalizar_lista(lista: list[int]) -> list[float]:
    """Normaliza una lista de números enteros
    Pre: lista debe contener números enteros y la suma de sus números no debe ser 0
    Post: retorna una lista normalizada
    """
    suma = sum(lista)
    n = map((lambda valor: valor / suma), lista)
    normalizado = list(n)
    return normalizado
def main()-> None:
    lista = [1, 1, 2]
    normalizado = normalizar_lista(lista)
    print(normalizado)

if __name__ == "__main__":
    main()