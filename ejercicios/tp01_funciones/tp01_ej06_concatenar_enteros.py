def concatenar_enteros(num1: int, num2: int) -> int:
    """ Concatena el primer y segundo número ingresado.
    Pre: Num1 y Num2 deben ser enteros positivos.
    Post: Devuelve un número entero resultante de la concatenación de ambos número ingresados.
    """
    digitos = 1
    segundo_num = num2

    while segundo_num > 0:
        segundo_num //= 10
        digitos *= 10

    concatenado = (num1 * digitos) + num2
    return concatenado

def main() -> None:

    a = int(input("Ingresar el primer numero: "))
    b = int(input("Ingresar el segundo numero: "))

    concatenado = concatenar_enteros(a, b)
    print(f"El número concatenado quedó así: {concatenado}")

if __name__ == "__main__":
    main()