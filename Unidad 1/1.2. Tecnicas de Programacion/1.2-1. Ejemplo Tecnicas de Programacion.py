from abc import ABC, abstractmethod

# Clase base abstracta
class Vehiculo(ABC):
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

    @abstractmethod
    def tipo_de_vehiculo(self):
        pass

    def mostrar_info(self):
        return f'Marca: {self.marca}, Modelo: {self.modelo}, Año: {self.año}'

# Clase Auto que hereda de Vehiculo
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, puertas):
        super().__init__(marca, modelo, año)
        self.puertas = puertas

    def tipo_de_vehiculo(self):
        return "Auto"

    def mostrar_info(self):
        info = super().mostrar_info()
        return f'{info}, Puertas: {self.puertas}'

# Clase Camion que hereda de Vehiculo
class Camion(Vehiculo):
    def __init__(self, marca, modelo, año, capacidad_carga):
        super().__init__(marca, modelo, año)
        self.capacidad_carga = capacidad_carga

    def tipo_de_vehiculo(self):
        return "Camión"

    def mostrar_info(self):
        info = super().mostrar_info()
        return f'{info}, Capacidad de carga: {self.capacidad_carga} kg'

# Clase Trailer que hereda de Vehiculo
class Trailer(Vehiculo):
    def __init__(self, marca, modelo, año, numero_ejes):
        super().__init__(marca, modelo, año)
        self.numero_ejes = numero_ejes

    def tipo_de_vehiculo(self):
        return "Trailer"

    def mostrar_info(self):
        info = super().mostrar_info()
        return f'{info}, Número de ejes: {self.numero_ejes}'

# Clase Moto que hereda de Vehiculo
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, tipo_moto):
        super().__init__(marca, modelo, año)
        self.tipo_moto = tipo_moto

    def tipo_de_vehiculo(self):
        return "Moto"

    def mostrar_info(self):
        info = super().mostrar_info()
        return f'{info}, Tipo de moto: {self.tipo_moto}'

# Función para mostrar el menú y obtener la elección del usuario
def mostrar_menu():
    print("==========================================")
    print("Seleccione el tipo de vehículo:")
    print("1. Auto")
    print("2. Camión")
    print("3. Trailer")
    print("4. Moto")
    print("===========================================")
    return input("Ingrese el número de su elección: ")


# Función principal
def main():
    # Crear instancias de cada clase
    auto = Auto("Toyota", "Corolla", 2020, 4)
    camion = Camion("Mercedes", "Actros", 2019, 18000)
    trailer = Trailer("Volvo", "FH16", 2018, 3)
    moto = Moto("Yamaha", "MT-07", 2021, "Deportiva")

    # Lista de vehículos
    vehiculos = [auto, camion, trailer, moto]

    while True:
        eleccion = mostrar_menu()

        if eleccion in ['1', '2', '3', '4']:
            vehiculo = vehiculos[int(eleccion) - 1]
            print("\nInformación del Vehículo:")
            print(vehiculo.mostrar_info())
            print(f'Tipo de Vehículo: {vehiculo.tipo_de_vehiculo()}\n')
        else:
            print("Elección no válida. Intente de nuevo.")

        continuar = input("¿Desea ver otro vehículo? (s/n): ")
        if continuar.lower() != 's':
            break

if __name__ == "__main__":
    main()