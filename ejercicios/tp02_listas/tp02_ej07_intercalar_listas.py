def intercalar_lista(lista: list[int], lista2: list[int]) -> list[int]:
    """Intercala los elementos de lista2 entre los elementos de lista
    Pre: lista y lista2 deben contener números enteros
    Post: retorna lista modificada con sus elementos intercalados con los de lista2
    """
    cantidad = len(lista)
    for i in range(min(len(lista), len(lista2))):
        lista[i * 2 +1 : i * 2 +1] = lista2[i : i + 1]
    lista[len(lista) : len(lista)] = lista2[cantidad : ]

    return lista
    
def main()-> None:
    lista = [8, 1, 3]
    lista2 = [5, 9, 7]
    lista = intercalar_lista(lista, lista2)
    print(lista)

if __name__ == "__main__":
    main()