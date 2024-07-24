# Programación Tradicional
# Ejemplo: Gestión de una tabla  de multiplicar
# Definición de variables globales

def generar_tabla_multiplicar(numero, limite=10):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, limite + 1):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    while True:
        try:
            numero = int(input("Ingrese el número para generar su tabla de multiplicar: "))
            limite = int(input("Ingrese el límite para la tabla de multiplicar (opcional, presione enter para usar 10): ") or 10)
            generar_tabla_multiplicar(numero, limite)
            continuar = input("¿Desea generar otra tabla? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()