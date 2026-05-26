# Precios de los helados
precios = [2500, 2000, 3800, 4500, 1800]

# Nombres de los helados
nombres = ["Vaso de Helado", "Chococono", "paleta Dracula", "Polet", "Platillo"]

# Contadores
cantidades = [0, 0, 0, 0, 0]
total_helados = 0
total_compra = 0

# Entrada
dinero = int(input("Ingrese dinero disponible: "))

# Proceso de compra
while True:
    print("\n1.Vaso de Helado  2.Chococono  3.paleta Dracula  4.Polet  5.Platillo")
    opcion = int(input("Elija tipo de helado (1-5): "))
    
    if opcion < 1 or opcion > 5:
        print("Opción inválida")
        continue
    
    precio = precios[opcion - 1]
    
    if dinero >= precio:
        dinero -= precio
        total_compra += precio
        total_helados += 1
        cantidades[opcion - 1] += 1
        
        print("Compra realizada. Dinero restante:", dinero)
    else:
        print("No alcanza el dinero")
        break
    
    if dinero < min(precios):
        print("Ya no alcanza para comprar más helados")
        break
    
    seguir = input("¿Desea continuar? (si/no): ")
    if seguir == "no":
        break

# RESULTADOS
print("\n--- RESULTADOS ---")
print("Total helados comprados:", total_helados)

print("\nCantidad por tipo:")
for nombre, cantidad in zip(nombres, cantidades):
    print(nombre, ":", cantidad)

print("\nTotal compra:", total_compra)

if total_helados > 0:
    print("Promedio por helado:", int(total_compra / total_helados))

print("Dinero sobrante:", dinero)