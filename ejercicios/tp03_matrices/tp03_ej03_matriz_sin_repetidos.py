from random import randint

def rellenar_matriz(n: int) -> list[list[int]]:
    """Rellena una matriz de n x n con números enteros al azar entre 0 y n2
    Pre: n debe ser un entero positivo
    Post: retorna una matriz de n x n con números al azar entre 0 y N2
    """
    matriz = []
    ya_usados = []
    for fila in range(n): 
        f = []  
        for columnas in range(n):
            
            agregar = randint(0, n ** 2 - 1)

            while agregar in ya_usados:
                agregar = randint(0, n ** 2 - 1)
            f.append(agregar)
            ya_usados.append(agregar)
        
        matriz.append(f)
    return matriz

def main() -> None:
    n = int(input("Ingrese un número: "))
    matriz = rellenar_matriz(n)
    print(matriz)

if __name__ == "__main__":
    main()
