class Dispositivo:
    """Clase base para todos los dispositivos electrónicos"""
    
    def __init__(self, marca, modelo, sistema_operativo):
        self.marca = marca
        self.modelo = modelo
        self.sistema_operativo = sistema_operativo
        self.encendido = False
        self.bateria = 100  # Porcentaje de batería
        self.tiempo_encendido = 0  # en minutos
    
    def encender(self):
        """Método que debe ser implementado por las clases hijas"""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def apagar(self):
        """Método común para apagar el dispositivo"""
        if self.encendido:
            self.encendido = False
            return f"{self.marca} {self.modelo} se está apagando..."
        return f"{self.marca} {self.modelo} ya está apagado"
    
    def estado_bateria(self):
        """Método común para verificar batería"""
        return f"Batería al {self.bateria}%"
    
    def cargar(self, cantidad=10):
        """Método común para cargar la batería"""
        self.bateria = min(100, self.bateria + cantidad)
        return f"Cargando... {self.estado_bateria()}"
    
    def usar(self, minutos=10):
        """Método común para usar el dispositivo"""
        if self.encendido:
            self.tiempo_encendido += minutos
            self.bateria = max(0, self.bateria - (minutos // 10))
            return f"Usando {self.marca} {self.modelo} por {minutos} minutos"
        return f"Primero debe encender el dispositivo"
    
    def informacion(self):
        """Método común para mostrar información"""
        estado = "🟢 ENCENDIDO" if self.encendido else "🔴 APAGADO"
        return f"{self.__class__.__name__}: {self.marca} {self.modelo} - {estado} - {self.estado_bateria()} - SO: {self.sistema_operativo}"


class Laptop(Dispositivo):
    """Clase hija que representa una Laptop"""
    
    def __init__(self, marca, modelo, sistema_operativo, ram, almacenamiento, tiene_webcam=True):
        super().__init__(marca, modelo, sistema_operativo)
        self.ram = ram  # en GB
        self.almacenamiento = almacenamiento  # en GB
        self.tiene_webcam = tiene_webcam
        self.brillo_pantalla = 50  # porcentaje
        self.modo_rendimiento = "Equilibrado"
    
    def encender(self):
        """Implementación específica para laptop"""
        if self.bateria <= 5:
            return f"⚠️  Batería crítica ({self.bateria}%). Conecta el cargador para encender {self.marca} {self.modelo}"
        
        if not self.encendido:
            self.encendido = True
            return f"💻 {self.marca} {self.modelo} iniciando {self.sistema_operativo}... ⏳ (RAM: {self.ram}GB)"
        return f"💻 {self.marca} {self.modelo} ya está encendida"
    
    def abrir_programa(self, programa):
        """Método específico para laptop"""
        if self.encendido:
            return f"📂 Abriendo {programa} en {self.marca} {self.modelo}..."
        return "La laptop debe estar encendida para abrir programas"
    
    def ajustar_brillo(self, nuevo_brillo):
        """Método específico para laptop"""
        if 0 <= nuevo_brillo <= 100:
            self.brillo_pantalla = nuevo_brillo
            return f"🔆 Brillo ajustado al {nuevo_brillo}%"
        return "El brillo debe estar entre 0% y 100%"
    
    def cambiar_modo_rendimiento(self, modo):
        """Método específico para laptop"""
        modos_validos = ["Económico", "Equilibrado", "Alto Rendimiento"]
        if modo in modos_validos:
            self.modo_rendimiento = modo
            return f"⚡ Modo de rendimiento cambiado a: {modo}"
        return f"Modo no válido. Opciones: {', '.join(modos_validos)}"
    
    def informacion(self):
        """Información específica de la laptop"""
        info_base = super().informacion()
        return f"{info_base} - RAM: {self.ram}GB - Almacenamiento: {self.almacenamiento}GB - Brillo: {self.brillo_pantalla}%"


class Telefono(Dispositivo):
    """Clase hija que representa un Teléfono"""
    
    def __init__(self, marca, modelo, sistema_operativo, almacenamiento, tiene_biometrico=False):
        super().__init__(marca, modelo, sistema_operativo)
        self.almacenamiento = almacenamiento  # en GB
        self.tiene_biometrico = tiene_biometrico
        self.sim_insertada = True
        self.senal = 4  # 0-5 barras de señal
        self.pantalla_bloqueada = True
    
    def encender(self):
        """Implementación específica para teléfono"""
        if not self.encendido:
            self.encendido = True
            mensaje = f"📱 {self.marca} {self.modelo} arrancando..."
            if self.tiene_biometrico:
                mensaje += " 👁️  Sensor biométrico activado"
            return mensaje
        return f"📱 {self.marca} {self.modelo} ya está encendido"
    
    def desbloquear(self, metodo="patron"):
        """Método específico para teléfono"""
        if self.encendido:
            self.pantalla_bloqueada = False
            if self.tiene_biometrico and metodo == "huella":
                return "🔓 Teléfono desbloqueado con huella dactilar"
            elif metodo == "patron":
                return "🔓 Teléfono desbloqueado con patrón"
            elif metodo == "pin":
                return "🔓 Teléfono desbloqueado con PIN"
            else:
                return "🔓 Teléfono desbloqueado"
        return "El teléfono debe estar encendido para desbloquear"
    
    def hacer_llamada(self, numero):
        """Método específico para teléfono"""
        if self.encendido and not self.pantalla_bloqueada:
            if self.senal > 0:
                return f"📞 Llamando a {numero}... Señal: {'📶' * self.senal}"
            return "❌ Sin señal para hacer llamada"
        return "Desbloquea el teléfono primero"
    
    def enviar_mensaje(self, numero, mensaje):
        """Método específico para teléfono"""
        if self.encendido and not self.pantalla_bloqueada:
            if self.senal > 0:
                return f"💬 Mensaje enviado a {numero}: '{mensaje}'"
            return "❌ Sin señal para enviar mensaje"
        return "Desbloquea el teléfono primero"
    
    def informacion(self):
        """Información específica del teléfono"""
        info_base = super().informacion()
        estado_bloqueo = "🔒 Bloqueado" if self.pantalla_bloqueada else "🔓 Desbloqueado"
        return f"{info_base} - Almacenamiento: {self.almacenamiento}GB - Señal: {'📶' * self.senal} - {estado_bloqueo}"


class Tablet(Dispositivo):
    """Clase hija que representa una Tablet"""
    
    def __init__(self, marca, modelo, sistema_operativo, tamaño_pantalla, es_wifi_only=True):
        super().__init__(marca, modelo, sistema_operativo)
        self.tamaño_pantalla = tamaño_pantalla  # en pulgadas
        self.es_wifi_only = es_wifi_only
        self.orientacion = "vertical"  # vertical u horizontal
        self.apps_abiertas = []
    
    def encender(self):
        """Implementación específica para tablet"""
        if not self.encendido:
            self.encendido = True
            tipo_conexion = "Wi-Fi Only" if self.es_wifi_only else "Wi-Fi + Cellular"
            return f"📟 {self.marca} {self.modelo} iniciando... 📏 Pantalla: {self.tamaño_pantalla}\" - {tipo_conexion}"
        return f"📟 {self.marca} {self.modelo} ya está encendida"
    
    def cambiar_orientacion(self, orientacion):
        """Método específico para tablet"""
        if orientacion in ["vertical", "horizontal"]:
            self.orientacion = orientacion
            return f"🔄 Orientación cambiada a: {orientacion}"
        return "Orientación no válida. Usa 'vertical' u 'horizontal'"
    
    def abrir_app(self, app):
        """Método específico para tablet"""
        if self.encendido:
            if app not in self.apps_abiertas:
                self.apps_abiertas.append(app)
            return f"🔼 Abriendo {app} en modo {self.orientacion}"
        return "La tablet debe estar encendida para abrir apps"
    
    def cerrar_app(self, app):
        """Método específico para tablet"""
        if app in self.apps_abiertas:
            self.apps_abiertas.remove(app)
            return f"🔽o está abierta"
    
    def informacion(self):
        """Información específica de la tablet"""
        info_base = super().informacion()
        apps_abiertas = len(self.apps_abiertas)
        return f"{info_base} - Pantalla: {self.tamaño_pantalla}\" - Orientación: {self.orientacion} - Apps abiertas: {apps_abiertas}"


class SmartWatch(Dispositivo):
    """Clase hija que representa un SmartWatch"""
    
    def __init__(self, marca, modelo, sistema_operativo, resistencia_agua, tiene_gps=True):
        super().__init__(marca, modelo, sistema_operativo)
        self.resistencia_agua = resistencia_agua  # ej: "IP68"
        self.tiene_gps = tiene_gps
        self.pulsaciones_por_minuto = 0
        self.pasos_hoy = 0
        self.conectado_telefono = False
    
    def encender(self):
        """Implementación específica para smartwatch"""
        if not self.encendido:
            self.encendido = True
            mensaje = f"⌚ {self.marca} {self.modelo} activándose..."
            if self.tiene_gps:
                mensaje += "  GPS activo"
            mensaje += f" Resistencia: {self.resistencia_agua}"
            return mensaje
        return f"⌚ {self.marca} {self.modelo} ya está encendido"
    
    def medir_ritmo_cardiaco(self):
        """Método específico para smartwatch"""
        if self.encendido:
            # Simular medición de ritmo cardíaco
            import random
            self.pulsaciones_por_minuto = random.randint(60, 100)
            return f"Ritmo cardíaco: {self.pulsaciones_por_minuto} ppm"
        return "El smartwatch debe estar encendido"
    
    def contar_pasos(self, pasos):
        """Método específico para smartwatch"""
        if self.encendido:
            self.pasos_hoy += pasos
            return f"Pasos hoy: {self.pasos_hoy}"
        return "El smartwatch debe estar encendido"
    
    def conectar_telefono(self):
        """Método específico para smartwatch"""
        self.conectado_telefono = True
        return "📱 Conectado al teléfono - Notificaciones sincronizadas"
    
    def informacion(self):
        """Información específica del smartwatch"""
        info_base = super().informacion()
        estado_conexion = "Conectado 📱" if self.conectado_telefono else "Desconectado"
        return f"{info_base} - Ritmo: {self.pulsaciones_por_minuto}ppm - Pasos: {self.pasos_hoy} - {estado_conexion}"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE DISPOSITIVOS ELECTRÓNICOS ===\n")
    
    # Crear diferentes tipos de dispositivos
    dispositivos = [
        Laptop("Dell", "XPS 13", "Windows 11", 16, 512),
        Telefono("Samsung", "Galaxy S23", "Android", 256, tiene_biometrico=True),
        Tablet("Apple", "iPad Air", "iPadOS", 10.9),
        SmartWatch("Apple", "Watch Series 8", "watchOS", "IP68", tiene_gps=True)
    ]
    
    # Mostrar información inicial
    print("=== INFORMACIÓN INICIAL ===")
    for dispositivo in dispositivos:
        print(dispositivo.informacion())
    
    # Demostración de polimorfismo con el método encender()
    print("\n=== ENCENDIENDO DISPOSITIVOS ===")
    for dispositivo in dispositivos:
        print(f"{dispositivo.__class__.__name__}: {dispositivo.encender()}")
    
    # Probar cada dispositivo individualmente
    print("\n=== PRUEBA DE LAPTOP ===")
    laptop = dispositivos[0]
    print(laptop.encender())  # Ya encendida
    print(laptop.ajustar_brillo(80))
    print(laptop.cambiar_modo_rendimiento("Alto Rendimiento"))
    print(laptop.abrir_programa("Visual Studio Code"))
    print(laptop.usar(30))
    print(laptop.informacion())
    
    print("\n=== PRUEBA DE TELÉFONO ===")
    telefono = dispositivos[1]
    print(telefono.desbloquear("huella"))
    print(telefono.hacer_llamada("+1-234-567-8900"))
    print(telefono.enviar_mensaje("+1-234-567-8900", "¡Hola! ¿Cómo estás?"))
    print(telefono.usar(15))
    print(telefono.cargar(20))
    print(telefono.informacion())
    
    print("\n=== PRUEBA DE TABLET ===")
    tablet = dispositivos[2]
    print(tablet.cambiar_orientacion("horizontal"))
    print(tablet.abrir_app("Netflix"))
    print(tablet.abrir_app("YouTube"))
    print(tablet.cerrar_app("Netflix"))
    print(tablet.usar(45))
    print(tablet.informacion())
    
    print("\n=== PRUEBA DE SMARTWATCH ===")
    smartwatch = dispositivos[3]
    print(smartwatch.medir_ritmo_cardiaco())
    print(smartwatch.contar_pasos(2500))
    print(smartwatch.conectar_telefono())
    print(smartwatch.usar(120))  # 2 horas de uso
    print(smartwatch.informacion())
    
    # Apagar todos los dispositivos
    print("\n=== APAGANDO DISPOSITIVOS ===")
    for dispositivo in dispositivos:
        print(dispositivo.apagar())
    
    # Probar dispositivo con batería baja
    print("\n=== PRUEBA CON BATERÍA BAJA ===")
    laptop_low_battery = Laptop("Lenovo", "ThinkPad", "Windows 10", 8, 256)
    laptop_low_battery.bateria = 3  # Batería crítica
    print(laptop_low_battery.encender())