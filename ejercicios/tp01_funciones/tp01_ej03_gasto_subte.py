def gastos_mes(viajes: int) -> float:
    """ Calcula los gastos de viaejes en el mes
    Pre: Viajes debe ser un número entero positivo.
    Post: Devuelve el gasto total a pagar en Float
    """
    tarifa = 1000
    cant_viajes = (41, 31, 21)
    descuentos = (0.4, 0.3, 0.2)
    total = 0

    if viajes <= 20:
        return float(viajes * tarifa)
    else:
        for cantidad, descuento in zip(cant_viajes, descuentos):
            if viajes >= cantidad:
                sobrante = viajes - (cantidad -1)
                total += sobrante * (tarifa - (tarifa * descuento))
                viajes -= sobrante

    total += viajes * tarifa
    return float(total)


def main() -> None:
    viajes = int(input("Ingrese la cantidad de viajes hechos en un mes: "))
    while viajes <= 0:
        print("Ingrese una cantidad de viajes mayor a 0")
        viajes = int(input("Ingrese la cantidad de viajes hechos en un mes: "))
    total = gastos_mes(viajes)
    print(f"El total de gastos en viajes fue de: ${total}")


if __name__ == "__main__":
    main()