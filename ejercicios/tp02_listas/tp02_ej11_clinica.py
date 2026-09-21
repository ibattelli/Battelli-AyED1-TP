def opciones() -> None:
    print("--Menu--")
    print("a- Mostrar un listado de los pacientes atendidos por urgencia y con turno.")
    print("b- Búsqueda de un número de afiliado e informar cuántas veces fue atendido por turno y cuántas por urgencia.")
    print("c- Salir.")


def ingreso_paciente() -> tuple[list]:
    """Carga el ingreso de los pacientes
    Pre: no hay
    Post: Retorna una tupla con afiliados y urgencia_turno que son listas
    """
    afiliados = []
    urgencia_turno = []
    while True:
        n_afiliado = int(input("Ingrese su número de afiliado: "))
        if n_afiliado == -1:
            break
        while n_afiliado > 9999 or n_afiliado < 1000:
            n_afiliado = int(input("reingrese su número de afiliado: "))
            if n_afiliado == -1:
                break
        if n_afiliado == -1:
            break
        
        ut = int(input("Ingrese el número(0: urgencia o 1: turno): "))

        while ut < 0 or ut > 1:
            ut= int(input("Reingrese el número(0: urgencia o 1: turno): "))

        afiliados.append(n_afiliado)
        urgencia_turno.append(ut)

    return afiliados, urgencia_turno

def mostrar_pacientes(pacientes: tuple[list]) -> None:
    """Informa los pacientes que vinieron por urgencia o con turno
    Pre: pacientes debe ser una tupla con dos listas de números enteros
    Post: Imprime que pacientes vinieron por urgencia o con turno
    """
    print("\n -Lista de pacientes que vinieron por urgencia-")
    for p, _ in enumerate(pacientes[0]):
        if pacientes[1][p] == 0:
            print(f"\n Paciente: {pacientes[0][p]} ")

    print("\n -Lista de pacientes que vinieron con turno-")
    
    for p, _ in enumerate(pacientes[0]):
        if pacientes[1][p] == 1:
            print(f"\nPaciente {pacientes[0][p]}")
                
def busqueda_afiliado(pacientes: tuple[list]) -> None:
    """Busca un afiliado por su número e informa cuantas veces fue atendido por urgencia y con turno
    Pre: pacientes debe ser una tupla con dos listas de números enteros
    Post: imprime cuantas veces fue atendido por urgencia y con turno  
    """
    
    while True:
        buscar = int(input("\nIngrese el número de afiliado: "))
        if buscar == -1:
            break
        while buscar > 9999 or buscar < 1000:
            buscar = int(input("\nreingrese su número de afiliado: "))
            if buscar == -1:
                break
        if buscar == -1:
            break
        if buscar not in pacientes[0]:
            print("\nNo se encontró una persona afiliada con ese número.")
        else:
            contador_urgencia = 0
            contador_turno = 0
            for p, _ in enumerate(pacientes[0]):
                if pacientes[0][p] == buscar:
                    
                    if pacientes[1][p] == 0:
                        contador_urgencia += 1   
                    else:
                        contador_turno += 1
                        
            print(f"\nEl pacientes {buscar} fue atendido {contador_urgencia} veces por urgencia")
            print(f"\nEl pacientes {buscar} fue atendido {contador_turno} veces con turno\n")


def main() -> None:
    pacientes = ingreso_paciente()
    while True:
        op = input("Ingrese la opcion a ejecutar: ")
        if op == "a":
            mostrar_pacientes(pacientes)
        elif op == "b":
            busqueda_afiliado(pacientes)
        elif op == "c":
            print("\nAdios")
            break

if __name__ == "__main__":
    main()
        