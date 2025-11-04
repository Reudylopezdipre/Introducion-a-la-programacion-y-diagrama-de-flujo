# Programa para el Ejercicio 1: Tuplas
# Guarda este archivo como /mnt/data/ejercicio_tuplas.py si quieres descargarlo.

vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

print("Tupla 'vulnerabilidades':", vulnerabilidades)

# a) Muestra el segundo elemento (índice 1)
print("\na) Segundo elemento (vulnerabilidades[1]):", vulnerabilidades[1])

# b) Muestra los dos últimos elementos
print("\nb) Los dos últimos elementos (vulnerabilidades[-2:]):", vulnerabilidades[-2:])

# c) Intenta modificar un elemento y observa el resultado.
print("\nc) Intento de modificar un elemento:")
try:
    vulnerabilidades[0] = 'Inyección SQL'  # intento de modificación (debe fallar)
except TypeError as e:
    print("   Error capturado:", type(e).__name__, "-", e)
    print("   Explicación: Las tuplas son inmutables; no se pueden cambiar sus elementos.")

# Alternativa: convertir a lista para modificar y luego volver a tupla
print("\n   Alternativa: convertir la tupla a lista, modificar y volver a tupla.")
vul_list = list(vulnerabilidades)
print("   Lista antes de modificar:", vul_list)
vul_list[0] = 'Inyección SQL'  # modificación permitida en listas
print("   Lista después de modificar:", vul_list)
vulnerabilidades_mod = tuple(vul_list)
print("   Nueva tupla a partir de la lista modificada:", vulnerabilidades_mod)

# Guardar el programa en un archivo .py para descargar si se desea
program_code = '''# Programa para el Ejercicio 1: Tuplas
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

print("Tupla 'vulnerabilidades':", vulnerabilidades)
print("\\na) Segundo elemento (vulnerabilidades[1]):", vulnerabilidades[1])
print("\\nb) Los dos últimos elementos (vulnerabilidades[-2:]):", vulnerabilidades[-2:])
print("\\nc) Intento de modificar un elemento:")
try:
    vulnerabilidades[0] = 'Inyección SQL'
except TypeError as e:
    print("   Error capturado:", type(e).__name__, "-", e)
    print("   Explicación: Las tuplas son inmutables; no se pueden cambiar sus elementos.")

print("\\n   Alternativa: convertir la tupla a lista, modificar y volver a tupla.")
vul_list = list(vulnerabilidades)
print("   Lista antes de modificar:", vul_list)
vul_list[0] = 'Inyección SQL'
print("   Lista después de modificar:", vul_list)
vulnerabilidades_mod = tuple(vul_list)
print("   Nueva tupla a partir de la lista modificada:", vulnerabilidades_mod)
'''

file_path = '/mnt/data/ejercicio_tuplas.py'
with open(file_path, 'w', encoding='utf-8') as f:
    f.write(program_code)

print(f"\nArchivo guardado en: {file_path}")
