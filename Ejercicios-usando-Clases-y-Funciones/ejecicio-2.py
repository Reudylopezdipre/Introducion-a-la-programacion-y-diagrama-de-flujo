class Usuario:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def mostrar_datos(self):
        print(f"Datos del usuario:")
        print(f"  Nombre: {self.nombre}")
        print(f"  Edad: {self.edad}")
    
    def __str__(self):
        return f"Usuario: {self.nombre}, {self.edad} años"

# Ejemplo de uso
usuario1 = Usuario("Carlos López", 30)
usuario1.mostrar_datos()
print(usuario1)  # Esto usará el método __str__