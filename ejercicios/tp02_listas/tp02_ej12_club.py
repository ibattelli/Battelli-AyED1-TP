"""Resolver el siguiente problema, utilizando funciones:
Se desea llevar un registro de los socios que visitan un club cada día. Para ello, se
ingresa el número de socio de cinco dígitos hasta ingresar un cero como fin de car-
ga. Se solicita:
a. Informar para cada socio, cuántas veces ingresó al club. Cada socio debe
aparecer una sola vez en el informe.
b. Solicitar un número de socio que se dio de baja del club y eliminar todos sus
ingresos. Mostrar los registros de entrada al club antes y después de
eliminarlo. Informar cuántos ingresos se eliminaron."""

def registro_socios() -> list[int]:
    socios = []
    while True:
        n_socio = int(input("Ingrese el número de socio: "))
        if n_socio == 0:
            break
        while n_socio < 10000 or n_socio > 99999:
            n_socio = int(input("Reingrese el número de socio: "))
            if n_socio == 0:
                break
        socios.append(n_socio)
    return socios

def cant_ingresos(socios: list[int]) -> None:
    socios_revisados = []
    for socio in socios:
        if socio not in socios_revisados:
            socios_revisados.append(socio)
            contador = socios.count(socio)
            if contador > 1:
                print(f"El socio {socio} ingresó {contador} veces al club")
            else:
                print(f"El socio {socio} ingresó {contador} vez al club")
            contador = 0



def dar_baja(socios: list[int]) -> None:
    baja = int(input("Ingrese el número de socio para dar de baja: "))
    while baja < 10000 or baja > 99999:
        baja = int(input("Reingrese el número de socio: "))
    if baja not in socios:
        print("No se encontró el número de socio ingresado.")
    else:
        i = 0
        eliminados = 0
        socios_nuevo = []
        socios_nuevo = socios.copy()
        while i < len(socios_nuevo):
            if socios_nuevo[i] == baja:
                del socios_nuevo[i]
                eliminados += 1
            else:
                i += 1
        print(f"Registro antes de eliminar: {socios}")
        print(f"Registro despues de eliminar: {socios_nuevo}")
        print(f"Se eliminaron {eliminados} ingresos.")


def main() -> None:
    socios = registro_socios()
    cant_ingresos(socios)
    dar_baja(socios)
        
if __name__ == "__main__":
    main()
    