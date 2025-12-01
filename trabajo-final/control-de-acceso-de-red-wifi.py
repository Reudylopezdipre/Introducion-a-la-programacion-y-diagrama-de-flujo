import json
import csv
import random
import re
import time
from datetime import datetime, timedelta
from collections import defaultdict
import threading
import socket

class ControlAccesosWiFi:
    def __init__(self, archivo_config="config_wifi.json"):
        # Vectores para dispositivos y usuarios
        self.dispositivos_autorizados = []  # MAC addresses autorizados
        self.dispositivos_bloqueados = []   # MAC addresses bloqueados
        self.usuarios = []                  # Nombres de usuarios
        
        # Matrices para conexiones y registros
        self.conexiones_activas = []        # [mac, ip, usuario, timestamp, ssid]
        self.historial_conexiones = []      # Historial completo de conexiones
        self.limites_usuarios = []          # [usuario, limite_conexiones]
        
        # Configuración
        self.archivo_config = archivo_config
        self.ssid = "MiRedWiFi"
        self.limite_conexiones_global = 5
        self.tiempo_maximo_conexion = 24 * 60 * 60  # 24 horas en segundos
        self.intervalo_verificacion = 60  # 60 segundos
        
        # Estadísticas
        self.estadisticas = {
            'total_conexiones': 0,
            'conexiones_rechazadas': 0,
            'dispositivos_unicos': set(),
            'alertas_generadas': 0
        }
        
        # Hilos para monitoreo
        self.monitoreo_activo = False
        self.hilo_monitoreo = None
        
        # Cargar configuración
        self.cargar_configuracion()
    
    def validar_mac(self, mac: str) -> bool:
        """Valida que la MAC address tenga formato correcto"""
        patron_mac = r'^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
        return re.match(patron_mac, mac) is not None
    
    def validar_ip(self, ip: str) -> bool:
        """Valida que la IP tenga formato correcto"""
        try:
            socket.inet_aton(ip)
            return True
        except socket.error:
            return False
    
    def generar_mac_aleatoria(self) -> str:
        """Genera una MAC address aleatoria válida"""
        mac = [0x00, 0x16, 0x3e,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))
    
    def generar_ip_aleatoria(self) -> str:
        """Genera una dirección IP aleatoria"""
        return f"192.168.1.{random.randint(2, 254)}"
    
    def registrar_dispositivo(self, mac: str, usuario: str, limite_conexiones: int = None) -> bool:
        """
        Registra un dispositivo autorizado en la red WiFi
        
        Args:
            mac (str): MAC address del dispositivo
            usuario (str): Nombre del usuario/propietario
            limite_conexiones (int): Límite de conexiones simultáneas
        
        Returns:
            bool: True si se registró exitosamente
        """
        # Validar MAC
        if not self.validar_mac(mac):
            print(f"Error: MAC address {mac} no válida")
            return False
        
        # Verificar si ya está autorizado
        if mac in self.dispositivos_autorizados:
            print(f"Error: Dispositivo {mac} ya está autorizado")
            return False
        
        # Verificar si está bloqueado
        if mac in self.dispositivos_bloqueados:
            print(f"Error: Dispositivo {mac} está bloqueado")
            return False
        
        # Registrar dispositivo
        self.dispositivos_autorizados.append(mac)
        
        # Registrar usuario si es nuevo
        if usuario not in self.usuarios:
            self.usuarios.append(usuario)
        
        # Establecer límite de conexiones
        if limite_conexiones is None:
            limite_conexiones = self.limite_conexiones_global
        
        self.limites_usuarios.append({
            'usuario': usuario,
            'mac': mac,
            'limite': limite_conexiones
        })
        
        print(f"✅ Dispositivo {mac} registrado para usuario '{usuario}' (Límite: {limite_conexiones} conexiones)")
        
        # Guardar configuración
        self.guardar_configuracion()
        return True
    
    def bloquear_dispositivo(self, mac: str, razon: str = "Violación de políticas") -> bool:
        """
        Bloquea un dispositivo de la red WiFi
        
        Args:
            mac (str): MAC address a bloquear
            razon (str): Razón del bloqueo
        
        Returns:
            bool: True si se bloqueó exitosamente
        """
        if not self.validar_mac(mac):
            print(f"Error: MAC address {mac} no válida")
            return False
        
        # Remover de autorizados si está allí
        if mac in self.dispositivos_autorizados:
            self.dispositivos_autorizados.remove(mac)
        
        # Agregar a bloqueados
        if mac not in self.dispositivos_bloqueados:
            self.dispositivos_bloqueados.append(mac)
        
        # Desconectar si está activo
        self._desconectar_dispositivo(mac)
        
        print(f"🚫 Dispositivo {mac} bloqueado. Razón: {razon}")
        
        # Registrar en historial
        self.registrar_historial("Bloqueo", mac, "", razon)
        
        # Guardar configuración
        self.guardar_configuracion()
        return True
    
    def desbloquear_dispositivo(self, mac: str) -> bool:
        """
        Desbloquea un dispositivo previamente bloqueado
        
        Args:
            mac (str): MAC address a desbloquear
        
        Returns:
            bool: True si se desbloqueó exitosamente
        """
        if mac in self.dispositivos_bloqueados:
            self.dispositivos_bloqueados.remove(mac)
            print(f"✅ Dispositivo {mac} desbloqueado")
            
            # Registrar en historial
            self.registrar_historial("Desbloqueo", mac, "", "Dispositivo desbloqueado")
            
            self.guardar_configuracion()
            return True
        else:
            print(f"Error: Dispositivo {mac} no está bloqueado")
            return False
    
    def validar_acceso(self, mac: str, ip: str, ssid: str = None):
        """
        Valida si un dispositivo puede acceder a la red WiFi
        
        Args:
            mac (str): MAC address del dispositivo
            ip (str): Dirección IP solicitada
            ssid (str): SSID de la red
        
        Returns:
            Dict: Resultado de la validación
        """
        if ssid is None:
            ssid = self.ssid
        
        resultado = {
            'acceso_permitido': False,
            'razon': '',
            'usuario': 'Desconocido',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Validaciones básicas
        if not self.validar_mac(mac):
            resultado['razon'] = 'MAC address no válida'
            self.estadisticas['conexiones_rechazadas'] += 1
            return resultado
        
        if not self.validar_ip(ip):
            resultado['razon'] = 'IP no válida'
            self.estadisticas['conexiones_rechazadas'] += 1
            return resultado
        
        # Verificar si está bloqueado
        if mac in self.dispositivos_bloqueados:
            resultado['razon'] = 'Dispositivo bloqueado'
            self.estadisticas['conexiones_rechazadas'] += 1
            self.generar_alertas(mac, ip, "Intento de acceso desde dispositivo bloqueado")
            return resultado
        
        # Verificar si está autorizado
        if mac not in self.dispositivos_autorizados:
            resultado['razon'] = 'Dispositivo no autorizado'
            self.estadisticas['conexiones_rechazadas'] += 1
            self.generar_alertas(mac, ip, "Intento de acceso desde dispositivo no autorizado")
            return resultado
        
        # Obtener información del usuario
        usuario_info = self._obtener_info_usuario(mac)
        if not usuario_info:
            resultado['razon'] = 'Usuario no encontrado'
            self.estadisticas['conexiones_rechazadas'] += 1
            return resultado
        
        resultado['usuario'] = usuario_info['usuario']
        
        # Verificar límite de conexiones
        if not self._verificar_limite_conexiones(mac, usuario_info):
            resultado['razon'] = 'Límite de conexiones alcanzado'
            self.estadisticas['conexiones_rechazadas'] += 1
            self.generar_alertas(mac, ip, f"Límite de conexiones alcanzado para {usuario_info['usuario']}")
            return resultado
        
        # Verificar tiempo máximo de conexión
        if not self._verificar_tiempo_conexion(mac):
            resultado['razon'] = 'Tiempo máximo de conexión excedido'
            self.estadisticas['conexiones_rechazadas'] += 1
            self.generar_alertas(mac, ip, "Tiempo máximo de conexión excedido")
            return resultado
        
        # Todas las validaciones pasaron
        resultado['acceso_permitido'] = True
        resultado['razon'] = 'Acceso autorizado'
        
        # Registrar conexión
        self._registrar_conexion(mac, ip, usuario_info['usuario'], ssid)
        
        return resultado
    
    def _obtener_info_usuario(self, mac: str):
        """Obtiene la información del usuario basado en la MAC"""
        for usuario_info in self.limites_usuarios:
            if usuario_info['mac'] == mac:
                return usuario_info
        return None
    
    def _verificar_limite_conexiones(self, mac: str, usuario_info):
        """Verifica si el usuario ha alcanzado su límite de conexiones"""
        conexiones_activas_usuario = sum(1 for conexion in self.conexiones_activas 
                                       if conexion['usuario'] == usuario_info['usuario'])
        
        return conexiones_activas_usuario < usuario_info['limite']
    
    def _verificar_tiempo_conexion(self, mac: str) -> bool:
        """Verifica si alguna conexión existente ha excedido el tiempo máximo"""
        ahora = datetime.now()
        for conexion in self.conexiones_activas:
            if conexion['mac'] == mac:
                try:
                    tiempo_conexion = ahora - datetime.strptime(conexion['timestamp'], "%Y-%m-%d %H:%M:%S")
                    if tiempo_conexion.total_seconds() > self.tiempo_maximo_conexion:
                        return False
                except ValueError:
                    # Si hay error en el formato de fecha, continuar
                    continue
        return True
    
    def _registrar_conexion(self, mac: str, ip: str, usuario: str, ssid: str):
        """Registra una nueva conexión activa"""
        conexion = {
            'mac': mac,
            'ip': ip,
            'usuario': usuario,
            'ssid': ssid,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.conexiones_activas.append(conexion)
        self.historial_conexiones.append(conexion)
        self.estadisticas['total_conexiones'] += 1
        self.estadisticas['dispositivos_unicos'].add(mac)
        
        print(f"📱 Conexión establecida: {usuario} ({mac}) -> {ip}")
    
    def _desconectar_dispositivo(self, mac: str):
        """Desconecta un dispositivo de la red"""
        conexiones_originales = len(self.conexiones_activas)
        self.conexiones_activas = [c for c in self.conexiones_activas if c['mac'] != mac]
        conexiones_eliminadas = conexiones_originales - len(self.conexiones_activas)
        
        if conexiones_eliminadas > 0:
            print(f"🔌 Desconectadas {conexiones_eliminadas} conexiones del dispositivo {mac}")
    
    def generar_alertas(self, mac: str, ip: str, mensaje: str):
        """Genera alertas de seguridad"""
        alerta = {
            'tipo': 'Alerta Seguridad',
            'mac': mac,
            'ip': ip,
            'mensaje': mensaje,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'nivel': 'ALTO'
        }
        
        print(f"🚨 ALERTA: {mensaje} - MAC: {mac}, IP: {ip}")
        
        # Guardar alerta en historial
        self.registrar_historial("Alerta", mac, ip, mensaje)
        
        self.estadisticas['alertas_generadas'] += 1
        
        # Guardar alerta en archivo de log
        self._guardar_alerta_log(alerta)
    
    def registrar_historial(self, tipo: str, mac: str, ip: str, mensaje: str):
        """Registra un evento en el historial"""
        evento = {
            'tipo': tipo,
            'mac': mac,
            'ip': ip,
            'mensaje': mensaje,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.historial_conexiones.append(evento)
        
        # Mantener solo los últimos 1000 eventos en memoria
        if len(self.historial_conexiones) > 1000:
            self.historial_conexiones.pop(0)
    
    def _guardar_alerta_log(self, alerta):
        """Guarda alertas en un archivo de log"""
        try:
            with open("alertas_wifi.log", "a", encoding="utf-8") as f:
                f.write(f"{alerta['timestamp']} - {alerta['nivel']} - {alerta['mensaje']} "
                       f"(MAC: {alerta['mac']}, IP: {alerta['ip']})\n")
        except Exception as e:
            print(f"Error guardando alerta: {e}")
    
    def mostrar_conexiones_activas(self):
        """Muestra las conexiones activas actuales"""
        print("\n" + "="*90)
        print("CONEXIONES ACTIVAS")
        print("="*90)
        
        if not self.conexiones_activas:
            print("No hay conexiones activas")
            return
            
        print(f"{'Usuario':<15} {'MAC':<18} {'IP':<15} {'SSID':<15} {'Tiempo Conexión':<20}")
        print("-"*90)
        
        for conexion in self.conexiones_activas:
            try:
                tiempo_conexion = datetime.now() - datetime.strptime(conexion['timestamp'], "%Y-%m-%d %H:%M:%S")
                horas, resto = divmod(int(tiempo_conexion.total_seconds()), 3600)
                minutos, segundos = divmod(resto, 60)
                tiempo_str = f"{horas:02d}:{minutos:02d}:{segundos:02d}"
            except ValueError:
                tiempo_str = "Error tiempo"
            
            print(f"{conexion['usuario']:<15} {conexion['mac']:<18} {conexion['ip']:<15} "
                  f"{conexion['ssid']:<15} {tiempo_str:<20}")
    
    def mostrar_dispositivos_autorizados(self):
        """Muestra la lista de dispositivos autorizados"""
        print("\n" + "="*70)
        print("DISPOSITIVOS AUTORIZADOS")
        print("="*70)
        
        if not self.limites_usuarios:
            print("No hay dispositivos autorizados")
            return
            
        print(f"{'MAC':<18} {'Usuario':<15} {'Límite Conexiones':<18}")
        print("-"*70)
        
        for dispositivo in self.limites_usuarios:
            print(f"{dispositivo['mac']:<18} {dispositivo['usuario']:<15} {dispositivo['limite']:<18}")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas del sistema"""
        print("\n" + "="*50)
        print("ESTADÍSTICAS DEL SISTEMA")
        print("="*50)
        
        print(f"Total de conexiones: {self.estadisticas['total_conexiones']}")
        print(f"Conexiones rechazadas: {self.estadisticas['conexiones_rechazadas']}")
        print(f"Dispositivos únicos: {len(self.estadisticas['dispositivos_unicos'])}")
        print(f"Alertas generadas: {self.estadisticas['alertas_generadas']}")
        print(f"Conexiones activas: {len(self.conexiones_activas)}")
        print(f"Dispositivos autorizados: {len(self.dispositivos_autorizados)}")
        print(f"Dispositivos bloqueados: {len(self.dispositivos_bloqueados)}")
        
        # Estadísticas por usuario
        print(f"\nConexiones por usuario:")
        conexiones_por_usuario = defaultdict(int)
        for conexion in self.conexiones_activas:
            conexiones_por_usuario[conexion['usuario']] += 1
        
        for usuario, count in conexiones_por_usuario.items():
            print(f"  {usuario}: {count} conexiones")
    
    def limpiar_conexiones_antiguas(self):
        """Limpia conexiones que han excedido el tiempo máximo"""
        ahora = datetime.now()
        conexiones_a_remover = []
        
        for conexion in self.conexiones_activas:
            try:
                tiempo_conexion = ahora - datetime.strptime(conexion['timestamp'], "%Y-%m-%d %H:%M:%S")
                if tiempo_conexion.total_seconds() > self.tiempo_maximo_conexion:
                    conexiones_a_remover.append(conexion)
                    print(f"🔌 Desconectando {conexion['usuario']} por tiempo excedido")
            except ValueError:
                # Si hay error en el formato de fecha, remover la conexión
                conexiones_a_remover.append(conexion)
        
        # Remover conexiones antiguas
        for conexion in conexiones_a_remover:
            if conexion in self.conexiones_activas:
                self.conexiones_activas.remove(conexion)
    
    def iniciar_monitoreo(self):
        """Inicia el monitoreo automático de conexiones"""
        if self.monitoreo_activo:
            print("⚠️ El monitoreo ya está activo")
            return
            
        self.monitoreo_activo = True
        self.hilo_monitoreo = threading.Thread(target=self._monitorear_conexiones)
        self.hilo_monitoreo.daemon = True
        self.hilo_monitoreo.start()
        print("🔍 Monitoreo de conexiones WiFi iniciado")
    
    def detener_monitoreo(self):
        """Detiene el monitoreo automático"""
        if not self.monitoreo_activo:
            print("⚠️ El monitoreo no está activo")
            return
            
        self.monitoreo_activo = False
        if self.hilo_monitoreo and self.hilo_monitoreo.is_alive():
            self.hilo_monitoreo.join(timeout=5)
        print("⏹️ Monitoreo de conexiones WiFi detenido")
    
    def _monitorear_conexiones(self):
        """Hilo de monitoreo continuo"""
        while self.monitoreo_activo:
            try:
                self.limpiar_conexiones_antiguas()
                time.sleep(self.intervalo_verificacion)
            except Exception as e:
                print(f"Error en monitoreo: {e}")
                time.sleep(10)  # Esperar antes de reintentar
    
    def exportar_reportes(self, archivo="reporte_wifi.csv"):
        """Exporta reportes a CSV"""
        try:
            with open(archivo, 'w', newline='', encoding='utf-8') as csvfile:
                campos = ['timestamp', 'usuario', 'mac', 'ip', 'ssid', 'tipo']
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                
                for evento in self.historial_conexiones[-1000:]:  # Últimos 1000 eventos
                    row_data = {
                        'timestamp': evento.get('timestamp', ''),
                        'mac': evento.get('mac', ''),
                        'ip': evento.get('ip', ''),
                        'ssid': evento.get('ssid', ''),
                        'tipo': evento.get('tipo', 'Evento')
                    }
                    
                    # Para eventos de conexión, usar el campo 'usuario'
                    # Para otros eventos, usar 'Desconocido'
                    if 'usuario' in evento:
                        row_data['usuario'] = evento['usuario']
                    else:
                        row_data['usuario'] = 'Desconocido'
                        
                    writer.writerow(row_data)
            
            print(f"✅ Reporte exportado a {archivo}")
        except Exception as e:
            print(f"❌ Error exportando reporte: {e}")
    
    def guardar_configuracion(self):
        """Guarda la configuración en archivo JSON"""
        try:
            datos = {
                'dispositivos_autorizados': self.dispositivos_autorizados,
                'dispositivos_bloqueados': self.dispositivos_bloqueados,
                'limites_usuarios': self.limites_usuarios,
                'usuarios': self.usuarios,
                'configuracion': {
                    'ssid': self.ssid,
                    'limite_global': self.limite_conexiones_global,
                    'tiempo_maximo': self.tiempo_maximo_conexion
                }
            }
            
            with open(self.archivo_config, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False)
            
        except Exception as e:
            print(f"Error guardando configuración: {e}")
    
    def cargar_configuracion(self):
        """Carga la configuración desde archivo JSON"""
        try:
            with open(self.archivo_config, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            self.dispositivos_autorizados = datos.get('dispositivos_autorizados', [])
            self.dispositivos_bloqueados = datos.get('dispositivos_bloqueados', [])
            self.limites_usuarios = datos.get('limites_usuarios', [])
            self.usuarios = datos.get('usuarios', [])
            
            config = datos.get('configuracion', {})
            self.ssid = config.get('ssid', self.ssid)
            self.limite_conexiones_global = config.get('limite_global', self.limite_conexiones_global)
            self.tiempo_maximo_conexion = config.get('tiempo_maximo', self.tiempo_maximo_conexion)
            
            print(f"✅ Configuración cargada: {len(self.dispositivos_autorizados)} dispositivos autorizados")
            
        except FileNotFoundError:
            print("ℹ️ No se encontró archivo de configuración. Se creará uno nuevo.")
        except Exception as e:
            print(f"❌ Error cargando configuración: {e}")

# Función principal para demostrar el sistema
def main():
    control_wifi = ControlAccesosWiFi()
    
    print("📶 SISTEMA DE CONTROL DE ACCESOS WiFi")
    print("="*50)
    
    # Agregar dispositivos de ejemplo
    if not control_wifi.dispositivos_autorizados:
        print("Registrando dispositivos de ejemplo...")
        
        dispositivos_ejemplo = [
            ("aa:bb:cc:dd:ee:01", "Juan Perez", 3),
            ("aa:bb:cc:dd:ee:02", "Maria Garcia", 2),
            ("aa:bb:cc:dd:ee:03", "Carlos Lopez", 1),
            ("aa:bb:cc:dd:ee:04", "Ana Martinez", 4),
            ("aa:bb:cc:dd:ee:05", "Pedro Rodriguez", 2),
        ]
        
        for mac, usuario, limite in dispositivos_ejemplo:
            control_wifi.registrar_dispositivo(mac, usuario, limite)
    
    # Iniciar monitoreo
    control_wifi.iniciar_monitoreo()
    
    # Simular algunas conexiones
    print("\nSimulando conexiones...")
    conexiones_simuladas = [
        ("aa:bb:cc:dd:ee:01", "192.168.1.101"),
        ("aa:bb:cc:dd:ee:02", "192.168.1.102"),
        ("aa:bb:cc:dd:ee:06", "192.168.1.103"),  # No autorizado
        ("aa:bb:cc:dd:ee:01", "192.168.1.104"),  # Mismo usuario, diferente IP
        ("aa:bb:cc:dd:ee:03", "192.168.1.105"),
    ]
    
    for mac, ip in conexiones_simuladas:
        resultado = control_wifi.validar_acceso(mac, ip)
        print(f"Acceso {mac} -> {ip}: {'PERMITIDO' if resultado['acceso_permitido'] else 'DENEGADO'} - {resultado['razon']}")
        time.sleep(1)
    
    while True:
        print("\n" + "="*30)
        print("MENÚ PRINCIPAL")
        print("="*30)
        print("1. Mostrar conexiones activas")
        print("2. Mostrar dispositivos autorizados")
        print("3. Mostrar estadísticas")
        print("4. Registrar nuevo dispositivo")
        print("5. Bloquear dispositivo")
        print("6. Desbloquear dispositivo")
        print("7. Simular conexión")
        print("8. Exportar reportes")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            control_wifi.mostrar_conexiones_activas()
        
        elif opcion == "2":
            control_wifi.mostrar_dispositivos_autorizados()
        
        elif opcion == "3":
            control_wifi.mostrar_estadisticas()
        
        elif opcion == "4":
            mac = input("MAC address: ").strip()
            usuario = input("Usuario: ").strip()
            limite_input = input("Límite de conexiones (Enter para default): ").strip()
            limite = int(limite_input) if limite_input else None
            
            control_wifi.registrar_dispositivo(mac, usuario, limite)
        
        elif opcion == "5":
            mac = input("MAC address a bloquear: ").strip()
            razon = input("Razón del bloqueo: ").strip()
            if not razon:
                razon = "Violación de políticas"
            control_wifi.bloquear_dispositivo(mac, razon)
        
        elif opcion == "6":
            mac = input("MAC address a desbloquear: ").strip()
            control_wifi.desbloquear_dispositivo(mac)
        
        elif opcion == "7":
            mac = input("MAC address: ").strip()
            ip = input("IP address: ").strip()
            resultado = control_wifi.validar_acceso(mac, ip)
            print(f"Resultado: {'PERMITIDO' if resultado['acceso_permitido'] else 'DENEGADO'} - {resultado['razon']}")
        
        elif opcion == "8":
            control_wifi.exportar_reportes()
        
        elif opcion == "9":
            control_wifi.detener_monitoreo()
            print("¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()