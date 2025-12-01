class Coche:
    def __init__(self, marca, velocidad=0):
        self.marca = marca
        self.velocidad = max(0, velocidad)  # Velocidad mínima 0
        self.velocidad_maxima = 250  # Límite de velocidad
    
    def aumentar_velocidad(self, incremento):
        """Aumenta la velocidad con validaciones"""
        if incremento <= 0:
            print("⚠️ El incremento debe ser positivo")
            return
        
        nueva_velocidad = self.velocidad + incremento
        
        if nueva_velocidad > self.velocidad_maxima:
            print(f"🚨 ¡No se puede superar los {self.velocidad_maxima} km/h!")
            self.velocidad = self.velocidad_maxima
        else:
            self.velocidad = nueva_velocidad
            print(f"🚗 {self.marca} aceleró {incremento} km/h")
    
    def reducir_velocidad(self, decremento):
        """Reduce la velocidad del coche"""
        if decremento <= 0:
            print("⚠️ El decremento debe ser positivo")
            return
        
        self.velocidad = max(0, self.velocidad - decremento)
        print(f"🔄 {self.marca} redujo {decremento} km/h")
    
    def mostrar_estado(self):
        estado = "🚗 Apagado" if self.velocidad == 0 else "🚗 En movimiento"
        print(f"{estado} - {self.marca}: {self.velocidad} km/h")
    
    def __str__(self):
        return f"Coche {self.marca} - Velocidad: {self.velocidad} km/h"

# Ejemplo de uso
coche1 = Coche("toyota supra", 100)
print(coche1)

coche1.aumentar_velocidad(100)
coche1.mostrar_estado()

coche1.aumentar_velocidad(200)  # Intentar superar el límite
coche1.mostrar_estado()

coche1.reducir_velocidad(50)
coche1.mostrar_estado()