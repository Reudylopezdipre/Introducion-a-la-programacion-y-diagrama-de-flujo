# Ejercicio 3: Diccionarios
# Crea un diccionario llamado 'dispositivo_red' con la información especificada
dispositivo_red = {
    'IP': '192.168.1.10',
    'Hostname': 'Firewall-Corp', 
    'Estado': 'Activo'
}

print("=== EJERCICIO DE DICCIONARIOS ===\n")
print(f"Diccionario inicial: {dispositivo_red}")

# a) Muestra el valor de la clave 'Hostname'
print(f"\na) Valor de 'Hostname': {dispositivo_red['Hostname']}")

# b) Agrega una nueva clave llamada 'Ubicación' con el valor 'Centro de Datos'
dispositivo_red['Ubicación'] = 'Centro de Datos'
print(f"b) Después de agregar 'Ubicación': {dispositivo_red}")

# c) Cambia el valor de 'Estado' a 'Inactivo'
dispositivo_red['Estado'] = 'Inactivo'
print(f"c) Después de cambiar 'Estado' a 'Inactivo': {dispositivo_red}")

# d) Muestra todo el diccionario actualizado
print(f"\nd) Diccionario actualizado completo:")
for clave, valor in dispositivo_red.items():
    print(f"   {clave}: {valor}")

# Información adicional sobre diccionarios
print("\n=== INFORMACIÓN ADICIONAL ===")
print(f"Tipo de dato: {type(dispositivo_red)}")
print(f"Cantidad de elementos: {len(dispositivo_red)}")
print(f"Claves disponibles: {list(dispositivo_red.keys())}")
print(f"Valores almacenados: {list(dispositivo_red.values())}")

# Demostración de otras operaciones útiles con diccionarios
print("\n=== OTRAS OPERACIONES ÚTILES ===")
# Verificar si existe una clave
if 'IP' in dispositivo_red:
    print(f"✓ La clave 'IP' existe en el diccionario")

# Obtener valor con valor por defecto si no existe
servicio = dispositivo_red.get('Servicio', 'No especificado')
print(f"Servicio (con valor por defecto): {servicio}")

# Eliminar una clave específica
if 'Ubicación' in dispositivo_red:
    ubicacion_eliminada = dispositivo_red.pop('Ubicación')
    print(f"✓ Eliminada ubicación: {ubicacion_eliminada}")

print(f"Diccionario final: {dispositivo_red}")

# Agregar información adicional
dispositivo_red['Puertos_abiertos'] = [22, 80, 443]
dispositivo_red['Tipo'] = 'Firewall'
print(f"\nDiccionario con información extendida: {dispositivo_red}")