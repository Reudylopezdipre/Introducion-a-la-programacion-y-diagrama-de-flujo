# Ejercicio 1: Tuplas
# Crea una tupla llamada 'vulnerabilidades' que contenga los siguientes elementos:
vulnerabilidades = ('SQL Injection', 'Cross-Site Scripting', 'Buffer Overflow', 'Denegación de Servicio')

print("=== EJERCICIO DE TUPLAS ===\n")

# a) Mostrar el segundo elemento de la tupla
print("a) Segundo elemento de la tupla:")
print(vulnerabilidades[1])
print()

# b) Mostrar los dos últimos elementos
print("b) Dos últimos elementos de la tupla:")
print(vulnerabilidades[-2:])
print()

# c) Intentar modificar un elemento y observar el resultado
print("c) Intentando modificar un elemento...")
try:
    print("Antes de modificar:", vulnerabilidades)
    vulnerabilidades[0] = 'Nuevo ataque'  # Esto generará un error
    print("Después de modificar:", vulnerabilidades)
except TypeError as e:
    print(f"❌ Error al intentar modificar: {e}")
    print("💡 Las tuplas son INMUTABLES - no se pueden modificar después de crearse")
print()

# Información adicional sobre la tupla
print("=== INFORMACIÓN ADICIONAL ===")
print(f"Tupla completa: {vulnerabilidades}")
print(f"Tipo de dato: {type(vulnerabilidades)}")
print(f"Cantidad de elementos: {len(vulnerabilidades)}")