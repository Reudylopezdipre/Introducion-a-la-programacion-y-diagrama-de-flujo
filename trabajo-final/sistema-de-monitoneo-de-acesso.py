import random
import datetime
from collections import defaultdict
import csv
import json

class SistemaMonitoreoAccesos:
    def __init__(self):
        # Vectores para usuarios y servidores
        self.usuarios = ["admin", "usuario1", "usuario2", "invitado", "soporte"]
        self.servidores = ["servidor1", "servidor2", "servidor3", "servidor_db", "servidor_web"]
        
        # Matrices para almacenar información de intentos
        self.intentos = []  # Matriz de intentos de acceso
        self.IPs = []       # Matriz de direcciones IP
        self.tipos = []     # Matriz de tipos de acceso
        self.horas = []     # Matriz de horas de acceso
        
        # Configuración del sistema
        self.max_intentos_fallidos = 3
        self.horas_sospechosas = [2, 3, 4, 5]  # Horas de la madrugada
        
    def generar_ip_aleatoria(self):
        """Genera una dirección IP aleatoria"""
        return f"192.168.{random.randint(1, 255)}.{random.randint(1, 255)}"
    
    def generar_tipo_acceso(self):
        """Genera un tipo de acceso aleatorio"""
        tipos = ["login", "consulta", "modificacion", "descarga", "administracion"]
        return random.choice(tipos)
    
    def generar_hora_aleatoria(self):
        """Genera una hora aleatoria en formato HH:MM"""
        hora = random.randint(0, 23)
        minuto = random.randint(0, 59)
        return f"{hora:02d}:{minuto:02d}"
    
    def registrar_intento(self, usuario, servidor, exito=True, ip=None, tipo=None, hora=None):
        """
        Registra un intento de acceso en el sistema
        
        Args:
            usuario (str): Nombre del usuario
            servidor (str): Servidor al que se intenta acceder
            exito (bool): True si el acceso fue exitoso, False si falló
            ip (str): Dirección IP (si None, se genera aleatoria)
            tipo (str): Tipo de acceso (si None, se genera aleatorio)
            hora (str): Hora del acceso (si None, se genera aleatoria)
        """
        # Generar valores si no se proporcionan
        if ip is None:
            ip = self.generar_ip_aleatoria()
        if tipo is None:
            tipo = self.generar_tipo_acceso()
        if hora is None:
            hora = self.generar_hora_aleatoria()
        
        # Registrar el intento en las matrices
        self.intentos.append([usuario, servidor, exito])
        self.IPs.append([usuario, servidor, ip])
        self.tipos.append([usuario, servidor, tipo])
        self.horas.append([usuario, servidor, hora])
        
        print(f"Intento registrado: {usuario} -> {servidor} | Éxito: {exito} | IP: {ip} | Tipo: {tipo} | Hora: {hora}")
        
        # Verificar si genera alerta
        self.generar_alertas(usuario, servidor, ip, tipo, hora, exito)
    
    def generar_alertas(self, usuario, servidor, ip, tipo, hora, exito):
        """
        Genera alertas basadas en patrones sospechosos
        """
        alertas = []
        
        # Verificar intentos fallidos consecutivos
        intentos_fallidos = self.contar_intentos_fallidos_recientes(usuario, 10)  # Últimos 10 minutos
        if intentos_fallidos >= self.max_intentos_fallidos:
            alertas.append(f"ALERTA: {usuario} tiene {intentos_fallidos} intentos fallidos consecutivos")
        
        # Verificar acceso en horas sospechosas
        hora_numero = int(hora.split(':')[0])
        if hora_numero in self.horas_sospechosas:
            alertas.append(f"ALERTA: Acceso sospechoso a las {hora} (madrugada)")
        
        # Verificar múltiples IPs para el mismo usuario
        ips_usuario = self.obtener_ips_por_usuario(usuario)
        if len(ips_usuario) > 2:
            alertas.append(f"ALERTA: Usuario {usuario} accediendo desde {len(ips_usuario)} IPs diferentes")
        
        # Verificar acceso a múltiples servidores en poco tiempo
        servidores_accedidos = self.obtener_servidores_por_usuario_recientes(usuario, 15)  # Últimos 15 minutos
        if len(servidores_accedidos) > 3:
            alertas.append(f"ALERTA: Usuario {usuario} accedió a {len(servidores_accedidos)} servidores en poco tiempo")
        
        # Mostrar alertas
        for alerta in alertas:
            print(f"🚨 {alerta}")
    
    def contar_intentos_fallidos_recientes(self, usuario, minutos):
        """Cuenta intentos fallidos recientes de un usuario"""
        contador = 0
        for intento in reversed(self.intentos):
            if intento[0] == usuario and not intento[2]:
                contador += 1
            else:
                break
        return contador
    
    def obtener_ips_por_usuario(self, usuario):
        """Obtiene todas las IPs desde las que ha accedido un usuario"""
        ips = set()
        for ip_registro in self.IPs:
            if ip_registro[0] == usuario:
                ips.add(ip_registro[2])
        return list(ips)
    
    def obtener_servidores_por_usuario_recientes(self, usuario, minutos):
        """Obtiene servidores a los que ha accedido un usuario recientemente"""
        servidores = set()
        for intento in self.intentos:
            if intento[0] == usuario:
                servidores.add(intento[1])
        return list(servidores)
    
    def mostrar_reporte(self, usuario_filtro=None, servidor_filtro=None):
        """
        Muestra un reporte completo de los accesos
        
        Args:
            usuario_filtro (str): Filtrar por usuario específico
            servidor_filtro (str): Filtrar por servidor específico
        """
        print("\n" + "="*80)
        print("REPORTE DE ACCESOS AL SISTEMA")
        print("="*80)
        
        # Estadísticas generales
        total_intentos = len(self.intentos)
        intentos_exitosos = sum(1 for intento in self.intentos if intento[2])
        intentos_fallidos = total_intentos - intentos_exitosos
        
        print(f"Total de intentos: {total_intentos}")
        print(f"Intentos exitosos: {intentos_exitosos} ({intentos_exitosos/total_intentos*100:.1f}%)")
        print(f"Intentos fallidos: {intentos_fallidos} ({intentos_fallidos/total_intentos*100:.1f}%)")
        
        # Reporte por usuario
        print("\n--- ESTADÍSTICAS POR USUARIO ---")
        estadisticas_usuario = defaultdict(lambda: {'exitosos': 0, 'fallidos': 0})
        
        for intento in self.intentos:
            usuario = intento[0]
            if usuario_filtro and usuario != usuario_filtro:
                continue
            if intento[2]:
                estadisticas_usuario[usuario]['exitosos'] += 1
            else:
                estadisticas_usuario[usuario]['fallidos'] += 1
        
        for usuario, stats in estadisticas_usuario.items():
            total = stats['exitosos'] + stats['fallidos']
            print(f"{usuario}: {stats['exitosos']} exitosos, {stats['fallidos']} fallidos (Total: {total})")
        
        # Reporte por servidor
        print("\n--- ESTADÍSTICAS POR SERVIDOR ---")
        estadisticas_servidor = defaultdict(lambda: {'exitosos': 0, 'fallidos': 0})
        
        for intento in self.intentos:
            servidor = intento[1]
            if servidor_filtro and servidor != servidor_filtro:
                continue
            if intento[2]:
                estadisticas_servidor[servidor]['exitosos'] += 1
            else:
                estadisticas_servidor[servidor]['fallidos'] += 1
        
        for servidor, stats in estadisticas_servidor.items():
            total = stats['exitosos'] + stats['fallidos']
            print(f"{servidor}: {stats['exitosos']} exitosos, {stats['fallidos']} fallidos (Total: {total})")
        
        # Últimos 10 intentos
        print("\n--- ÚLTIMOS 10 INTENTOS ---")
        for i, intento in enumerate(self.intentos[-10:], 1):
            usuario, servidor, exito = intento
            ip = self.IPs[-i][2] if len(self.IPs) >= i else "N/A"
            tipo = self.tipos[-i][2] if len(self.tipos) >= i else "N/A"
            hora = self.horas[-i][2] if len(self.horas) >= i else "N/A"
            estado = "EXITOSO" if exito else "FALLIDO"
            print(f"{i}. {usuario} -> {servidor} | {estado} | IP: {ip} | Tipo: {tipo} | Hora: {hora}")
    
    def exportar_reporte_csv(self, filename="reporte_accesos.csv"):
        """Exporta el reporte a un archivo CSV"""
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Usuario', 'Servidor', 'Éxito', 'IP', 'Tipo', 'Hora'])
            
            for i in range(len(self.intentos)):
                usuario, servidor, exito = self.intentos[i]
                ip = self.IPs[i][2]
                tipo = self.tipos[i][2]
                hora = self.horas[i][2]
                writer.writerow([usuario, servidor, exito, ip, tipo, hora])
        
        print(f"Reporte exportado a {filename}")
    
    def simular_intentos_acceso(self, cantidad=20):
        """Simula múltiples intentos de acceso para pruebas"""
        for _ in range(cantidad):
            usuario = random.choice(self.usuarios)
            servidor = random.choice(self.servidores)
            exito = random.random() > 0.2  # 80% de éxito
            self.registrar_intento(usuario, servidor, exito)

