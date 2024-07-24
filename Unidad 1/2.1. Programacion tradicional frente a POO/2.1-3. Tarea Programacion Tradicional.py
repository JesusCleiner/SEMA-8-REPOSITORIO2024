# Programación Tradicional

def ingresar_calificaciones():
    while True:
        try:
            calificacion1 = float(input("Ingrese la primera calificación (sobre 10): "))
            calificacion2 = float(input("Ingrese la segunda calificación (sobre 10): "))
            if 0 <= calificacion1 <= 10 and 0 <= calificacion2 <= 10:
                return calificacion1, calificacion2
            else:
                print("Las calificaciones deben estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def calcular_promedio(calificacion1, calificacion2):
    return (calificacion1 + calificacion2) / 2


def determinar_si_pasa(promedio):
    if promedio >= 14:
        return True
    else:
        return False


def main():
    nombre = input("Ingrese el nombre del alumno: ")
    calificacion1, calificacion2 = ingresar_calificaciones()
    promedio = calcular_promedio(calificacion1, calificacion2)
    pasa = determinar_si_pasa(promedio)

    if pasa:
        print(f"El alumno {nombre} pasa de año con un promedio de {promedio}.")
    else:
        print(f"El alumno {nombre} no pasa de año. Su promedio es {promedio}.")


if __name__ == "__main__":
    main()