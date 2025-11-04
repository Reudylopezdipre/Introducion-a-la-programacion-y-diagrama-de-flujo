# Programa para el Ejercicio 2: Listas

# Crear la lista inicial
puertos_abiertos = [22, 80, 443, 8080]
print("Lista inicial de puertos abiertos:", puertos_abiertos)

# a) Agrega el puerto 21 a la lista
puertos_abiertos.append(21)
print("\na) Después de agregar el puerto 21:", puertos_abiertos)

# b) Elimina el puerto 8080
if 8080 in puertos_abiertos:
    puertos_abiertos.remove(8080)
print("\nb) Después de eliminar el puerto 8080:", puertos_abiertos)

# c) Muestra la lista ordenada de menor a mayor
puertos_ordenados = sorted(puertos_abiertos)
print("\nc) Lista ordenada de menor a mayor:", puertos_ordenados)

# Guardar el programa en un archivo .py
program_code = '''# Programa para el Ejercicio 2: Listas
puertos_abiertos = [22, 80, 443, 8080]
print("Lista inicial de puertos abiertos:", puertos_abiertos)

# a) Agrega el puerto 21 a la lista
puertos_abiertos.append(21)
print("\\na) Después de agregar el puerto 21:", puertos_abiertos)

# b) Elimina el puerto 8080
if 8080 in puertos_abiertos:
    puertos_abiertos.remove(8080)
print("\\nb) Después de eliminar el puerto 8080:", puertos_abiertos)

# c) Muestra la lista ordenada de menor a mayor
puertos_ordenados = sorted(puertos_abiertos)
print("\\nc) Lista ordenada de menor a mayor:", puertos_ordenados)
'''

file_path = '/mnt/data/ejercicio_listas.py'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(program_code)

print(f"\nArchivo guardado en: {file_path}")
