"""Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros."""

def ultimos_caracteres(cadena: str, numero: int) -> str:
    print(cadena[-numero : ])

cadena = "maquinándome"
numero = 7
ultimos_caracteres(cadena, numero)