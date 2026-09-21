from random import randint

def crear_matriz() -> list[list[int]]:
    """Crea una matriz de 4 filas y 10 columnas de 0(ceros)
    Pre: no hay
    Post: retorna una matriz de 4 filas y 10 columnas de 0(ceros)
    """
    sala = []
    for fila in range(4):
        f = []
        for butacas in range(10):
            f.append(0)
        sala.append(f)
    return sala

def mostrar_butacas(sala: list[list[int]]) -> None:
    """Muestra el estado de todas las butacas del cine
    Pre: sala debe ser una matriz con números enteros
    Post: imprime todas las butacas que hay en la matriz
    """
    for fila in sala:
        print(fila)
        print()

def reservar(sala: list[list[int]], butaca: tuple[int, int]) -> bool:
    """Reserva una butaca libre
    Pre: sala debe ser una matriz con números enteros
    Post: si la butaca estaba libre, retorna True, sino retorna False
    """
    if sala[butaca[0]][butaca[1]] == 0:
        sala[butaca[0]][butaca[1]] = 1
        return True
    else:
        return False

def cargar_sala(matriz: list[list[int]]) -> list[list[int]]:
    """Carga una matriz con números random entre 0 y 1
    Pre: matriz debe ser una matriz de números enteros.
    Post: retorna la matriz con sus posiciones cargadas aleatoriamente con 0 o 1
    """
    for i, fila in enumerate(matriz):
        for p, butaca in enumerate(fila):
            matriz[i][p] = randint(0, 1)
    return matriz

def butacas_libres(sala: list[list[int]]) -> int:
    """Cuenta la cantidad de butacas que hay libre en la sala
    Pre: sala debe ser una matriz con valores 0 o 1.
    Post: retorna la cantidad de butacas libres de la sala
    """
    contador = 0
    for i, fila in enumerate(sala):
        for p, butaca in enumerate(fila):
            if butaca == 0:
                contador += 1
    return contador  

def butacas_contiguas(sala: list[list[int]]) -> tuple:
    """Busca la secuencia más larga de butacas libres contiguas
    Pre: sala debe ser una matriz con valores 0 o 1
    Post: retorna una tupla con las coordenadas de inicio de la secuencia más larga de butacas libres contiguas. 
    """
    contador_actual = 0
    secuencia_larga = 0
    coordenadas = (0, 0)
    for i, fila in enumerate(sala):
        for p, butaca in enumerate(fila):
            if butaca == 0:
                contador_actual += 1
                if contador_actual > secuencia_larga:
                    secuencia_larga = contador_actual
                    coordenadas = i, p - contador_actual + 1
            else:
                contador_actual = 0
    return coordenadas

def main() -> None:
    sala = crear_matriz()
    sala = cargar_sala(sala)
    mostrar_butacas(sala)
    
    fila = int(input("Ingrese el número de fila: "))
    columna = int(input("Ingrese el número de columna: "))

    butaca = fila, columna
    if reservar(sala, butaca):
        print("Reserva realizada correctamente.")
    else:
        print("La butaca ya se encontraba reservada.")

    mostrar_butacas(sala)

    libres = butacas_libres(sala)
    print(f"Hay {libres} butacas libres.")
    coordenadas = butacas_contiguas(sala)
    print(f"La secuencia más larga empieza en: {coordenadas}")

if __name__ == "__main__":
    main()