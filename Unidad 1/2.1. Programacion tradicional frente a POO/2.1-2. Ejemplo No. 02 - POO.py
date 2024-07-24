# Programación Orientada a Objetos (POO)
# Ejemplo: Calculadora basica

class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"


def menu():
    print("Seleccione la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")


def main():
    calculadora = Calculadora()

    while True:
        menu()
        opcion = input("Ingrese su elección: ")

        if opcion == '5':
            break

        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            print("Resultado:", calculadora.sumar(num1, num2))
        elif opcion == '2':
            print("Resultado:", calculadora.restar(num1, num2))
        elif opcion == '3':
            print("Resultado:", calculadora.multiplicar(num1, num2))
        elif opcion == '4':
            print("Resultado:", calculadora.dividir(num1, num2))
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()