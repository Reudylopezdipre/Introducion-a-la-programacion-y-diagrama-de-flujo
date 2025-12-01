class Animal:
    """Clase base para todos los animales"""
    
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        """Método que debe ser implementado por las clases hijas"""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def presentarse(self):
        """Método común para todos los animales"""
        return f"Soy un {self.__class__.__name__} llamado {self.nombre}"


class Perro(Animal):
    """Clase hija que representa un perro"""
    
    def hablar(self):
        return "¡Guau! ¡Guau!"
    
    def mover_cola(self):
        return f"{self.nombre} está moviendo la cola felizmente"


class Gato(Animal):
    """Clase hija que representa un gato"""
    
    def hablar(self):
        return "¡Miau! ¡Miau!"
    
    def ronronear(self):
        return f"{self.nombre} está ronroneando"


class Vaca(Animal):
    """Clase hija que representa una vaca"""
    
    def hablar(self):
        return "¡Muuu!"


class Pato(Animal):
    """Clase hija que representa un pato"""
    
    def hablar(self):
        return "¡Cuac! ¡Cuac!"


# Ejemplo de uso
if __name__ == "__main__":
    # Crear instancias de diferentes animales
    animales = [
        Perro("Rex"),
        Gato("Mishi"),
        Vaca("Lola"),
        Pato("Donald")
    ]
    
    # Demostrar el polimorfismo
    print("=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    for animal in animales:
        print(f"{animal.presentarse()} - Sonido: {animal.hablar()}")
    
    print("\n=== COMPORTAMIENTOS ESPECÍFICOS ===")
    # Usar métodos específicos de cada clase
    perro = Perro("Firulais")
    gato = Gato("Garfield")
    
    print(perro.presentarse())
    print(perro.hablar())
    print(perro.mover_cola())
    
    print(gato.presentarse())
    print(gato.hablar())
    print(gato.ronronear())