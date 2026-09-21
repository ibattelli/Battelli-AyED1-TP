def cargar_matriz(n: int) -> list[list[int]]:
    """Carga una matriz n x n con números enteros que se ingresan por teclado
    Pre: n debe ser un entero mayor positivo
    Post: retorna una matriz con n x n con números enteros
    """
    matriz = []
    for filas in range(n):
        fila = []
        for j in range(n):
            numero = int(input("Ingresa un número: "))
            fila.append(numero)
        matriz.append(fila)
    return matriz

def ordenar_filas(matriz: list[list[int]]) -> list[list[int]]:
    """Ordena de forma ascente cada una de las filas de la matriz
    Pre: matriz debe ser una matriz de números enteros
    Post: retorna la matriz con cada una de sus filas ordenada de forma ascendente
    """
    for fila in matriz:  
        fila.sort()
    return matriz

def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> list[list[int]]:           #c
    """Intercambia dos filas de la matriz
    Pre: matriz debe ser una matriz cuadrada, fila1 y fila2 deben ser índices válidos de filas, siendo diferentes entre si
    Post: retorna la matriz con las filas fila1 y fila2 intercambiadas
    """
    matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]
    return matriz

def verificar_posicion(matriz: list[list[int]], posicion: int) -> int:
    """Verifica que una posición ingresada sea válida
    Pre: matriz debe ser una matriz cuadrada
    Post: devuelve una posicion válida entre 1 y la cantidad de filas de la matriz
    """
    while posicion < 1 or posicion > len(matriz):
        posicion = int(input(f"Ingrese la primera posición correctamente(1 a {len(matriz)}): "))
    return posicion
def verificar_segunda_posicion(matriz: list[list[int]], posicion: int, posicion2: int) -> int:
    """Verifica que una segunda posición sea válida y diferente de la primera
    Pre: matriz debe ser una matriz cuadrada y posición debe ser válida
    Post: retorna una posición válida entre 1 y la cantidad de filas de la matriz, diferente de posición
    """
    while posicion2 < 1 or posicion2 > len(matriz) or posicion2 == posicion:
        posicion2 = int(input(f"Ingrese la segunda posición correctamente(1 a {len(matriz)}): "))  
    return posicion2

def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> list[list[int]]:  #d
    """Intercambia dos columnas de la matriz
    Pre: matriz debe ser una matriz cuadrada, col1 y col2 deben ser índice válidos
    Post: retorna la matriz con las columnas col1 y col2 intercambiadas   
    """
    for fila in matriz:
        fila[col1], fila[col2] = fila[col2], fila[col1]
    return matriz

def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:                    #e
    """Transpone la matriz sobre sí misma
    Pre: matriz debe ser una matriz cuadrada
    Post: retorna la matriz transpuesta, intercambiando cada elemento Aij por Aji
    """
    for i in range(len(matriz)):  
        for j in range(i + 1, len(matriz)):
            matriz[i][j], matriz[j][i] = matriz[j][i], matriz[i][j]
    return matriz

def promedio_fila(matriz: list[list[int]], n_fila: int) -> float:           #f
    """Calcula el promedio de los elementos de una fila
    Pre: matriz debe ser una matriz cuadrada y n_fila debe ser un índice válido de fila
    Post: retorna el promedio de los elementos de la fila n_fila
    """
    suma = sum(matriz[n_fila])
    promedio = suma / len(matriz[n_fila])
    return promedio

def porcentaje_impar(matriz: list[list[int]], columna: int) -> float:               #g
    """Calcula el porcentaje de elementos impares de una columna
    Pre: matriz debe ser una matriz cuadrada y columna debe ser un índice válido de columna
    Post: retorna el procentaje del elementis impares de la columna indicada
    """
    impar = 0
    for fila in range(len(matriz)):
        if matriz[fila][columna] % 2 != 0:
            impar += 1
    porcentaje = impar / len(matriz) * 100
    return porcentaje

def matriz_simetrica(matriz: list[list[int]]) -> bool:                           #h
    """Determina si la matriz es simétrica respecto de su diagonal principal
    Pre: matriz debe ser una matriz cuadrada
    Post: retorn True si la matriz es simétrica respecto a su diagonal principal y False en caso contrario
    """
    for i in range(len(matriz)):  
        for j in range(len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def matriz_simetrica_secundaria(matriz: list[list[int]]) -> bool:  
    """Determina si la matriz es simétrica respecto de su diagonal secundaria
        Pre: matriz debe ser una matriz cuadrada
        Post: retorn True si la matriz es simétrica respecto a su diagonal secundaria y False en caso contrario
    """                
    for i in range(len(matriz)):  
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[len(matriz) - 1 - i][len(matriz) - 1 - j]:
                return False
    return True

def palindromos(matriz: list[list[int]]) -> list:
    """Determina qué columnas de la matriz son palíndromos
    Pre: matriz debe ser una matriz cuadrada
    Post: retorna una lista con los índices de las columnas que son palíndromos
    """
    columnas_palindromas = []
    for i in range(len(matriz)):
        lista = []
        for j in range(len(matriz)):
            lista.append(matriz[j][i])
        palindromo = True
        for c in range(len(lista) // 2):
            if lista[c] != lista[-(c+1)]:
                palindromo = False
        if palindromo:
            columnas_palindromas.append(i)
    return columnas_palindromas
                
def main() -> None:
    n = int(input("Ingrese el largo y ancho que tendrá la matriz: "))

    matriz = cargar_matriz(n)
    print(matriz)

    matriz = ordenar_filas(matriz)
    print(matriz)


    #intercambiar filas
    f1 = int(input(f"Ingrese la primera fila(1 a {len(matriz)}): "))
    f1 = verificar_posicion(matriz, f1)
    
    f2 = int(input(f"Ingrese la segunda fila(1 a {len(matriz)}): "))
    f2 = verificar_segunda_posicion(matriz, f1, f2)

    matriz = intercambiar_filas(matriz, f1 - 1, f2 - 1)
    print(matriz)


    col1 = int(input(f"Ingrese la primera columna(1 a {len(matriz)}): "))
    col1 = verificar_posicion(matriz, col1)

    #intercambiar columnas
    col2 = int(input(f"Ingrese la segunda columna(1 a {len(matriz)}): "))
    col2 = verificar_segunda_posicion(matriz, col1, col2)

    matriz = intercambiar_columnas(matriz, col1 - 1, col2 - 1)
    print(matriz)


    #transponer matriz
    matriz = transponer_matriz(matriz)
    print(matriz)


    #promedio de fila
    fila = int(input("Ingrese el número de fila: "))
    fila = verificar_posicion(matriz, fila)
    promedio = promedio_fila(matriz, fila - 1)
    print(f"El promedio es: {promedio}")


    #porcentaje de columna
    columna = int(input("Ingrese el número de columna: "))
    columna = verificar_posicion(matriz, columna)
    porcentaje = porcentaje_impar(matriz, columna - 1)
    print(f"El porcentaje es: {porcentaje}")


    #matriz simétrica
    if matriz_simetrica(matriz):
        print("La matriz es simétrica respecto a su diagonal principal.")
    else:
        print("La matriz no es simétrica")

    #matriz simétrica secundaria
    if matriz_simetrica_secundaria(matriz):
        print("La matriz es simétrica respecto a su diagonal secundaria.")
    else:
        print("La matriz no es simétrica")

    columnas_palindromos = palindromos(matriz)
    print(f"Las columnas palindromas son: {palindromos}")

if __name__ == "__main__":
    main()