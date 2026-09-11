from random import randint

def opciones() -> None:
    """Imprime la opciones para ejecutar"""
    print("\n--Menu--")
    print("1. Mostrar cantidad de cajones completos.")
    print("2. Mostrar cantidad de naranjas para jugo.")
    print("3. Mostrar naranjas sobrantes para otro envío")
    print("4. Mostrar cantidad de camiones llenos")
    print("0. Salir.")


def naranjas_vender_jugo(naranjas: int) -> tuple:
    """ Crea una lista de naranjas y otra de naranjas para jugo
    Pre: naranjas debe ser un número entero mayor o igual a 0
    Post: Retorna una tupla con dos listas
    """
    lista_naranjas = [randint(150, 350) for _ in range(naranjas)]
    naranjas_jugos = []

    for p, naranja in reversed(list(enumerate(lista_naranjas))):
        if naranja > 300 or naranja < 200:
            n_jugo = lista_naranjas.pop(p)
            naranjas_jugos.append(n_jugo)

    return lista_naranjas, naranjas_jugos

def cant_cajones(lista_naranjas: list) -> tuple:
    """Calcula la cantidad de cajones que se pueden llenar y su sobrante
    Pre: lista_naranjas debe ser una lista.
    Post: Retorna una tupla con la cantidad de cajones y el sobrante
    """
    assert isinstance(lista_naranjas, list), "Deber recibir una lista"

    cant_naranjas = len(lista_naranjas)
    cant_cajones = cant_naranjas // 100
    sobrante = cant_naranjas % 100
    return cant_cajones, sobrante

def dividir_reparto(lista_naranjas: list) -> int:
    """Calcula la cantidad de camiones necesarios para repartir las naranjas
    Pre: lista_naranjas debe ser una lista.
    Post: Retorna un número entero que es la cantidad de camiones necesarios.
    """
    assert isinstance(lista_naranjas, list), "Deber recibir una lista"

    total_reparto = sum(lista_naranjas)
    total_kilos = total_reparto / 1000
    cant_camiones = total_kilos // 500
    sobrante = total_kilos % 500

    if sobrante >= 500 * 0.8:
        cant_camiones += 1

    return int(cant_camiones)
    

def main() -> None:
    cant_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    while cant_naranjas < 0:
        cant_naranjas = int(input("Ingrese una cantidad correcta de naranjas cosechadas: "))

    lista_n, lista_j = naranjas_vender_jugo(cant_naranjas)
    cajones, sobrante = cant_cajones(lista_n)
    op = " "
    while op != "0":
        opciones()
        op = input("\nIngrese la opción que desea ejecutar: ")
        if op == "1":
            print(f"\nLa cantidad de cajones que se pueden llenar son: {cajones} cajones")
        elif op == "2":
            print(f"\nLa cantidad de naranjas para jugo son: {len(lista_j)} naranjas")
        elif op == "3":
            print(f"\nLa cantidad de naranjas sobrantes para otro envio son: {sobrante} naranjas")
        elif op == "4":
            cant_camiones = dividir_reparto(lista_n)
            print(f"\nPara transportar la consecha se necesitan: {cant_camiones} camiones")
        elif op == "0":
            print("\nAdios!")
        else:
            print("\nOpción incorrecta")

if __name__ == "__main__":
    main()