import json
import csv
import ipaddress
import subprocess
import platform
import threading
import time
from datetime import datetime, timedelta
from collections import defaultdict
import socket
import requests
from typing import List, Dict, Any

class SistemaInventarioRed:
    def __init__(self, archivo_inventario="inventario_red.json"):
        # Vectores para datos básicos
        self.equipos = []  # Nombres de equipos
        self.ubicaciones = []  # Ubicaciones físicas
        
        # Matrices para información detallada
        self.detalles_equipos = []  # [nombre, ip, tipo, ubicacion, estado, ultima_verificacion]
        self.historial_estados = []  # Historial de cambios de estado
        
        # Configuración
        self.archivo_inventario = archivo_inventario
        self.tipos_equipo = ["Router", "Switch", "Firewall", "Servidor", "Access Point", "PC", "Impresora", "Otro"]
        self.estados_posibles = ["En línea", "Fuera de línea", "Alerta", "Mantenimiento"]
        
        # Umbrales para alertas
        self.umbral_latencia = 100  # ms
        self.tiempo_verificacion = 300  # 5 minutos
        
        # Cargar inventario existente
        self.cargar_inventario()
    
    def validar_ip(self, ip: str) -> bool:
        """Valida que la IP tenga formato correcto"""
        try:
            ipaddress.IPv4Address(ip)
            return True
        except ipaddress.AddressValueError:
            return False
    
    def generar_ip_aleatoria(self, red="192.168.1.0/24") -> str:
        """Genera una dirección IP aleatoria dentro de una red"""
        try:
            network = ipaddress.IPv4Network(red)
            return str(random.choice(list(network.hosts())))
        except:
            return f"192.168.1.{random.randint(2, 254)}"
    
    def escanear_equipo(self, ip: str, timeout=2) -> Dict[str, Any]:
        """
        Escanea un equipo para verificar su estado y obtener información
        
        Args:
            ip (str): Dirección IP del equipo
            timeout (int): Tiempo máximo de espera
        
        Returns:
            Dict: Información del escaneo
        """
        resultado = {
            'ip': ip,
            'estado': 'Fuera de línea',
            'latencia': None,
            'puertos_abiertos': [],
            'hostname': None,
            'timestamp': datetime.now()
        }
        
        try:
            # Método 1: Usar ping del sistema operativo
            latencia = self._ping_sistema_operativo(ip, timeout)
            if latencia is not None:
                resultado['estado'] = 'En línea'
                resultado['latencia'] = latencia
            
            # Si el ping falla, intentar con conexión TCP a puertos comunes
            if resultado['estado'] == 'Fuera de línea':
                if self._verificar_conectividad_tcp(ip, timeout):
                    resultado['estado'] = 'En línea'
                    resultado['latencia'] = 1  # Valor simbólico para TCP exitoso
            
            # Intentar obtener hostname
            try:
                hostname = socket.gethostbyaddr(ip)[0]
                resultado['hostname'] = hostname
            except:
                resultado['hostname'] = f"desconocido-{ip.replace('.', '-')}"
            
            # Escanear puertos comunes
            puertos_comunes = [22, 23, 80, 443, 3389, 21, 25, 53]
            for puerto in puertos_comunes:
                if self.verificar_puerto(ip, puerto, timeout=1):
                    resultado['puertos_abiertos'].append(puerto)
            
        except Exception as e:
            resultado['error'] = str(e)
        
        return resultado
    
    def _ping_sistema_operativo(self, ip: str, timeout: int) -> float:
        """
        Realiza ping usando el comando del sistema operativo
        
        Returns:
            float: Latencia en milisegundos o None si falla
        """
        try:
            if platform.system().lower() == "windows":
                comando = ["ping", "-n", "1", "-w", str(timeout * 1000), ip]
                output = subprocess.run(comando, capture_output=True, text=True, timeout=timeout + 1)
                
                if output.returncode == 0 and "TTL=" in output.stdout:
                    # Extraer tiempo del output de Windows
                    for line in output.stdout.split('\n'):
                        if 'tiempo=' in line or 'time=' in line:
                            if 'ms' in line:
                                tiempo_str = line.split('tiempo=')[-1].split('ms')[0]
                                return float(tiempo_str)
            else:
                # Linux/Mac
                comando = ["ping", "-c", "1", "-W", str(timeout), ip]
                output = subprocess.run(comando, capture_output=True, text=True, timeout=timeout + 1)
                
                if output.returncode == 0:
                    # Extraer tiempo del output de Linux
                    for line in output.stdout.split('\n'):
                        if 'time=' in line:
                            tiempo_str = line.split('time=')[-1].split(' ms')[0]
                            return float(tiempo_str)
            
        except subprocess.TimeoutExpired:
            pass
        except Exception as e:
            print(f"Error en ping a {ip}: {e}")
        
        return None
    
    def _verificar_conectividad_tcp(self, ip: str, timeout: int) -> bool:
        """
        Verifica conectividad intentando conexión TCP a puertos comunes
        """
        puertos_prueba = [80, 443, 22, 23, 21]  # HTTP, HTTPS, SSH, Telnet, FTP
        
        for puerto in puertos_prueba:
            if self.verificar_puerto(ip, puerto, timeout):
                return True
        
        return False
    
    def verificar_puerto(self, ip: str, puerto: int, timeout=1) -> bool:
        """Verifica si un puerto está abierto"""
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(timeout)
                resultado = sock.connect_ex((ip, puerto))
                return resultado == 0
        except:
            return False
    
    def registrar_equipo(self, nombre: str, ip: str, tipo: str, ubicacion: str, 
                        descripcion: str = "", usuario: str = "Sistema") -> bool:
        """
        Registra un nuevo equipo en el inventario
        
        Args:
            nombre (str): Nombre del equipo
            ip (str): Dirección IP
            tipo (str): Tipo de equipo
            ubicacion (str): Ubicación física
            descripcion (str): Descripción adicional
            usuario (str): Usuario que registra el equipo
        
        Returns:
            bool: True si se registró exitosamente
        """
        # Validaciones
        if not self.validar_ip(ip):
            print(f"Error: IP {ip} no válida")
            return False
        
        if tipo not in self.tipos_equipo:
            print(f"Error: Tipo {tipo} no válido. Tipos permitidos: {', '.join(self.tipos_equipo)}")
            return False
        
        # Verificar si el equipo ya existe
        for equipo in self.detalles_equipos:
            if equipo['nombre'] == nombre or equipo['ip'] == ip:
                print(f"Error: El equipo {nombre} o IP {ip} ya existe")
                return False
        
        # Escanear equipo para obtener estado inicial
        escaneo = self.escanear_equipo(ip)
        
        # Crear registro del equipo
        equipo = {
            'nombre': nombre,
            'ip': ip,
            'tipo': tipo,
            'ubicacion': ubicacion,
            'descripcion': descripcion,
            'estado': escaneo['estado'],
            'hostname': escaneo['hostname'],
            'latencia': escaneo['latencia'],
            'puertos_abiertos': escaneo['puertos_abiertos'],
            'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'usuario_registro': usuario,
            'ultima_verificacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'estadisticas': {
                'tiempo_activo': 0,
                'tiempo_inactivo': 0,
                'cambios_estado': 0
            }
        }
        
        # Agregar a los vectores y matrices
        self.equipos.append(nombre)
        if ubicacion not in self.ubicaciones:
            self.ubicaciones.append(ubicacion)
        
        self.detalles_equipos.append(equipo)
        
        # Registrar en historial
        self.registrar_historial(nombre, "Registro", f"Equipo registrado por {usuario}", "info")
        
        print(f"✅ Equipo {nombre} ({ip}) registrado exitosamente. Estado: {escaneo['estado']}")
        
        # Guardar inventario
        self.guardar_inventario()
        
        return True
    
    def verificar_estado_equipos(self) -> None:
        """Verifica el estado de todos los equipos en el inventario"""
        print("\n🔍 Verificando estado de equipos...")
        
        for equipo in self.detalles_equipos:
            nombre = equipo['nombre']
            ip = equipo['ip']
            estado_anterior = equipo['estado']
            
            # Escanear equipo
            escaneo = self.escanear_equipo(ip)
            
            # Actualizar información
            equipo['estado'] = escaneo['estado']
            equipo['latencia'] = escaneo['latencia']
            equipo['hostname'] = escaneo['hostname']
            equipo['puertos_abiertos'] = escaneo['puertos_abiertos']
            equipo['ultima_verificacion'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            # Actualizar estadísticas
            if estado_anterior != escaneo['estado']:
                equipo['estadisticas']['cambios_estado'] += 1
                self.registrar_historial(nombre, "Cambio Estado", 
                                       f"Estado cambió de {estado_anterior} a {escaneo['estado']}", 
                                       "alerta" if escaneo['estado'] == "Fuera de línea" else "info")
            
            # Generar alertas si es necesario
            self.generar_alertas(equipo, escaneo)
            
            estado_emoji = "🟢" if escaneo['estado'] == "En línea" else "🔴"
            latencia_str = f"{escaneo['latencia']}ms" if escaneo['latencia'] else "N/A"
            print(f"  {estado_emoji} {nombre} ({ip}): {escaneo['estado']} - Latencia: {latencia_str}")
        
        print("✅ Verificación completada")
        self.guardar_inventario()
    
    def generar_alertas(self, equipo: Dict, escaneo: Dict) -> None:
        """Genera alertas basadas en el estado del equipo"""
        alertas = []
        
        # Alertas por estado
        if escaneo['estado'] == "Fuera de línea":
            alertas.append(f"Equipo {equipo['nombre']} ({equipo['ip']}) está fuera de línea")
        
        # Alertas por latencia alta
        if escaneo['latencia'] and escaneo['latencia'] > self.umbral_latencia:
            alertas.append(f"Alta latencia en {equipo['nombre']}: {escaneo['latencia']}ms")
        
        # Alertas por puertos inesperados
        if equipo['tipo'] == "Router" and 80 in escaneo['puertos_abiertos']:
            alertas.append(f"Puerto HTTP abierto en router {equipo['nombre']} - Posible riesgo de seguridad")
        
        if equipo['tipo'] == "Servidor" and 22 in escaneo['puertos_abiertos'] and "web" in equipo['descripcion'].lower():
            alertas.append(f"Puerto SSH abierto en servidor web {equipo['nombre']} - Verificar seguridad")
        
        # Alertas por cambios en puertos
        puertos_anteriores = set(equipo.get('puertos_abiertos_anteriores', []))
        puertos_actuales = set(escaneo['puertos_abiertos'])
        
        nuevos_puertos = puertos_actuales - puertos_anteriores
        if nuevos_puertos:
            alertas.append(f"Puertos nuevos abiertos en {equipo['nombre']}: {list(nuevos_puertos)}")
        
        # Guardar puertos actuales para la próxima verificación
        equipo['puertos_abiertos_anteriores'] = escaneo['puertos_abiertos']
        
        # Mostrar y guardar alertas
        for alerta in alertas:
            print(f"🚨 ALERTA: {alerta}")
            self.registrar_historial(equipo['nombre'], "Alerta", alerta, "error")
    
    def registrar_historial(self, equipo: str, tipo: str, mensaje: str, nivel: str) -> None:
        """Registra un evento en el historial"""
        evento = {
            'equipo': equipo,
            'tipo': tipo,
            'mensaje': mensaje,
            'nivel': nivel,
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.historial_estados.append(evento)
    
    def mostrar_inventario(self, filtro_tipo: str = None, filtro_ubicacion: str = None) -> None:
        """Muestra el inventario completo o filtrado"""
        print("\n" + "="*120)
        print("INVENTARIO DE EQUIPOS DE RED")
        print("="*120)
        
        equipos_filtrados = self.detalles_equipos
        
        if filtro_tipo:
            equipos_filtrados = [e for e in equipos_filtrados if e['tipo'] == filtro_tipo]
        
        if filtro_ubicacion:
            equipos_filtrados = [e for e in equipos_filtrados if e['ubicacion'] == filtro_ubicacion]
        
        if not equipos_filtrados:
            print("No se encontraron equipos con los filtros aplicados")
            return
        
        print(f"{'Nombre':<20} {'IP':<15} {'Tipo':<12} {'Ubicación':<15} {'Estado':<12} {'Latencia':<10} {'Última Verificación':<20}")
        print("-"*120)
        
        for equipo in equipos_filtrados:
            estado_emoji = "🟢" if equipo['estado'] == "En línea" else "🔴"
            latencia_str = f"{equipo['latencia']}ms" if equipo['latencia'] else "N/A"
            
            print(f"{equipo['nombre']:<20} {equipo['ip']:<15} {equipo['tipo']:<12} "
                  f"{equipo['ubicacion']:<15} {estado_emoji} {equipo['estado']:<10} "
                  f"{latencia_str:<10} {equipo['ultima_verificacion']:<20}")
    
    def mostrar_estadisticas(self) -> None:
        """Muestra estadísticas del inventario"""
        print("\n" + "="*60)
        print("ESTADÍSTICAS DEL INVENTARIO")
        print("="*60)
        
        total_equipos = len(self.detalles_equipos)
        equipos_online = sum(1 for e in self.detalles_equipos if e['estado'] == "En línea")
        equipos_offline = total_equipos - equipos_online
        
        print(f"Total de equipos: {total_equipos}")
        print(f"Equipos en línea: {equipos_online} ({equipos_online/total_equipos*100:.1f}%)")
        print(f"Equipos fuera de línea: {equipos_offline} ({equipos_offline/total_equipos*100:.1f}%)")
        
        # Estadísticas por tipo
        print(f"\nEstadísticas por tipo:")
        tipos_contador = defaultdict(int)
        for equipo in self.detalles_equipos:
            tipos_contador[equipo['tipo']] += 1
        
        for tipo, cantidad in sorted(tipos_contador.items()):
            print(f"  {tipo}: {cantidad} equipos")
        
        # Equipos con problemas
        equipos_problema = [e for e in self.detalles_equipos 
                          if e['estado'] == "Fuera de línea" or 
                          (e['latencia'] and e['latencia'] > self.umbral_latencia)]
        
        if equipos_problema:
            print(f"\n⚠️  Equipos con problemas ({len(equipos_problema)}):")
            for equipo in equipos_problema:
                problema = "Fuera de línea" if equipo['estado'] == "Fuera de línea" else f"Alta latencia ({equipo['latencia']}ms)"
                print(f"  • {equipo['nombre']} ({equipo['ip']}): {problema}")
    
    def mostrar_historial(self, equipo: str = None, limite: int = 10) -> None:
        """Muestra el historial de eventos"""
        print(f"\n{'='*80}")
        print("HISTORIAL DE EVENTOS")
        print("="*80)
        
        eventos_filtrados = self.historial_estados
        
        if equipo:
            eventos_filtrados = [e for e in eventos_filtrados if e['equipo'] == equipo]
        
        eventos_filtrados = eventos_filtrados[-limite:]
        
        if not eventos_filtrados:
            print("No hay eventos para mostrar")
            return
        
        for evento in eventos_filtrados:
            nivel_emoji = {
                'info': 'ℹ️',
                'alerta': '⚠️', 
                'error': '🚨'
            }.get(evento['nivel'], '📝')
            
            print(f"{evento['timestamp']} {nivel_emoji} [{evento['equipo']}] {evento['tipo']}: {evento['mensaje']}")
    
    def buscar_equipo(self, criterio: str, valor: str) -> List[Dict]:
        """Busca equipos por diferentes criterios"""
        resultados = []
        
        if criterio == "ip":
            resultados = [e for e in self.detalles_equipos if e['ip'] == valor]
        elif criterio == "nombre":
            resultados = [e for e in self.detalles_equipos if valor.lower() in e['nombre'].lower()]
        elif criterio == "tipo":
            resultados = [e for e in self.detalles_equipos if e['tipo'] == valor]
        elif criterio == "ubicacion":
            resultados = [e for e in self.detalles_equipos if valor.lower() in e['ubicacion'].lower()]
        
        return resultados
    
    def exportar_inventario(self, archivo: str = "inventario_red.csv") -> None:
        """Exporta el inventario a un archivo CSV"""
        try:
            with open(archivo, 'w', newline='', encoding='utf-8') as csvfile:
                campos = ['nombre', 'ip', 'tipo', 'ubicacion', 'descripcion', 'estado', 
                         'hostname', 'latencia', 'puertos_abiertos', 'fecha_registro']
                
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                
                for equipo in self.detalles_equipos:
                    # Filtrar solo los campos que nos interesan
                    fila = {campo: equipo.get(campo, '') for campo in campos}
                    fila['puertos_abiertos'] = ','.join(map(str, fila['puertos_abiertos']))
                    writer.writerow(fila)
            
            print(f"✅ Inventario exportado a {archivo}")
        except Exception as e:
            print(f"❌ Error exportando inventario: {e}")
    
    def guardar_inventario(self) -> None:
        """Guarda el inventario en un archivo JSON"""
        try:
            datos = {
                'equipos': self.detalles_equipos,
                'historial': self.historial_estados[-1000:],  # Guardar solo los últimos 1000 eventos
                'metadata': {
                    'ultima_actualizacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'total_equipos': len(self.detalles_equipos)
                }
            }
            
            with open(self.archivo_inventario, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False, default=str)
            
        except Exception as e:
            print(f"Error guardando inventario: {e}")
    
    def cargar_inventario(self) -> None:
        """Carga el inventario desde un archivo JSON"""
        try:
            with open(self.archivo_inventario, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            self.detalles_equipos = datos.get('equipos', [])
            self.historial_estados = datos.get('historial', [])
            
            # Reconstruir vectores básicos
            self.equipos = [e['nombre'] for e in self.detalles_equipos]
            self.ubicaciones = list(set(e['ubicacion'] for e in self.detalles_equipos))
            
            print(f"✅ Inventario cargado: {len(self.detalles_equipos)} equipos")
            
        except FileNotFoundError:
            print("ℹ️  No se encontró archivo de inventario existente. Se creará uno nuevo.")
        except Exception as e:
            print(f"❌ Error cargando inventario: {e}")
    
    def monitoreo_continuo(self, intervalo: int = 300) -> None:
        """Inicia el monitoreo continuo de equipos"""
        print(f"🚀 Iniciando monitoreo continuo (intervalo: {intervalo} segundos)")
        print("Presiona Ctrl+C para detener el monitoreo")
        
        try:
            while True:
                self.verificar_estado_equipos()
                time.sleep(intervalo)
        except KeyboardInterrupt:
            print("\n⏹️  Monitoreo detenido")

# Función principal para demostrar el sistema
def main():
    inventario = SistemaInventarioRed()
    
    print("🌐 SISTEMA DE INVENTARIO DE EQUIPOS DE RED")
    print("="*50)
    print("Versión sin dependencia de ping3 - Usando métodos nativos")
    print("="*50)
    
    # Agregar equipos de ejemplo si el inventario está vacío
    if not inventario.detalles_equipos:
        print("Agregando equipos de ejemplo...")
        
        equipos_ejemplo = [
            ("Router Principal", "192.168.1.1", "Router", "Sala de Servidores", "Router Cisco 2900"),
            ("Switch Piso 1", "192.168.1.2", "Switch", "Piso 1", "Switch HP 24 puertos"),
            ("Servidor Web", "192.168.1.10", "Servidor", "Sala de Servidores", "Servidor Dell R740"),
            ("Firewall", "192.168.1.254", "Firewall", "Sala de Servidores", "Fortinet 60F"),
            ("AP Recepción", "192.168.1.20", "Access Point", "Recepción", "Ubiquiti UAP-AC-PRO"),
            ("PC Admin", "192.168.1.100", "PC", "Oficina Admin", "Computadora administrativa"),
            ("Impresora Color", "192.168.1.50", "Impresora", "Oficina Admin", "HP Color LaserJet"),
        ]
        
        for nombre, ip, tipo, ubicacion, descripcion in equipos_ejemplo:
            inventario.registrar_equipo(nombre, ip, tipo, ubicacion, descripcion)
    
    while True:
        print("\nOpciones:")
        print("1. Mostrar inventario completo")
        print("2. Verificar estado de equipos")
        print("3. Registrar nuevo equipo")
        print("4. Mostrar estadísticas")
        print("5. Mostrar historial")
        print("6. Buscar equipo")
        print("7. Exportar inventario")
        print("8. Monitoreo continuo")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            inventario.mostrar_inventario()
        
        elif opcion == "2":
            inventario.verificar_estado_equipos()
        
        elif opcion == "3":
            nombre = input("Nombre del equipo: ")
            ip = input("Dirección IP: ")
            
            print("Tipos disponibles:", ", ".join(inventario.tipos_equipo))
            tipo = input("Tipo de equipo: ")
            
            ubicacion = input("Ubicación: ")
            descripcion = input("Descripción (opcional): ")
            
            inventario.registrar_equipo(nombre, ip, tipo, ubicacion, descripcion)
        
        elif opcion == "4":
            inventario.mostrar_estadisticas()
        
        elif opcion == "5":
            equipo = input("Equipo específico (dejar vacío para todos): ") or None
            inventario.mostrar_historial(equipo)
        
        elif opcion == "6":
            print("Criterios: ip, nombre, tipo, ubicacion")
            criterio = input("Criterio de búsqueda: ")
            valor = input("Valor a buscar: ")
            
            resultados = inventario.buscar_equipo(criterio, valor)
            if resultados:
                print(f"\nSe encontraron {len(resultados)} equipos:")
                for equipo in resultados:
                    print(f"  • {equipo['nombre']} ({equipo['ip']}) - {equipo['tipo']} - {equipo['ubicacion']}")
            else:
                print("No se encontraron equipos")
        
        elif opcion == "7":
            inventario.exportar_inventario()
        
        elif opcion == "8":
            intervalo = int(input("Intervalo de verificación en segundos (default 300): ") or "300")
            inventario.monitoreo_continuo(intervalo)
        
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    import random  # Importar aquí para el ejemplo
    main()