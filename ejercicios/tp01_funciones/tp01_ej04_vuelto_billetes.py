def cambio(total: int, recibido: int) -> None:
    """ Calcula e informa la cantidad de billetes necesarios para dar como vuelto.
    Pre: El total y recibido deben ser mayores a 0 y deben ser números enteros
    Post: Informa la cantidad de billetes necesarios para dar como vuelto o si no es posible entregar el cambio.
    """
    assert total > 0, "El total deber ser mayor a 0"
    assert recibido > 0, "Recibido debe ser mayor a 0"

    if total > recibido:
        print("Dinero insuficiente")
    else:
        vuelto = recibido - total
        billetes = [5000, 1000, 500, 200, 100, 50, 10]
        for b in billetes:
            cantidad = vuelto // b
            if cantidad > 0:
                print(f"\nBilletes de ${b}: {cantidad}")
                vuelto %= b

        if vuelto > 0:
            print("No se puede entregar el cambio.")
    
def main() -> None:
    total = int(input("Ingrese el total de la compra: "))
    recibido = int(input("Ingrese el dinero recibido: "))
    cambio(total, recibido)

if __name__ == "__main__":
    main()