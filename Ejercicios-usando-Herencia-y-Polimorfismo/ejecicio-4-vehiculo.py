class Vehiculo:
    """Clase base para todos los vehículos"""
    
    def __init__(self, marca, modelo, velocidad_maxima):
        self.marca = marca
        self.modelo = modelo
        self.velocidad_maxima = velocidad_maxima
        self.velocidad_actual = 0
        self.encendido = False
    
    def mover(self):
        """Método que debe ser implementado por las clases hijas"""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def encender(self):
        """Método común para encender el vehículo"""
        if not self.encendido:
            self.encendido = True
            return f"{self.marca} {self.modelo} se ha encendido"
        return f"{self.marca} {self.modelo} ya está encendido"
    
    def apagar(self):
        """Método común para apagar el vehículo"""
        if self.encendido:
            self.encendido = False
            self.velocidad_actual = 0
            return f"{self.marca} {self.modelo} se ha apagado"
        return f"{self.marca} {self.modelo} ya está apagado"
    
    def acelerar(self, incremento):
        """Método común para acelerar"""
        if self.encendido:
            nueva_velocidad = self.velocidad_actual + incremento
            self.velocidad_actual = min(nueva_velocidad, self.velocidad_maxima)
            return f"Velocidad actual: {self.velocidad_actual} km/h"
        return "Primero debe encender el vehículo"
    
    def frenar(self, decremento):
        """Método común para frenar"""
        if self.encendido:
            nueva_velocidad = self.velocidad_actual - decremento
            self.velocidad_actual = max(nueva_velocidad, 0)
            return f"Velocidad actual: {self.velocidad_actual} km/h"
        return "El vehículo está apagado"
    
    def informacion(self):
        """Método común para mostrar información"""
        estado = "Encendido" if self.encendido else "Apagado"
        return f"{self.__class__.__name__}: {self.marca} {self.modelo} - Estado: {estado} - Velocidad: {self.velocidad_actual} km/h"


class Carro(Vehiculo):
    """Clase hija que representa un Carro"""
    
    def __init__(self, marca, modelo, velocidad_maxima, tipo_combustible, num_puertas):
        super().__init__(marca, modelo, velocidad_maxima)
        self.tipo_combustible = tipo_combustible
        self.num_puertas = num_puertas
        self.marcha_actual = "N"  # N: Neutral, P: Park, R: Reverse, D: Drive
    
    def mover(self):
        """Implementación específica para carro"""
        if not self.encendido:
            return f"El carro {self.marca} {self.modelo} necesita estar encendido para moverse"
        
        if self.marcha_actual == "P":
            return f"El carro {self.marca} {self.modelo} está en Park, cambia a Drive o Reverse"
        elif self.marcha_actual == "N":
            return f"El carro {self.marca} {self.modelo} está en Neutral"
        elif self.marcha_actual == "R":
            return f"El carro {self.marca} {self.modelo} se mueve en reversa a {self.velocidad_actual} km/h"
        elif self.marcha_actual == "D":
            return f"El carro {self.marca} {self.modelo} se mueve hacia adelante a {self.velocidad_actual} km/h"
    
    def cambiar_marcha(self, nueva_marcha):
        """Método específico para carro - cambiar marchas"""
        marchas_validas = ["P", "R", "N", "D"]
        if nueva_marcha in marchas_validas:
            self.marcha_actual = nueva_marcha
            return f"Marcha cambiada a {nueva_marcha}"
        return "Marcha no válida"
    
    def informacion(self):
        """Información específica del carro"""
        info_base = super().informacion()
        return f"{info_base} - Combustible: {self.tipo_combustible} - Puertas: {self.num_puertas} - Marcha: {self.marcha_actual}"


class Bicicleta(Vehiculo):
    """Clase hija que representa una Bicicleta"""
    
    def __init__(self, marca, modelo, tipo_bicicleta, num_cambios):
        # Velocidad máxima típica de bicicleta
        super().__init__(marca, modelo, velocidad_maxima=50)
        self.tipo_bicicleta = tipo_bicicleta  # Montaña, Ruta, Urbana, etc.
        self.num_cambios = num_cambios
        self.cambio_actual = 1
        self.pedaleando = False
    
    def mover(self):
        """Implementación específica para bicicleta"""
        if not self.pedaleando:
            return f"La bicicleta {self.marca} {self.modelo} necesita que pedalees para moverse"
        
        return f"La bicicleta {self.marca} {self.modelo} se mueve pedaleando a {self.velocidad_actual} km/h en el cambio {self.cambio_actual}"
    
    def empezar_pedalear(self):
        """Método específico para bicicleta - empezar a pedalear"""
        self.pedaleando = True
        return f"Empezaste a pedalear la bicicleta {self.marca} {self.modelo}"
    
    def dejar_pedalear(self):
        """Método específico para bicicleta - dejar de pedalear"""
        self.pedaleando = False
        self.velocidad_actual = 0
        return f"Dejaste de pedalear la bicicleta {self.marca} {self.modelo}"
    
    def cambiar_marcha(self, nueva_marcha):
        """Método específico para bicicleta - cambiar marchas"""
        if 1 <= nueva_marcha <= self.num_cambios:
            self.cambio_actual = nueva_marcha
            return f"Cambio ajustado a {nueva_marcha}"
        return f"Cambio no válido. Debe estar entre 1 y {self.num_cambios}"
    
    def acelerar(self, incremento):
        """Sobrescribir acelerar para bicicleta"""
        if self.pedaleando:
            return super().acelerar(incremento)
        return "Debes empezar a pedalear primero"
    
    def informacion(self):
        """Información específica de la bicicleta"""
        info_base = super().informacion()
        estado_pedal = "Pedaleando" if self.pedaleando else "Sin pedalear"
        return f"{info_base} - Tipo: {self.tipo_bicicleta} - Cambios: {self.num_cambios} - Estado: {estado_pedal}"


