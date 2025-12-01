# Ejercicio 2: Listas
# Crea una lista llamada 'puertos_abiertos' con los valores [22, 80, 443, 8080]
puertos_abiertos = [22, 80, 443, 8080]

print("=== EJERCICIO DE LISTAS ===\n")
print(f"Lista inicial: {puertos_abiertos}")

# a) Agrega el puerto 21 a la lista
puertos_abiertos.append(21)
print(f"\na) Después de agregar puerto 21: {puertos_abiertos}")

# b) Elimina el puerto 8080
puertos_abiertos.remove(8080)
print(f"b) Después de eliminar puerto 8080: {puertos_abiertos}")

# c) Muestra la lista ordenada de menor a mayor
puertos_abiertos.sort()
print(f"c) Lista ordenada de menor a mayor: {puertos_abiertos}")

# Información adicional sobre listas
print("\n=== INFORMACIÓN ADICIONAL ===")
print(f"Lista actual: {puertos_abiertos}")
print(f"Tipo de dato: {type(puertos_abiertos)}")
print(f"Cantidad de puertos: {len(puertos_abiertos)}")
print(f"Primer puerto: {puertos_abiertos[0]}")
print(f"Último puerto: {puertos_abiertos[-1]}")

# Demostración de otras operaciones útiles con listas
print("\n=== OTRAS OPERACIONES ÚTILES ===")
# Insertar en posición específica
puertos_abiertos.insert(1, 25)  # Inserta puerto 25 en posición 1
print(f"Después de insertar puerto 25 en posición 1: {puertos_abiertos}")

# Eliminar por índice
puerto_eliminado = puertos_abiertos.pop(2)  # Elimina elemento en posición 2
print(f"Eliminado puerto {puerto_eliminado} (posición 2): {puertos_abiertos}")

# Revertir orden
puertos_abiertos.reverse()
print(f"Lista en orden inverso: {puertos_abiertos}")