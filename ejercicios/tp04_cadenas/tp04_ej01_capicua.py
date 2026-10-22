def cadena_capicua(cadena: str) -> bool:
    """Verifica si una cadena es capicúa o no
    Pre: cadena debe ser un string.
    Post: Retorna False si no es capicúa, si es, retorna True
    """
    for i in range(len(cadena) // 2):
        if cadena[i] != cadena[-(i + 1)]:
            return False
    return True
        
def main() -> None:
    cadena = input("Ingrese la cadena de caracteres: ")
    capicua = cadena_capicua(cadena)
    if capicua:
        print(f"La cadena: -{cadena}- es capicúa.")
    else:
        print(f"La cadena: -{cadena}- no es capicúa.")

if __name__ == "__main__":
    main()