class Motocicleta(Vehiculo):
    """Clase hija que representa una Motocicleta"""
    
    def __init__(self, marca, modelo, velocidad_maxima, cilindrada):
        super().__init__(marca, modelo, velocidad_maxima)
        self.cilindrada = cilindrada  # en cc
        self.marcha_actual = 0  # 0: Neutral, 1-6: Marchas
    
    def mover(self):
        """Implementación específica para motocicleta"""
        if not self.encendido:
            return f"La motocicleta {self.marca} {self.modelo} necesita estar encendida"
        
        if self.marcha_actual == 0:
            return f"La motocicleta {self.marca} {self.modelo} está en Neutral"
        else:
            return f"La motocicleta {self.marca} {self.modelo} se mueve en {self.marcha_actual}ª marcha a {self.velocidad_actual} km/h"
    
    def cambiar_marcha(self, nueva_marcha):
        """Método específico para motocicleta - cambiar marchas"""
        if 0 <= nueva_marcha <= 6:
            self.marcha_actual = nueva_marcha
            return f"Marcha cambiada a {nueva_marcha}"
        return "Marcha no válida"
    
    def hacer_caballito(self):
        """Método específico para motocicleta"""
        if self.velocidad_actual > 20:
            return f"¡{self.marca} {self.modelo} está haciendo un caballito! 🏍️"
        return "Necesitas más velocidad para hacer un caballito"
    
    def informacion(self):
        """Información específica de la motocicleta"""
        info_base = super().informacion()
        return f"{info_base} - Cilindrada: {self.cilindrada}cc - Marcha: {self.marcha_actual}"


class Barco(Vehiculo):
    """Clase hija que representa un Barco"""
    
    def __init__(self, marca, modelo, velocidad_maxima, eslora, tipo_agua):
        super().__init__(marca, modelo, velocidad_maxima)
        self.eslora = eslora  # longitud en metros
        self.tipo_agua = tipo_agua  # dulce, salada
        self.anclado = True
    
    def mover(self):
        """Implementación específica para barco"""
        if self.anclado:
            return f"El barco {self.marca} {self.modelo} no puede moverse porque está anclado"
        
        if not self.encendido:
            return f"El barco {self.marca} {self.modelo} necesita estar encendido"
        
        return f"El barco {self.marca} {self.modelo} navega a {self.velocidad_actual} nudos en agua {self.tipo_agua}"
    
    def levantar_ancla(self):
        """Método específico para barco - levantar ancla"""
        if self.anclado:
            self.anclado = False
            return "Ancla levantada - listo para navegar"
        return "El ancla ya está levantada"
    
    def echar_ancla(self):
        """Método específico para barco - echar ancla"""
        if not self.anclado:
            self.anclado = True
            self.velocidad_actual = 0
            return "Ancla echada - barco detenido"
        return "El ancla ya está echada"
    
    def acelerar(self, incremento):
        """Sobrescribir acelerar para barco"""
        if not self.anclado:
            return super().acelerar(incremento)
        return "Levanta el ancla primero para navegar"
    
    def informacion(self):
        """Información específica del barco"""
        info_base = super().informacion()
        estado_ancla = "Anclado" if self.anclado else "Navegando"
        return f"{info_base} - Eslora: {self.eslora}m - Agua: {self.tipo_agua} - Estado: {estado_ancla}"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE VEHÍCULOS ===\n")
    
    # Crear diferentes tipos de vehículos
    vehiculos = [
        Carro("Toyota", "Corolla", 180, "Gasolina", 4),
        Bicicleta("Trek", "Marlin 5", "Montaña", 21),
        Motocicleta("Honda", "CBR600", 250, 600),
        Barco("Bayliner", "Element E16", 35, 4.88, "dulce")
    ]
    
    # Mostrar información inicial
    print("=== INFORMACIÓN INICIAL DE VEHÍCULOS ===")
    for vehiculo in vehiculos:
        print(vehiculo.informacion())
    
    # Demostración de polimorfismo con el método mover()
    print("\n=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    for vehiculo in vehiculos:
        print(f"{vehiculo.__class__.__name__}: {vehiculo.mover()}")
    
    # Probar cada vehículo individualmente
    print("\n=== PRUEBA DE CARRO ===")
    carro = vehiculos[0]
    print(carro.encender())
    print(carro.cambiar_marcha("D"))
    print(carro.acelerar(60))
    print(carro.mover())
    print(carro.informacion())
    
    print("\n=== PRUEBA DE BICICLETA ===")
    bicicleta = vehiculos[1]
    print(bicicleta.empezar_pedalear())
    print(bicicleta.acelerar(15))
    print(bicicleta.cambiar_marcha(5))
    print(bicicleta.mover())
    print(bicicleta.informacion())
    
    print("\n=== PRUEBA DE MOTOCICLETA ===")
    moto = vehiculos[2]
    print(moto.encender())
    print(moto.cambiar_marcha(1))
    print(moto.acelerar(40))
    print(moto.mover())
    print(moto.hacer_caballito())
    print(moto.informacion())
    
    print("\n=== PRUEBA DE BARCO ===")
    barco = vehiculos[3]
    print(barco.encender())
    print(barco.levantar_ancla())
    print(barco.acelerar(15))
    print(barco.mover())
    print(barco.informacion())
    
    # Mostrar que todos responden al mismo método de manera diferente
    print("\n=== TODOS LOS VEHÍCULOS EN ACCIÓN ===")
    for vehiculo in vehiculos:
        print(f"> {vehiculo.mover()}")