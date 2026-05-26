# Listas para guardar datos
salarios_A = []
salarios_B = []
salarios_C = []

edades_A = []
edades_B = []
edades_C = []

# Entrada de datos
for i in range(10):
    salario = float(input("Salario: "))
    antiguedad = int(input("Antigüedad: "))
    edad = int(input("Edad: "))

    if antiguedad <= 2:
        salarios_A.append(salario)
        edades_A.append(edad)
    elif antiguedad <= 8:
        salarios_B.append(salario)
        edades_B.append(edad)
    else:
        salarios_C.append(salario)
        edades_C.append(edad)

# Función para mostrar resultados
def mostrar(grupo, salarios, edades, limite, inc1, inc2):
    if len(salarios) > 0:
        prom = sum(salarios) / len(salarios)
        prom_edad = sum(edades) / len(edades)
        inc = inc1 if prom > limite else inc2

        print("\nGrupo", grupo)
        print("Promedio salario:", prom)
        print("Suma salarios:", sum(salarios))
        print("Incremento:", inc, "%")
        print("Promedio edad:", prom_edad)

# Resultados
mostrar("A", salarios_A, edades_A, 2000000, 4, 7)
mostrar("B", salarios_B, edades_B, 2400000, 5, 8)
mostrar("C", salarios_C, edades_C, 3000000, 6, 10)