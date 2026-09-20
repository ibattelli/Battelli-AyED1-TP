"""Intercalar los elementos de una lista entre los elementos de otra. La intercalación
deberá realizarse exclusivamente mediante la técnica de rebanadas y no se creará
una lista nueva sino que se modificará la primera. Por ejemplo, si lista1 = [8, 1, 3]
y lista2 = [5, 9, 7], lista1 deberá quedar como [8, 5, 1, 9, 3, 7]. Las listas pueden
tener distintas longitudes"""

def intercalar_lista(lista: list[int], lista2: list[int]) -> list[int]:
    for p, _ in enumerate(lista[ : : 2]):
        valor = lista2.pop()
        lista.insert(p, valor)
    return lista

lista = [8, 1, 3]
lista2 = [5, 9, 7]

lista = intercalar_lista(lista, lista2)
print(lista)
