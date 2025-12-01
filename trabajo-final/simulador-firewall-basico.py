import random
import datetime
import json
import csv
from collections import defaultdict
import ipaddress

class SimuladorFirewall:
    def __init__(self):
        # Vectores para datos del sistema
        self.ips_bloqueadas = []  # Lista de IPs bloqueadas
        self.puertos_permitidos = [80, 443, 22, 21, 25, 53, 110, 143]  # Puertos comunes permitidos
        self.protocolos = ["TCP", "UDP", "ICMP", "HTTP", "HTTPS", "FTP", "SSH", "DNS"]
        
        # Matrices para registros de paquetes
        self.registros_paquetes = []  # [timestamp, ip_origen, puerto, protocolo, accion, razon]
        
        # Configuración del firewall
        self.reglas_personalizadas = []
        self.umbral_ataque = 10  # Número de intentos para considerar ataque
        
        # Estadísticas
        self.estadisticas = {
            'total_paquetes': 0,
            'paquetes_permitidos': 0,
            'paquetes_bloqueados': 0,
            'ips_sospechosas': defaultdict(int)
        }
        
        # Cargar configuración inicial
        self._cargar_configuracion_inicial()
    
    def _cargar_configuracion_inicial(self):
        """Carga configuración inicial de IPs bloqueadas y reglas"""
        # IPs maliciosas conocidas (ejemplo)
        self.ips_bloqueadas.extend([
            "192.168.1.100",
            "10.0.0.50", 
            "172.16.0.25",
            "203.0.113.15"
        ])
        
        # Rangos de IPs privadas (generalmente permitidas)
        self.rangos_privados = [
            ipaddress.IPv4Network('10.0.0.0/8'),
            ipaddress.IPv4Network('172.16.0.0/12'),
            ipaddress.IPv4Network('192.168.0.0/16')
        ]
        
        # Agregar reglas personalizadas
        self.agregar_regla_personalizada("BLOQUEAR", "UDP", 123, "Bloqueo de NTP externo")
        self.agregar_regla_personalizada("PERMITIR", "TCP", 22, "SSH permitido")
        self.agregar_regla_personalizada("BLOQUEAR", "TCP", 3389, "Bloqueo de RDP")
    
    def validar_ip(self, ip):
        """Valida que la IP tenga formato correcto"""
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False
    
    def generar_ip_aleatoria(self, tipo="publica"):
        """Genera una dirección IP aleatoria"""
        if tipo == "privada":
            red = random.choice(self.rangos_privados)
            return str(random.choice(list(red.hosts())))
        else:
            return f"{random.randint(1, 223)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(1, 254)}"
    
    def agregar_ip_bloqueada(self, ip):
        """Agrega una IP a la lista de bloqueadas"""
        if self.validar_ip(ip) and ip not in self.ips_bloqueadas:
            self.ips_bloqueadas.append(ip)
            print(f"IP {ip} agregada a la lista de bloqueadas")
            return True
        else:
            print(f"Error: IP {ip} no válida o ya está en la lista")
            return False
    
    def remover_ip_bloqueada(self, ip):
        """Remueve una IP de la lista de bloqueadas"""
        if ip in self.ips_bloqueadas:
            self.ips_bloqueadas.remove(ip)
            print(f"IP {ip} removida de la lista de bloqueadas")
            return True
        else:
            print(f"Error: IP {ip} no encontrada en la lista de bloqueadas")
            return False
    
    def agregar_regla_personalizada(self, accion, protocolo, puerto, descripcion):
        """Agrega una regla personalizada al firewall"""
        regla = {
            'accion': accion,
            'protocolo': protocolo.upper(),
            'puerto': puerto,
            'descripcion': descripcion
        }
        self.reglas_personalizadas.append(regla)
        print(f"Regla agregada: {accion} {protocolo} puerto {puerto} - {descripcion}")
    
    def aplicar_reglas_personalizadas(self, protocolo, puerto):
        """Aplica las reglas personalizadas del firewall"""
        for regla in self.reglas_personalizadas:
            if (regla['protocolo'] == protocolo.upper() and 
                regla['puerto'] == puerto):
                return regla['accion'], regla['descripcion']
        return None, None
    
    def detectar_comportamiento_sospechoso(self, ip_origen):
        """Detecta comportamientos sospechosos basados en frecuencia"""
        # Contar intentos recientes de la misma IP
        tiempo_limite = datetime.datetime.now() - datetime.timedelta(minutes=5)
        intentos_recientes = 0

        for registro in reversed(self.registros_paquetes):
            if registro[0] < tiempo_limite:
                break
            if registro[1] == ip_origen:
                intentos_recientes += 1

        # Actualizar estadísticas
        self.estadisticas['ips_sospechosas'][ip_origen] = intentos_recientes

        # Si hay muchos intentos, bloquear automáticamente
        if intentos_recientes > self.umbral_ataque:
            if ip_origen not in self.ips_bloqueadas:
                self.agregar_ip_bloqueada(ip_origen)
                return True, f"Ataque detectado: {intentos_recientes} intentos en 5 minutos"

        return False, ""    
    def registrar_paquete(self, ip_origen, puerto, protocolo):
        """
        Registra un paquete entrante y decide si permitirlo o bloquearlo
        
        Args:
            ip_origen (str): Dirección IP de origen
            puerto (int): Puerto de destino
            protocolo (str): Protocolo utilizado
        
        Returns:
            dict: Resultado del procesamiento del paquete
        """
        timestamp = datetime.datetime.now()
        self.estadisticas['total_paquetes'] += 1
        
        # Validar IP
        if not self.validar_ip(ip_origen):
            resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo, 
                                           "BLOQUEADO", "IP no válida")
            self.estadisticas['paquetes_bloqueados'] += 1
            return resultado
        
        # Verificar reglas personalizadas primero
        accion_regla, razon_regla = self.aplicar_reglas_personalizadas(protocolo, puerto)
        if accion_regla:
            resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo,
                                           accion_regla, razon_regla)
            if accion_regla == "BLOQUEADO":
                self.estadisticas['paquetes_bloqueados'] += 1
            else:
                self.estadisticas['paquetes_permitidos'] += 1
            return resultado
        
        # Verificar IPs bloqueadas
        if ip_origen in self.ips_bloqueadas:
            resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo,
                                           "BLOQUEADO", "IP en lista negra")
            self.estadisticas['paquetes_bloqueados'] += 1
            return resultado
        
        # Verificar puertos permitidos
        if puerto not in self.puertos_permitidos:
            resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo,
                                           "BLOQUEADO", f"Puerto {puerto} no permitido")
            self.estadisticas['paquetes_bloqueados'] += 1
            return resultado
        
        # Verificar protocolo válido
        if protocolo.upper() not in self.protocolos:
            resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo,
                                           "BLOQUEADO", f"Protocolo {protocolo} no permitido")
            self.estadisticas['paquetes_bloqueados'] += 1
            return resultado
        
        # Detectar comportamiento sospechoso
        ataque_detectado, razon_ataque = self.detectar_comportamiento_sospechoso(ip_origen)
        if ataque_detectado:
            resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo,
                                           "BLOQUEADO", razon_ataque)
            self.estadisticas['paquetes_bloqueados'] += 1
            return resultado
        
        # Si pasa todas las verificaciones, permitir
        resultado = self._crear_registro(timestamp, ip_origen, puerto, protocolo,
                                       "PERMITIDO", "Acceso autorizado")
        self.estadisticas['paquetes_permitidos'] += 1
        return resultado
    
    def _crear_registro(self, timestamp, ip_origen, puerto, protocolo, accion, razon):
        """Crea un registro de paquete y lo agrega a la matriz"""
        registro = [timestamp, ip_origen, puerto, protocolo.upper(), accion, razon]
        self.registros_paquetes.append(registro)
        
        # Generar alerta si es bloqueado
        if accion == "BLOQUEADO":
            self.generar_alertas(registro)
        
        return {
            'timestamp': timestamp,
            'ip_origen': ip_origen,
            'puerto': puerto,
            'protocolo': protocolo,
            'accion': accion,
            'razon': razon
        }
    
    def generar_alertas(self, registro):
        """Genera alertas para paquetes bloqueados"""
        timestamp, ip_origen, puerto, protocolo, accion, razon = registro
        
        if accion == "BLOQUEADO":
            mensaje = f"ALERTA: Paquete BLOQUEADO - IP: {ip_origen}, Puerto: {puerto}, " \
                     f"Protocolo: {protocolo}, Razón: {razon}"
            print(f"🚨 {mensaje}")
            
            # Guardar alerta en archivo
            self._guardar_alerta(mensaje)
    
    def _guardar_alerta(self, mensaje):
        """Guarda alertas en un archivo de log"""
        try:
            with open("alertas_firewall.log", "a", encoding="utf-8") as f:
                f.write(f"{datetime.datetime.now()} - {mensaje}\n")
        except Exception as e:
            print(f"Error guardando alerta: {e}")
    
    def mostrar_registros(self, filtro_ip=None, limite=20):
        """Muestra los registros de paquetes
        
        Args:
            filtro_ip (str): Filtrar por IP específica
            limite (int): Número máximo de registros a mostrar
        """
        print("\n" + "="*100)
        print("REGISTROS DEL FIREWALL")
        print("="*100)
        print(f"{'Timestamp':<20} {'IP Origen':<15} {'Puerto':<8} {'Protocolo':<10} {'Acción':<10} {'Razón'}")
        print("-"*100)
        
        registros_mostrar = self.registros_paquetes[-limite:] if limite > 0 else self.registros_paquetes
        
        for registro in registros_mostrar:
            timestamp, ip_origen, puerto, protocolo, accion, razon = registro
            
            if filtro_ip and ip_origen != filtro_ip:
                continue
            
            # Colorizar la acción
            accion_str = f"🔴 {accion}" if accion == "BLOQUEADO" else f"🟢 {accion}"
            
            print(f"{timestamp.strftime('%Y-%m-%d %H:%M:%S'):<20} {ip_origen:<15} {puerto:<8} "
                  f"{protocolo:<10} {accion_str:<12} {razon}")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del firewall"""
        print("\n" + "="*50)
        print("ESTADÍSTICAS DEL FIREWALL")
        print("="*50)
        
        total = self.estadisticas['total_paquetes']
        permitidos = self.estadisticas['paquetes_permitidos']
        bloqueados = self.estadisticas['paquetes_bloqueados']
        
        if total > 0:
            porcentaje_permitidos = (permitidos / total) * 100
            porcentaje_bloqueados = (bloqueados / total) * 100
        else:
            porcentaje_permitidos = porcentaje_bloqueados = 0
        
        print(f"Total de paquetes: {total}")
        print(f"Paquetes permitidos: {permitidos} ({porcentaje_permitidos:.1f}%)")
        print(f"Paquetes bloqueados: {bloqueados} ({porcentaje_bloqueados:.1f}%)")
        
        # IPs más sospechosas
        print(f"\nIPs más activas/monitoreadas:")
        ips_ordenadas = sorted(self.estadisticas['ips_sospechosas'].items(), 
                              key=lambda x: x[1], reverse=True)[:5]
        
        for ip, intentos in ips_ordenadas:
            estado = "🚨 BLOQUEADA" if ip in self.ips_bloqueadas else "⚠️ MONITOREADA"
            print(f"  {ip}: {intentos} intentos - {estado}")
    
    def mostrar_configuracion(self):
        """Muestra la configuración actual del firewall"""
        print("\n" + "="*50)
        print("CONFIGURACIÓN DEL FIREWALL")
        print("="*50)
        
        print(f"\nIPs Bloqueadas ({len(self.ips_bloqueadas)}):")
        for ip in self.ips_bloqueadas:
            print(f"  🔴 {ip}")
        
        print(f"\nPuertos Permitidos ({len(self.puertos_permitidos)}):")
        print(f"  {', '.join(map(str, sorted(self.puertos_permitidos)))}")
        
        print(f"\nReglas Personalizadas ({len(self.reglas_personalizadas)}):")
        for regla in self.reglas_personalizadas:
            emoji = "🔴" if regla['accion'] == "BLOQUEAR" else "🟢"
            print(f"  {emoji} {regla['accion']} {regla['protocolo']} puerto {regla['puerto']} - {regla['descripcion']}")
    
    def exportar_registros_csv(self, filename="registros_firewall.csv"):
        """Exporta los registros a un archivo CSV"""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Timestamp', 'IP_Origen', 'Puerto', 'Protocolo', 'Accion', 'Razon'])
                
                for registro in self.registros_paquetes:
                    writer.writerow(registro)
            
            print(f"Registros exportados a {filename}")
        except Exception as e:
            print(f"Error exportando registros: {e}")
    
    def simular_trafico(self, cantidad=15):
        """Simula tráfico de red para pruebas"""
        print("Simulando tráfico de red...")
        
        for i in range(cantidad):
            # Generar IP aleatoria (80% privadas, 20% públicas)
            tipo_ip = "privada" if random.random() < 0.8 else "publica"
            ip = self.generar_ip_aleatoria(tipo_ip)
            
            # Ocasionalmente usar IPs bloqueadas conocidas
            if random.random() < 0.2 and self.ips_bloqueadas:
                ip = random.choice(self.ips_bloqueadas)
            
            puerto = random.choice([80, 443, 22, 21, 25, 53, 8080, 3000, 5000, 123])
            protocolo = random.choice(self.protocolos)
            
            self.registrar_paquete(ip, puerto, protocolo)

# Función principal para demostrar el sistema
def main():
    firewall = SimuladorFirewall()
    
    print("🔥 SIMULADOR DE FIREWALL BÁSICO")
    print("="*50)
    
    # Mostrar configuración inicial
    firewall.mostrar_configuracion()
    
    # Simular tráfico
    firewall.simular_trafico(20)
    
    # Agregar algunas IPs manualmente para demostración
    print("\nAgregando IPs manualmente para demostración...")
    firewall.registrar_paquete("192.168.1.100", 80, "TCP")  # IP bloqueada conocida
    firewall.registrar_paquete("10.0.0.50", 22, "SSH")      # Otra IP bloqueada
    firewall.registrar_paquete("8.8.8.8", 53, "DNS")        # DNS de Google (debería pasar)
    
    # Simular ataque (múltiples intentos de misma IP)
    print("\nSimulando comportamiento sospechoso...")
    ip_ataque = "203.0.113.99"
    for i in range(15):
        firewall.registrar_paquete(ip_ataque, random.randint(1000, 65000), "TCP")
    
    # Mostrar resultados
    firewall.mostrar_registros(limite=15)
    firewall.mostrar_estadisticas()
    
    # Exportar registros
    firewall.exportar_registros_csv()
    
    # Mostrar registros filtrados por IP de ataque
    print(f"\nRegistros para IP de ataque {ip_ataque}:")
    firewall.mostrar_registros(filtro_ip=ip_ataque, limite=10)

if __name__ == "__main__":
    main()