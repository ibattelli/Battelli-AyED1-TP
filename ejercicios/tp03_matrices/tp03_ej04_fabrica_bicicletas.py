from random import randint

def crear_matriz(n: int) -> list[list[int]]:
    """Crear una matriz con datos generados al azar para N fábricas
    Pre: n debe ser un número entero positivo
    Post: retorna una matriz de n filas y 6 columnas con valores enteros entre 0 y 150
    """
    matriz = [] 
    for fabricas in range(n):
        fabrica = []
        for dia in range(6):
            fabrica.append(randint(0, 150))
        matriz.append(fabrica)
    return matriz

def cant_bicicletas_fabricadas(matriz: list[list[int]]) -> None:
    """Muestra la cantidad de bicicletas fabricadas por cada fábrica
    Pre: matriz debe ser una lista de listas con números enteros 
    Post: imprime la cantidad de bicicletas fabricadas por cada fábrica
    """
    for i, fabrica in enumerate(matriz):
        total = sum(fabrica)
        print(f"La fábrica {i} fabricó: {total} bicicletas.")

def mayor_produccion_dia(matriz: list[list[int]]) -> None:
    """Muestra cuál es la fábrica que más produjo en un solo día
    Pre: matriz debe ser una lista de listas con números enteros
    Post: imprime cuál fue la fábrica que más produjo en un solo día
    """
    mayor = 0
    m_fabrica = 0
    dia = 0
    for i, fabrica in enumerate(matriz):
        maxima_prod = max(fabrica)
        dia = fabrica.index(maxima_prod)
        if mayor < maxima_prod:
            mayor = maxima_prod
            m_fabrica = i
            mayor_dia = dia
    print(f"La fábrica que mas produjo en un solo día fue: {m_fabrica} con {mayor} bicicletas el dia {mayor_dia}")

def dia_mas_productivo(matriz: list[list[int]]) -> None:
    """ Muestra cual fue el día mas productivo considerando todas las fábricas combinadas
    Pre: matriz debe ser una lista de listas con números enteros
    Post: imprime cuál día fue el mas productivo y con cuantas bicicletas
    
    """
    mas_productivo = 0
    dia_productivo = 0
    for dia in range(6):
        suma_dia = 0
        for fabrica in matriz:
            suma_dia += fabrica[dia]
        if suma_dia > mas_productivo:
            mas_productivo = suma_dia
            dia_productivo = dia
    print(f"El día más productivo fue el día {dia_productivo}, con {mas_productivo} bicicletas")

def menor_cant_fabricada(matriz: list[list[int]]) -> list[int]:
    """Crea una lista por compresión que contiene la menor cantidad fabricada por cada fábrica
    Pre: matriz debe ser una lista de listas con números enteros
    Post: retorna una lista con la menor cantidad fabricada de cada fábrica
    """
    menor_cant = [min(i) for i in matriz]
    return menor_cant

def main() -> None:
    n = 3
    matriz = crear_matriz(n)
    print(matriz)
    cant_bicicletas_fabricadas(matriz)
    mayor_produccion_dia(matriz)
    dia_mas_productivo(matriz)
    menores = menor_cant_fabricada(matriz)
    print(menores)

if __name__ == "__main__":
    main()




