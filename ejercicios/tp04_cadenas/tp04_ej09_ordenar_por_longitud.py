"""Escribir una función que reciba como parámetro una cadena de caracteres en la que
las palabras se encuentran separadas por uno o más espacios. Devolver otra
cadena con las palabras ordenadas según su longitud, dejando un espacio entre
cada una. Los signos de puntuación no deben ser tenidos en cuenta al medir la
longitud de las palabras, pero deberán conservarse en la cadena final."""
import string

def elimar_puntuacion(cadena):
    eliminar = str.maketrans('', '', string.punctuation)
    cadena_nueva = cadena.translate(eliminar)

    return cadena_nueva

def cadena_ordenadas_longitud(cadena, cadena_nueva):
    ordenada = cadena_nueva.split(" ")
    ordanos = cadena.split(" ")
    #ordanos = ordanos.sort(lambda a: for o in ordenada if )
    print(ordenada)
    print(ordanos)
    pass
cadena = "Hola, como estas."
cadena_nueva = elimar_puntuacion(cadena)
print(cadena_nueva)

cadena_ordenadas_longitud(cadena, cadena_nueva)