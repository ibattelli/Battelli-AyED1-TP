def opciones() -> None:
    """Muestra las opciones para ejecutar."""
    print("\nMenú")
    print("a. Sumar determinada cantidad de dias.")
    print("b. Calcular la cantidad de días existentes entre dos fechas.")
    print("c. Salir.")

def bisiesto(anio: int) -> bool:
    """ Verifica si el año ingresado es bisiesto o no
    Pre: anio debe ser un numero entero positivo
    Post: si anio es bisiesto devuelte True, sino lo es, devuelve False
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def diasiguiente(d: int, m: int, a: int) -> tuple:
    """ Devuelve la fecha del día siguiente de la fecha ingresada
    Pre: "d, m y a" deben ser enteros positivos
    Post: Devuelve una tupla con "d, m y a" actualizados al día siguiente
    """
    
    if m in (1, 3, 5, 7, 8, 10, 12):
        if d < 31:
            d += 1
        else:
            if m < 12:
                m += 1
                d = 1
            else:
                m = 1
                d = 1
                a += 1
    elif m in (4, 6, 9, 11):
        if d < 30:
            d += 1
        else:
            m += 1
            d = 1
    elif m == 2:
        if bisiesto(a):
            if d < 29:
                d += 1
            else:
                m += 1
                d = 1
        else:
            if d < 28:
                d+= 1
            else:
                m += 1
                d = 1
    return d, m, a

def verificar_fecha(d: int, m: int, a: int) -> bool:
    """ Verifica si la fecha ingresada es válida
    Pre: "d, m y a" deben ser número enteros positivos
    Post: Si la fecha es correcta devuelve True, de lo contrario devuelve False
    """

    if a < 1900:     #tomo como fecha mínima el año 1900
        return False
    if m < 1 or m > 12:
            return False
    if m in (1, 3, 5, 7, 8, 10, 12):
        if d < 1 or d > 31:
            return False
    if m in (4, 6, 9, 11):
        if d < 1 or d > 30:
            return False
    if m == 2:
        if bisiesto(a):
            if d < 1 or d > 29:
                return  False
        else:
            if d < 1 or d > 28:
                return False
    return True

def opcion_a() -> None:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    if verificar_fecha(dia, mes, anio):
        sumar_dias = int(input("\nIngrese la cantidad de días a sumar: "))
        while sumar_dias < 1:
            sumar_dias = int(input("\nIngrese una cantidad correcta de días a sumar: "))
        dia_actualizado = dia
        mes_actualizado = mes
        anio_actualizado = anio
        for _ in range(sumar_dias):
            dia_actualizado, mes_actualizado, anio_actualizado = diasiguiente(dia_actualizado, mes_actualizado, anio_actualizado)
                            
        print(f"La fecha actualizada es: {dia_actualizado}/{mes_actualizado}/{anio_actualizado}")
    else:
        print("\nFecha incorrecta.")

def opcion_b() -> None:
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año: "))
    if verificar_fecha(dia, mes, anio):    
        dia_final = int(input("\nIngrese el día de la segunda fecha: "))
        mes_final = int(input("Ingrese el mes de la segunda fecha: "))
        anio_final = int(input("Ingrese el año de la segunda fecha: "))
        if verificar_fecha(dia_final, mes_final, anio_final):
            contador = 0
            if (anio, mes, dia) < (anio_final, mes_final, dia_final):
                while (dia, mes, anio) != (dia_final, mes_final, anio_final):
                    dia, mes, anio = diasiguiente(dia, mes, anio)
                    contador += 1
                print(f"\nLa cantidad de dias entre las fechas es de: {contador}")
            else:
                while (dia_final, mes_final, anio_final) != (dia, mes, anio):
                    dia_final, mes_final, anio_final = diasiguiente(dia_final, mes_final, anio_final)
                    contador += 1
                print(f"\nLa cantidad de dias entre las fechas es de: {contador}")
        else:
            print("La segunda fecha es incorrecta.")
    else:
        print("La primera fecha es incorrecta.")

def main() -> None:
    op = ""
    while op != "c":
        opciones()
        op = input("\nIngrese la opción que desea ejecutar: ")
        if op == "a":
            opcion_a()
                
        elif op == "b":
            opcion_b()
            
        elif op == "c":
            print("Adios!")
                
        else:
            print("Opción incorrecta.")

assert diasiguiente(15, 5, 2025) == (16, 5, 2025)
assert diasiguiente(29, 2, 2024) == (1, 3, 2024)
assert diasiguiente(31, 12, 2026) == (1, 1, 2027)

if __name__ == "__main__":
    main()