def verificar_datos(m: int, a:int ) -> bool:
    """ Verifica si la fecha ingresada es correcta.
    Pre: m y a deben ser números enteros positivos.
    Post: Devuelve True si los datos son válidos o False si llos datos no son válidos.
    """
    if m < 1 or m > 12:
        return False
    
    if a < 1:
        return False

    return True

def crear_calendario(dia: int, mes: int, anio: int) -> None:
    """Imprime el calendario con la fecha ingresada.
    Pre: dia, mes y anio deben ser números enteros positivos.
    Post: Imprime el calendario del mes ingresado.
    """
    meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    dias = ("Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab")
    treintayuno = (1, 3, 5, 7, 8, 10, 12)
    treinta = (4, 6, 9, 11)
    cantidad_dias = 0
    dia_inicial = diadelasemana(dia, mes, anio)
    
    if mes in treintayuno:
        cantidad_dias = 31
    elif mes in treinta:
        cantidad_dias = 30
    elif bisiesto(anio):
        cantidad_dias = 29
    else:
        cantidad_dias = 28
    print(f"\nCalendario de {meses[mes - 1]} del año {anio}\n")
    
    for dia in dias:
        print(f"{dia}", end=" ")

    print()

    for d in range(dia_inicial):
        print("    ", end="")

    for dia in range(1, cantidad_dias + 1):
        print(f"{dia:4}", end= "")
        if (dia_inicial + dia) % 7 == 0:
            print()


def bisiesto(anio: int) -> bool:
    """ Verifica si el año ingresado es bisiesto o no
    Pre: anio debe ser un numero entero positivo
    Post: si anio es bisiesto devuelte True, sino lo es, devuelve False
    """
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def diadelasemana(dia: int, mes: int, anio: int) -> int:
    """Permite averiguar el día de la semana para una fecha determinada
    Pre: dia, mes, anio deben ser números enteros postivos.
    Post: Devuelve 0 para domingo, 1 para lunes, 2 para martes.. etc.
    """
    if mes < 3:
        mes = mes + 10
        anio = anio - 1
    else:
        mes = mes - 2
    siglo = anio // 100
    anio2 = anio % 100
    diasem = (((26*mes-2)//10)+dia+anio2+(anio2//4)+(siglo//4)-(2*siglo))%7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def main() -> None:
    mes = int(input("Ingrese el número de mes: "))
    anio = int(input("Ingrese el año: "))
    if verificar_datos(mes, anio):
        crear_calendario(1, mes, anio)
    else:
        print("Fecha incorrecta")

if __name__ == "__main__":
    main()