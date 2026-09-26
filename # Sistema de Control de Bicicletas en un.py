# Sistema de Control de Bicicletas en un Taller
# Programación Orientada a Objetos - Encapsulación

class BicicletaTaller:

    def __init__(self, serial, costo_por_hora):
        self._serial = serial
        self._hora_ingreso = None
        self._hora_salida = None
        self._costo_por_hora = costo_por_hora

    # Guarda la hora en que llega la bicicleta
    def registrar_ingreso(self, hora):
        self._hora_ingreso = hora

    # Guarda la hora en que se retira la bicicleta
    def registrar_salida(self, hora):
        if hora <= self._hora_ingreso:
            print("La hora de salida debe ser mayor a la de ingreso")
            return False
        self._hora_salida = hora
        return True

    # Calcula lo que se debe pagar segun las horas que estuvo la bici
    def calcular_total(self, hora_salida):
        if hora_salida <= self._hora_ingreso:
            print("La hora de salida debe ser mayor a la de ingreso")
            return None
        horas = hora_salida - self._hora_ingreso
        total = horas * self._costo_por_hora
        return total

    def obtener_serial(self):
        return self._serial


# lista donde se van a guardar todas las bicicletas registradas
bicicletas = []


def registrar_bicicleta():
    serial = input("Serial de la bicicleta: ")
    hora_ingreso = float(input("Hora de ingreso: "))
    costo = float(input("Costo por hora: "))

    bici = BicicletaTaller(serial, costo)
    bici.registrar_ingreso(hora_ingreso)
    bicicletas.append(bici)
    print("Bicicleta registrada")


def buscar_bicicleta(serial):
    for bici in bicicletas:
        if bici.obtener_serial() == serial:
            return bici
    return None


def registrar_salida():
    serial = input("Serial de la bicicleta que sale: ")
    bici = buscar_bicicleta(serial)

    if bici == None:
        print("No existe una bicicleta con ese serial")
        return

    hora_salida = float(input("Hora de salida: "))

    if bici.registrar_salida(hora_salida):
        total = bici.calcular_total(hora_salida)
        print("El costo total a pagar es:", total)


def mostrar_bicicletas():
    if len(bicicletas) == 0:
        print("No hay bicicletas registradas")
    for bici in bicicletas:
        print("Serial:", bici.obtener_serial())


# menu principal del programa
opcion = 0
while opcion != 4:
    print("\n1. Registrar ingreso de bicicleta")
    print("2. Registrar salida y calcular costo")
    print("3. Ver bicicletas registradas")
    print("4. Salir")

    opcion = int(input("Elija una opcion: "))

    if opcion == 1:
        registrar_bicicleta()
    elif opcion == 2:
        registrar_salida()
    elif opcion == 3:
        mostrar_bicicletas()
    elif opcion == 4:
        print("Fin del programa")
    else:
        print("Opcion invalida")