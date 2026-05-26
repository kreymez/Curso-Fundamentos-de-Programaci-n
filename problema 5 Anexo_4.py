# ==============================
# CONTROL DE HORAS SEMANALES
# ==============================

# Matriz:
# [Nombre, Lunes, Martes, Miércoles, Jueves, Viernes]

recursos = [
    ["Carlos", 8, 9, 8, 10, 9],
    ["Ana", 7, 8, 7, 8, 7],
    ["Luis", 9, 10, 9, 8, 10],
    ["María", 8, 8, 8, 8, 8]
]

# Función para calcular horas y clasificar jornada
def calcular_horas(recurso):
    nombre = recurso[0]
    horas = recurso[1:]

    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return nombre, total, clasificacion


# Mostrar resultados
print("=== REPORTE SEMANAL ===\n")

for recurso in recursos:
    nombre, total, clasificacion = calcular_horas(recurso)

    print("Recurso:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)
    print("----------------------")