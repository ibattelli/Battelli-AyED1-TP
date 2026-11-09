def filtrar_palabras(cadena: str, numero: int) -> str:
    """Recibe una cadena y un numero y retorna las palabras con "numero" o más caracteres
    Pre: cadena debe ser un string y numero debe ser un número entero
    Post: retorna un string con las palabras que tengan "numero" o más caracteres
    """
    palabras = cadena.split(" ")
    filtrado = []
    for palabra in palabras:
        if len(palabra) >= numero:
            filtrado.append(palabra)
    cadena_nueva = "-".join(filtrado)
    return cadena_nueva

def lista_comprension(cadena: str, numero: int) -> str:
    """Recibe una cadena y un numero y retorna mediante una lista por comprensión las palabras con "numero" o más caracteres
    Pre: cadena debe ser un string y numero debe ser un número entero
    Post: retorna un string con las palabras que tengan "numero" o más caracteres
    """
    filtrado = [palabra for palabra in cadena.split(" ") if len(palabra) >= numero]
    return "-".join(filtrado)


def lista_filter(cadena: str, numero: int) -> str:
    """Recibe una cadena y un numero y retorna mediante filter las palabras con "numero" o más caracteres
    Pre: cadena debe ser un string y numero debe ser un número entero
    Post: retorna un string con las palabras que tengan "numero" o más caracteres
    """
    filtrado = list(filter(lambda palabra: len(palabra) >= numero, cadena.split(" ")))
    return "-".join(filtrado)


def main() -> None:
    cadena = "hola soy estudiante de programación"
    numero = 4

    print(filtrar_palabras(cadena, numero))
    print(lista_comprension(cadena, numero))
    print(filtrar_palabras(cadena, numero))

if __name__ == "__main__":
    main()
