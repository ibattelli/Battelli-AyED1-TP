def lista_ordenada(lista: list) -> bool:
    """Verifica si la lista ingresada está ordenada
    Pre: lista debe contener elementos elementos comparables entre si
    Post: Retorna True si la lista está ordenada, sino, retorna False
    """
    lista2 = lista.copy()
    lista2.sort()
    return lista == lista2
lista = ["a", "b", "c"]

print(lista_ordenada(lista))