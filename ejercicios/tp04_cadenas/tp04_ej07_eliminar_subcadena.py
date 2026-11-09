def eliminar_subcadena(cadena: str, p: int, c: int) -> str:
    """Elimina una subcadena de una cadena de caracteres, según su posicion y la cantidad de caracteres utilizando rebanadas
    Pre: cadena debe ser un string, posicion debe ser un número entero positivo y cantidad debe ser un número entero positivo
    Post: retorna la cadena sin la subcadena de la posición y cantidad de caracteres deseados
    """
    return cadena[ : p] + cadena[p + c : ]

def eliminar_subcadena_sin_slices(cadena: str, p: int, c: int) -> str:
    """Elimina una subcadena de una cadena de caracteres, según su posicion y la cantidad de caracteres
    Pre: cadena debe ser un string, posicion debe ser un número entero positivo y cantidad debe ser un número entero positivo
    Post: retorna la cadena sin la subcadena de la posición y cantidad de caracteres deseados
    """
    nueva_cadena = ""
    for cad in range(len(cadena)):
        if cad < p or cad >= p + c:
            nueva_cadena += cadena[cad]
    return nueva_cadena
    
def main() -> None:
    cadena = "El número de teléfono es 4356-7890"
    p = 25
    c = 9

    print(eliminar_subcadena(cadena, p, c))
    print(eliminar_subcadena_sin_slices(cadena, p, c))


