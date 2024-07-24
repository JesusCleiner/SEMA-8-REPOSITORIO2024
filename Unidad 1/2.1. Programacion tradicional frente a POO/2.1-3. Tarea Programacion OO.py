# Programación Orientada a Objetos (POO)
# tabla  de multiplicar

class TablaMultiplicar:
    def __init__(self, numero, limite=10):
        self.numero = numero
        self.limite = limite

    def generar_tabla(self):
        print(f"Tabla de multiplicar del {self.numero}:")
        for i in range(1, self.limite + 1):
            resultado = self.numero * i
            print(f"{self.numero} x {i} = {resultado}")

def main():
    while True:
        try:
            numero = int(input("Ingrese el número para generar su tabla de multiplicar: "))
            limite = int(input("Ingrese el límite para la tabla de multiplicar (opcional, presione enter para usar 10): ") or 10)
            tabla = TablaMultiplicar(numero, limite)
            tabla.generar_tabla()
            continuar = input("¿Desea generar otra tabla? (s/n): ")
            if continuar.lower() != 's':
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()
