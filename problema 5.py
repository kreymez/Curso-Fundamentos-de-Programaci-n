# Matriz de datos del proyecto:
# Columna 0: ID de Tarea
# Columna 1: Estado ("Completado", "Pendiente", "En Curso")
# Columna 2: Recurso Asignado

DATOS_PROYECTO = [
    [101, "Completado", "Ana"],
    [102, "Pendiente", "Luis"],
    [103, "En Curso", "Ana"],
    [104, "Pendiente", "Marta"]
]

INDICE_ID = 0
INDICE_ESTADO = 1
INDICE_RECURSO = 2


# Validación de la matriz
def validar_matriz(matriz):
    if not matriz:
        raise ValueError("La matriz está vacía.")
    
    for fila in matriz:
        if not isinstance(fila, list) or len(fila) != 3:
            raise ValueError("Cada fila debe ser una lista con 3 elementos.")


#Contar tareas por estado
def contar_tareas_por_estado(matriz, estado_objetivo):
    contador = 0
    for tarea in matriz:
        if tarea[INDICE_ESTADO] == estado_objetivo:
            contador += 1
    return contador


#Obtener lista de recursos
def obtener_recursos(matriz):
    return [tarea[INDICE_RECURSO] for tarea in matriz]


#Contar tareas por recurso
def contar_tareas_por_recurso(matriz):
    conteo = {}
    for tarea in matriz:
        recurso = tarea[INDICE_RECURSO]
        conteo[recurso] = conteo.get(recurso, 0) + 1
    return conteo


#Resumen de tareas por estado
def resumen_estados(matriz):
    resumen = {}
    for tarea in matriz:
        estado = tarea[INDICE_ESTADO]
        resumen[estado] = resumen.get(estado, 0) + 1
    return resumen


#Transpuesta de la matriz (opcional, pero útil)
def obtener_matriz_transpuesta(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    
    transpuesta = []
    
    for j in range(columnas):
        columna = [matriz[i][j] for i in range(filas)]
        transpuesta.append(columna)
    
    return transpuesta


#Generar informe completo
def generar_informe(matriz):
    try:
        validar_matriz(matriz)

        print("\n" + "="*60)
        print("INFORME DE TAREAS DEL PROYECTO")
        print("="*60)

        #Resumen por estado
        print("\n Resumen por estado:")
        for estado, cantidad in resumen_estados(matriz).items():
            print(f"  - {estado}: {cantidad}")

        # Tareas por recurso
        print("\n Tareas por recurso:")
        for recurso, cantidad in contar_tareas_por_recurso(matriz).items():
            print(f"  - {recurso}: {cantidad}")

        # Tareas pendientes
        pendientes = contar_tareas_por_estado(matriz, "Pendiente")
        print(f"\n Total de tareas pendientes: {pendientes}")

        # 📋 Listado completo
        print("\n Lista de tareas:")
        for tarea in matriz:
            print(f"  ID: {tarea[INDICE_ID]} | Estado: {tarea[INDICE_ESTADO]} | Recurso: {tarea[INDICE_RECURSO]}")

        # Mostrar transpuesta (opcional)
        print("\n Matriz transpuesta:")
        transpuesta = obtener_matriz_transpuesta(matriz)
        for fila in transpuesta:
            print(f"  {fila}")

        print("="*60)

    except Exception as e:
        print(f"❌ Error: {e}")


# ▶Ejecutar programa
generar_informe(DATOS_PROYECTO)