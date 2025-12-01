import math

class Figura:
    """Clase base para todas las figuras geométricas"""
    
    def area(self):
        """Método que debe ser implementado por las clases hijas"""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def perimetro(self):
        """Método que debe ser implementado por las clases hijas"""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def describir(self):
        """Método común para todas las figuras"""
        return f"{self.__class__.__name__} - Área: {self.area():.2f} - Perímetro: {self.perimetro():.2f}"


class Circulo(Figura):
    """Clase hija que representa un Círculo"""
    
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        """Calcula el área del círculo: π * r²"""
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        """Calcula el perímetro del círculo: 2 * π * r"""
        return 2 * math.pi * self.radio
    
    def describir(self):
        info_base = super().describir()
        return f"{info_base} - Radio: {self.radio}"


class Cuadrado(Figura):
    """Clase hija que representa un Cuadrado"""
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        """Calcula el área del cuadrado: lado²"""
        return self.lado ** 2
    
    def perimetro(self):
        """Calcula el perímetro del cuadrado: 4 * lado"""
        return 4 * self.lado
    
    def describir(self):
        info_base = super().describir()
        return f"{info_base} - Lado: {self.lado}"


class Rectangulo(Figura):
    """Clase hija que representa un Rectángulo"""
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        """Calcula el área del rectángulo: base * altura"""
        return self.base * self.altura
    
    def perimetro(self):
        """Calcula el perímetro del rectángulo: 2*(base + altura)"""
        return 2 * (self.base + self.altura)
    
    def describir(self):
        info_base = super().describir()
        return f"{info_base} - Base: {self.base}, Altura: {self.altura}"


class Triangulo(Figura):
    """Clase hija que representa un Triángulo"""
    
    def __init__(self, base, altura, lado1=None, lado2=None, lado3=None):
        self.base = base
        self.altura = altura
        # Si no se proporcionan lados, asumimos triángulo con base y altura
        self.lado1 = lado1 if lado1 else base
        self.lado2 = lado2 if lado2 else altura
        self.lado3 = lado3 if lado3 else math.sqrt(base**2 + altura**2)  # hipotenusa por defecto
    
    def area(self):
        """Calcula el área del triángulo: (base * altura) / 2"""
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        """Calcula el perímetro del triángulo: suma de todos los lados"""
        return self.lado1 + self.lado2 + self.lado3
    
    def describir(self):
        info_base = super().describir()
        return f"{info_base} - Base: {self.base}, Altura: {self.altura}"


class TrianguloEquilatero(Figura):
    """Clase hija que representa un Triángulo Equilátero"""
    
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        """Calcula el área del triángulo equilátero: (√3/4) * lado²"""
        return (math.sqrt(3) / 4) * self.lado ** 2
    
    def perimetro(self):
        """Calcula el perímetro del triángulo equilátero: 3 * lado"""
        return 3 * self.lado
    
    def describir(self):
        info_base = super().describir()
        return f"{info_base} - Lado: {self.lado}"


class Elipse(Figura):
    """Clase hija que representa una Elipse"""
    
    def __init__(self, semieje_mayor, semieje_menor):
        self.semieje_mayor = semieje_mayor
        self.semieje_menor = semieje_menor
    
    def area(self):
        """Calcula el área de la elipse: π * semieje_mayor * semieje_menor"""
        return math.pi * self.semieje_mayor * self.semieje_menor
    
    def perimetro(self):
        """Calcula el perímetro aproximado de la elipse usando la fórmula de Ramanujan"""
        a, b = self.semieje_mayor, self.semieje_menor
        h = ((a - b) / (a + b)) ** 2
        return math.pi * (a + b) * (1 + (3 * h) / (10 + math.sqrt(4 - 3 * h)))
    
    def describir(self):
        info_base = super().describir()
        return f"{info_base} - Semiejes: {self.semieje_mayor} x {self.semieje_menor}"


# Función utilitaria para mostrar información de figuras
def mostrar_figuras(figuras):
    """Muestra información de una lista de figuras"""
    for figura in figuras:
        print(figura.describir())


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE FIGURAS GEOMÉTRICAS ===\n")
    
    # Crear diferentes figuras geométricas
    figuras = [
        Circulo(5),
        Cuadrado(4),
        Rectangulo(6, 3),
        Triangulo(4, 3),
        TrianguloEquilatero(5),
        Elipse(5, 3)
    ]
    
    # Mostrar información de todas las figuras
    print("=== INFORMACIÓN DE FIGURAS ===")
    mostrar_figuras(figuras)
    
    # Demostración de polimorfismo
    print("\n=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    for figura in figuras:
        print(f"{figura.__class__.__name__}:")
        print(f"  - Área: {figura.area():.2f}")
        print(f"  - Perímetro: {figura.perimetro():.2f}")
    
    # Comparar áreas de diferentes figuras
    print("\n=== COMPARACIÓN DE ÁREAS ===")
    figuras_ordenadas = sorted(figuras, key=lambda x: x.area())
    for figura in figuras_ordenadas:
        print(f"{figura.__class__.__name__}: {figura.area():.2f} unidades cuadradas")
    
    # Ejemplos específicos con diferentes dimensiones
    print("\n=== EJEMPLOS ESPECÍFICOS ===")
    ejemplos = [
        Circulo(10),
        Cuadrado(7),
        Rectangulo(8, 5),
        TrianguloEquilatero(6)
    ]
    
    for ejemplo in ejemplos:
        print(ejemplo.describir())