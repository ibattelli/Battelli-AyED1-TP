def bisiesto(anio: int) -> bool:
    """ Verifica si el año ingresado es bisiesto o no
    Pre: anio debe ser un numero entero positivo
    Post: si anio es bisiesto devuelte True, sino lo es, devuelve False
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def verificar_fecha(d: int, m: int, a:int ) -> bool:
    """ Verifica si la fecha ingresa es correcta
    Pre: d, m y a deben ser número enteros positivos
    Post: devuelve True si la fecha es válida o False si la fecha no es válida
    """
    if d < 1 or d > 31:
        return False
    
    if m < 1 or m > 12:
        return False
    
    if a < 1:
        return False

    # verificación fecha correcta
    if m in (1, 3, 5, 7, 8, 10, 12):
        return True
    elif m in (4, 6, 9, 11):
        if d <= 30:
            return True
        else:
            return False
    
    elif m == 2:
        if bisiesto(a):
            if d <= 29:
                return True
            else:
                return False
        else:
            if d <= 28:
                return True
            else:
                return False
         

def main() -> None:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    
    if verificar_fecha(dia, mes, anio):
        print(f"La fecha {dia}/{mes}/{anio} es válida.")
    else:
        print(f"La fecha {dia}/{mes}/{anio} es inválida.")


assert verificar_fecha(5, 5, 2020) == True
assert verificar_fecha(31, 12, 2021) == True
assert verificar_fecha(30, 6, 2026) == True
assert verificar_fecha(31, 6, 2020) == False
assert verificar_fecha(29, 2, 2024) == True
assert verificar_fecha(29, 2, 2023) == False

if __name__ == "__main__":
    main()
