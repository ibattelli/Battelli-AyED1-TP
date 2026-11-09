def extraer_subcadena(cadena: str, posicion: int, cantidad: int) -> str:
    """Extrae una subcadena de una cadena de caracteres, según su posicion y la cantidad de caracteres utilizando rebanadas
    Pre: cadena debe ser un string, posicion debe ser un número entero positivo y cantidad debe ser un número entero positivo
    Post: retorna la subcadena de la posición y cantidad de caracteres deseados
    """
    return cadena[posicion:(posicion + cantidad)]

def extrear_subcadena_sin_rebanadas(cadena: str, posicion: int, cantidad: int) -> str:
    """Extrae una subcadena de una cadena de caracteres, según su posicion y la cantidad de caracteres
    Pre: cadena debe ser un string, posicion debe ser un número entero positivo y cantidad debe ser un número entero positivo
    Post: retorna la subcadena de la posición y cantidad de caracteres deseados
    """
    s = ""
    for subcadena in range(posicion, (posicion + cantidad)):
        s += cadena[subcadena]
    return s

def main() -> None:
    cadena = "El número de teléfono es 4356-7890 hola"
    p = 25
    c = 9

    print(extraer_subcadena(cadena, p, c))
    print((extrear_subcadena_sin_rebanadas(cadena, p, c)))

if __name__=="__main__":
    main()