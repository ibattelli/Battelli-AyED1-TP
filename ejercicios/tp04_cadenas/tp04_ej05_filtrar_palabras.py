"""Escribir una función filtrar_palabras() que reciba una cadena de caracteres conte-
niendo una frase y un entero N, y devuelva otra cadena con las palabras que ten-
gan N o más caracteres de la cadena original. Escribir también un programa para
verificar el comportamiento de la misma. Hacer tres versiones de la función, para
cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter"""


def filtrar_palabras(cadena: str, numero: int) -> str:
    palabras = cadena.split(" ")
    filtrado = []
    for palabra in palabras:
        if len(palabra) >= numero:
            filtrado.append(palabra)
    cadena_nueva = "-".join(filtrado)
    return cadena_nueva

def main() -> None:
    cadena = "hola soy estudiante de programación"
    numero = 3

    cadena_nueva = filtrar_palabras(cadena, numero)
    print(cadena_nueva)

if __name__ == "__main__":
    main()