# Función principal para demostrar el sistema
def main():
    sistema = SistemaMonitoreoAccesos()
    
    print("SISTEMA DE MONITOREO DE ACCESOS")
    print("Simulando intentos de acceso...")
    
    # Simular algunos intentos de acceso
    sistema.simular_intentos_acceso(15)
    
    # Registrar algunos intentos manualmente para demostrar alertas
    print("\nRegistrando intentos específicos para demostración de alertas...")
    
    # Intentos fallidos consecutivos
    sistema.registrar_intento("usuario1", "servidor1", False, "192.168.1.100", "login", "14:30")
    sistema.registrar_intento("usuario1", "servidor1", False, "192.168.1.100", "login", "14:31")
    sistema.registrar_intento("usuario1", "servidor1", False, "192.168.1.100", "login", "14:32")
    
    # Acceso en hora sospechosa
    sistema.registrar_intento("invitado", "servidor_db", True, "192.168.1.150", "consulta", "03:45")
    
    # Múltiples IPs para mismo usuario
    sistema.registrar_intento("admin", "servidor_web", True, "192.168.1.200", "administracion", "10:15")
    sistema.registrar_intento("admin", "servidor1", True, "192.168.2.50", "modificacion", "10:20")
    sistema.registrar_intento("admin", "servidor2", True, "192.168.3.100", "consulta", "10:25")
    
    # Mostrar reporte completo
    sistema.mostrar_reporte()
    
    # Exportar reporte
    sistema.exportar_reporte_csv()
    
    # Mostrar reporte filtrado por usuario
    print("\n" + "="*50)
    print("REPORTE FILTRADO POR USUARIO: admin")
    print("="*50)
    sistema.mostrar_reporte(usuario_filtro="admin")

if __name__ == "__main__":
    main()