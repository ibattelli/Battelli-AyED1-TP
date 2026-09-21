def patron_a(n : int) -> list[list[int]]:
    matriz = []
    for f in range(n):
        fila = []
        if f == 0:
            fila.append(1)
        else:
            fila.append(0)
        for columna in range(n - 1):
            fila.append(0)
        matriz.append(fila)
    a = 1
    for i in range(1, len(matriz)):       
        a += 2
        matriz[i][i] = a
            
    return matriz
def patron_b(n: int) -> list[list[int]]:
    matriz = []
    a = 1
    for f in range(n - 1, -1, -1):
        fila = []
        if f == 0:
            fila.append(1)
        else:
            fila.append(0)
        for columna in range(n - 1):
            fila.append(0)
        matriz.append(fila)
        
    for i in range(len(matriz) -1, -1, -1):       
        matriz[i][n - 1 -i] = a
        a *= 3
                
    return matriz


def patron_c(n : int) -> list[list[int]]:
    matriz = []
    for f in range(n):
        fila = []
        if f == 0:
            fila.append(1)
        else:
            fila.append(0)
        for columna in range(n - 1):
            fila.append(0)
        matriz.append(fila)
    a = n + 1
    for i in range(len(matriz)):       
        a -= 1
        for j in range(i + 1):
            matriz[i][j] = a
        

    return matriz

def patron_d(n : int) -> list[list[int]]:
    matriz = []
    for f in range(n):
        fila = []
        if f == 0:
            fila.append(1)
        else:
            fila.append(0)
        for columna in range(n - 1):
            fila.append(0)
        matriz.append(fila)
    a = 2 ** n
    for i in range(len(matriz)):
        a = a // 2 
        for j in range(len(matriz)):      
            matriz[i][j] = a
            
    return matriz

def patron_e(n : int) -> list[list[int]]:
    matriz = []
    for f in range(n):
        fila = []
        for columna in range(n):
            fila.append(0)
        matriz.append(fila)
    a = 0
    for i in range(n):
        if i % 2 != 0:
            for j in range(0, n, 2):
                a += 1
                matriz[i][j] = a
        else:
            for j in range(1, n, 2):
                a += 1
                matriz[i][j] = a
              
    return matriz

def patron_f(n : int) -> list[list[int]]:
    matriz = []
    
    for f in range(n):
        fila = []
        for columna in range(n):
            fila.append(0)
        matriz.append(fila)
    a = 1    
    for i in range(len(matriz)):  
        for j in range(n - 1 , n -2 - i, -1):     
            matriz[i][j] = a
            a += 1
                
    return matriz

def patron_g() -> list[list[int]]:
    matriz = []
    
    for f in range(4):
        fila = []
        for columna in range(4):
            fila.append(0)
        matriz.append(fila)
    a = 0
    for borde in range(1):
        final = len(matriz) - 1
        for borde_sup in range(len(matriz)):
            a += 1
            matriz[borde][borde_sup] = a
        for derecha in range(1, len(matriz)):
            a += 1
            matriz[derecha][final] = a
        for abajo in range(final -1, -1, -1):
            a += 1
            matriz[final][abajo] = a
        for arriba in range(2, 0, -1):
            a += 1
            matriz[arriba][0] = a
        for derecha in range(1, 3):
            a += 1
            matriz[1][derecha] = a
        for abajo in range(2, 3):
            a += 1
            matriz[abajo][2] = a
        for izquierda in range(1, 2):
            a += 1
            matriz[2][izquierda] = a
       
    return matriz


def main() -> None:
    n = int(input("Ingrese el tamaño de la matriz: "))
    matriz = patron_a(n)
    print(matriz)

    matriz = patron_b(n)
    print(matriz)

    matriz = patron_c(n)
    print(matriz)

    matriz = patron_d(n)
    print(matriz)

    matriz = patron_e(n)
    print(matriz)
    matriz = patron_f(n)
    print(matriz)
    matriz = patron_g()
    print(matriz)


    

if __name__ == "__main__":
    main()



