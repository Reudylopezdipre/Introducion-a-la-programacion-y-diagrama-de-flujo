class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
    
    def to_dict(self):
        return {
            'nombre': self.nombre,
            'edad': self.edad
        }

# Crear varios usuarios y mostrar sus datos
usuarios = [
    Usuario("Laura Martínez", 28),
    Usuario("Pedro Sánchez", 35),
    Usuario("Sofía Ramírez", 19)
]

print("=== LISTA DE USUARIOS ===")
for i, usuario in enumerate(usuarios, 1):
    print(f"Usuario {i}: {usuario.mostrar_datos()}")

# Mostrar datos de forma individual
print("\n=== DATOS INDIVIDUALES ===")
for usuario in usuarios:
    usuario.mostrar_datos()
    print("-" * 20)