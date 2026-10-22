romanos = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I")
)

def convertir_a_romanos(numero: int) -> str:
    """Convierne un número entero en número romano
    Pre: Numero debe ser un número entero menor o igual a 3999
    Post: Retorna un string con el número convertido a romano
    """
    n_romano = []
    for valor, romano in romanos:
        cantidad = numero // valor
        if cantidad:
            n_romano.append(romano * cantidad)
        numero = numero % valor
    numero_romano = "".join(n_romano)
    return numero_romano

def main() -> None:
    numero = int(input("Ingresar número para convertir(menor or igual a 3999): "))
    while numero > 3999:
        numero = int(input("Ingresar número para convertir(menor or igual a 3999): "))

    numero_romano = convertir_a_romanos(numero)

    print(f"El numero a convertir en es: {numero}")
    print(f"El número convertido es: {numero_romano}")

if __name__ == "__main__":
    main()