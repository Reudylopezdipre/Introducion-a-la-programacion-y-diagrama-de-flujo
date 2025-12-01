import json
import csv
import random
import socket
from datetime import datetime, timedelta
from collections import defaultdict
import ipaddress

class SimuladorEscaneoVulnerabilidades:
    def __init__(self, archivo_datos="vulnerabilidades.json"):
        # Vectores para almacenamiento básico
        self.hosts = []  # Lista de hosts a escanear
        self.servicios_comunes = []  # Servicios conocidos
        
        # Matrices para datos detallados
        self.servicios_detectados = []  # [host, puerto, servicio, version, estado]
        self.intentos_escaneo = []  # Registro de todos los intentos de escaneo
        self.vulnerabilidades = []  # [host, servicio, vulnerabilidad, severidad, CVE]
        
        # Configuración
        self.archivo_datos = archivo_datos
        self.puertos_comunes = [21, 22, 23, 25, 53, 80, 110, 443, 993, 995, 3389, 5900]
        self.servicios = {
            21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP", 53: "DNS",
            80: "HTTP", 110: "POP3", 443: "HTTPS", 993: "IMAPS", 995: "POP3S",
            3389: "RDP", 5900: "VNC", 1433: "MSSQL", 3306: "MySQL", 5432: "PostgreSQL"
        }
        
        # Base de datos de vulnerabilidades simuladas
        self.base_vulnerabilidades = self._inicializar_base_vulnerabilidades()
        
        # Estadísticas
        self.estadisticas = {
            'total_hosts': 0,
            'hosts_escaneados': 0,
            'vulnerabilidades_encontradas': 0,
            'servicios_detectados': 0
        }
        
        # Cargar datos existentes
        self.cargar_datos()
    
    def _inicializar_base_vulnerabilidades(self):
        """Inicializa la base de datos de vulnerabilidades conocidas"""
        return {
            "FTP": [
                {"nombre": "FTP Anonymous Access", "severidad": "Alta", "CVE": "CVE-1999-0497", "descripcion": "Acceso anónimo habilitado"},
                {"nombre": "FTP Bounce Attack", "severidad": "Media", "CVE": "CVE-1999-0017", "descripcion": "Servidor vulnerable a ataques de rebote"}
            ],
            "SSH": [
                {"nombre": "SSH Weak Algorithms", "severidad": "Media", "CVE": "CVE-2008-5161", "descripcion": "Algoritmos de cifrado débiles soportados"},
                {"nombre": "SSH Version Disclosure", "severidad": "Baja", "CVE": "CVE-2001-0144", "descripcion": "Divulgación de versión del servicio"}
            ],
            "HTTP": [
                {"nombre": "SQL Injection", "severidad": "Alta", "CVE": "CVE-2021-1234", "descripcion": "Vulnerabilidad de inyección SQL detectada"},
                {"nombre": "XSS Cross-site Scripting", "severidad": "Media", "CVE": "CVE-2021-5678", "descripcion": "Vulnerabilidad XSS en parámetros URL"},
                {"nombre": "Outdated Apache Version", "severidad": "Alta", "CVE": "CVE-2021-41773", "descripcion": "Versión de Apache desactualizada"}
            ],
            "HTTPS": [
                {"nombre": "SSL/TLS Weak Cipher", "severidad": "Media", "CVE": "CVE-2016-2183", "descripcion": "Cifrado SSL/TLS débil soportado"},
                {"nombre": "Heartbleed", "severidad": "Alta", "CVE": "CVE-2014-0160", "descripcion": "Vulnerabilidad Heartbleed en OpenSSL"}
            ],
            "SMB": [
                {"nombre": "EternalBlue", "severidad": "Crítica", "CVE": "CVE-2017-0144", "descripcion": "Vulnerabilidad crítica en SMBv1"},
                {"nombre": "SMB Signing Disabled", "severidad": "Media", "CVE": "CVE-2000-1200", "descripcion": "Firma SMB deshabilitada"}
            ],
            "RDP": [
                {"nombre": "BlueKeep", "severidad": "Crítica", "CVE": "CVE-2019-0708", "descripcion": "Vulnerabilidad crítica RDP"},
                {"nombre": "RDP Session Hijacking", "severidad": "Alta", "CVE": "CVE-2012-0152", "descripcion": "Posible secuestro de sesión RDP"}
            ],
            "MySQL": [
                {"nombre": "MySQL Weak Authentication", "severidad": "Alta", "CVE": "CVE-2012-2122", "descripcion": "Debilidad en autenticación"},
                {"nombre": "MySQL Buffer Overflow", "severidad": "Alta", "CVE": "CVE-2016-6662", "descripcion": "Desbordamiento de búfer"}
            ]
        }
    
    def validar_host(self, host):
        """Valida si el host tiene formato correcto (IP o hostname)"""
        try:
            # Intentar como IP
            ipaddress.ip_address(host)
            return True
        except ValueError:
            try:
                # Intentar como hostname
                socket.gethostbyname(host)
                return True
            except socket.gaierror:
                return False
    
    def generar_ip_aleatoria(self):
        """Genera una dirección IP aleatoria"""
        return f"192.168.{random.randint(1, 255)}.{random.randint(1, 254)}"
    
    def registrar_host(self, host, descripcion="", tipo="Servidor"):
        """
        Registra un nuevo host para escanear
        
        Args:
            host (str): Dirección IP o hostname
            descripcion (str): Descripción del host
            tipo (str): Tipo de dispositivo
        
        Returns:
            bool: True si se registró exitosamente
        """
        if not self.validar_host(host):
            print(f"Error: Host {host} no válido")
            return False
        
        if host in self.hosts:
            print(f"Error: Host {host} ya está registrado")
            return False
        
        # Registrar host
        host_info = {
            'direccion': host,
            'descripcion': descripcion,
            'tipo': tipo,
            'fecha_registro': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            'ultimo_escaneo': None,
            'estado': 'No escaneado'
        }
        
        self.hosts.append(host_info)
        self.estadisticas['total_hosts'] += 1
        
        print(f"✅ Host {host} registrado exitosamente")
        self.guardar_datos()
        return True
    
    def escanear_puerto(self, host, puerto, timeout=1):
        """
        Simula el escaneo de un puerto específico
        
        Returns:
            dict: Resultado del escaneo del puerto
        """
        # Simular comportamiento realista
        probabilidad_abierto = random.random()
        
        resultado = {
            'host': host,
            'puerto': puerto,
            'estado': 'cerrado',
            'servicio': 'desconocido',
            'version': '',
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        # Determinar si el puerto está abierto (simulación)
        if probabilidad_abierto > 0.3:  # 70% de probabilidad de estar cerrado
            resultado['estado'] = 'cerrado'
            return resultado
        
        # Puerto abierto - detectar servicio
        servicio = self.servicios.get(puerto, "Desconocido")
        resultado['estado'] = 'abierto'
        resultado['servicio'] = servicio
        
        # Simular versión del servicio
        versiones = {
            "FTP": ["vsFTPd 2.3.4", "ProFTPD 1.3.5", "FileZilla 0.9.60"],
            "SSH": ["OpenSSH 7.4", "OpenSSH 8.2", "Dropbear SSH 2020.81"],
            "HTTP": ["Apache 2.4.41", "nginx 1.18.0", "IIS 10.0"],
            "HTTPS": ["Apache 2.4.46", "nginx 1.19.6", "IIS 10.0"],
            "RDP": ["Microsoft Terminal Services", "xrdp 0.9.13"],
            "MySQL": ["MySQL 5.7.32", "MySQL 8.0.22", "MariaDB 10.5.8"]
        }
        
        if servicio in versiones:
            resultado['version'] = random.choice(versiones[servicio])
        
        return resultado
    
    def escanear_host(self, host, puertos=None):
        """
        Realiza un escaneo completo de un host
        
        Args:
            host (str): Host a escanear
            puertos (list): Lista de puertos a escanear (None para puertos comunes)
        """
        if puertos is None:
            puertos = self.puertos_comunes
        
        print(f"\n🔍 Escaneando host: {host}")
        print(f"Puertos a escanear: {len(puertos)}")
        
        servicios_encontrados = []
        
        for puerto in puertos:
            resultado = self.escanear_puerto(host, puerto)
            
            # Registrar intento de escaneo
            self.intentos_escaneo.append(resultado)
            
            if resultado['estado'] == 'abierto':
                servicios_encontrados.append(resultado)
                print(f"  ✅ Puerto {puerto}/{resultado['servicio']} - ABIERTO - {resultado['version']}")
                
                # Registrar servicio detectado
                servicio_info = {
                    'host': host,
                    'puerto': puerto,
                    'servicio': resultado['servicio'],
                    'version': resultado['version'],
                    'estado': 'abierto',
                    'timestamp': resultado['timestamp']
                }
                self.servicios_detectados.append(servicio_info)
                
                # Analizar vulnerabilidades para este servicio
                self.analizar_vulnerabilidades(host, resultado['servicio'], resultado['version'])
            else:
                print(f"  ❌ Puerto {puerto} - CERRADO")
        
        # Actualizar información del host
        for host_info in self.hosts:
            if host_info['direccion'] == host:
                host_info['ultimo_escaneo'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                host_info['estado'] = 'Escaneado'
                host_info['servicios_encontrados'] = len(servicios_encontrados)
                break
        
        self.estadisticas['hosts_escaneados'] += 1
        self.estadisticas['servicios_detectados'] += len(servicios_encontrados)
        
        print(f"✅ Escaneo completado. Servicios encontrados: {len(servicios_encontrados)}")
        
        # Guardar datos
        self.guardar_datos()
        
        return servicios_encontrados
    
    def analizar_vulnerabilidades(self, host, servicio, version):
        """
        Analiza vulnerabilidades para un servicio específico
        
        Args:
            host (str): Host donde se encontró el servicio
            servicio (str): Nombre del servicio
            version (str): Versión del servicio
        """
        # Simular probabilidad de encontrar vulnerabilidades
        probabilidad_vulnerabilidad = random.random()
        
        if servicio not in self.base_vulnerabilidades or probabilidad_vulnerabilidad > 0.6:
            return  # No se encontraron vulnerabilidades
        
        vulnerabilidades_posibles = self.base_vulnerabilidades[servicio]
        
        # Seleccionar vulnerabilidades aleatorias (1-3)
        num_vulnerabilidades = random.randint(1, min(3, len(vulnerabilidades_posibles)))
        vulnerabilidades_encontradas = random.sample(vulnerabilidades_posibles, num_vulnerabilidades)
        
        for vuln in vulnerabilidades_encontradas:
            vulnerabilidad_info = {
                'host': host,
                'servicio': servicio,
                'version': version,
                'vulnerabilidad': vuln['nombre'],
                'severidad': vuln['severidad'],
                'CVE': vuln['CVE'],
                'descripcion': vuln['descripcion'],
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'estado': 'No parcheado'
            }
            
            self.vulnerabilidades.append(vulnerabilidad_info)
            self.estadisticas['vulnerabilidades_encontradas'] += 1
            
            # Mostrar alerta según severidad
            emoji_severidad = {
                'Crítica': '💀',
                'Alta': '🔴',
                'Media': '🟡',
                'Baja': '🔵'
            }
            
            emoji = emoji_severidad.get(vuln['severidad'], '⚪')
            print(f"    {emoji} VULNERABILIDAD {vuln['severidad']}: {vuln['nombre']} ({vuln['CVE']})")
    
    def escanear_red_completa(self, hosts=None):
        """
        Realiza escaneo de múltiples hosts
        
        Args:
            hosts (list): Lista de hosts a escanear (None para todos los registrados)
        """
        if hosts is None:
            hosts = [host['direccion'] for host in self.hosts]
        
        print(f"\n🎯 Iniciando escaneo completo de {len(hosts)} hosts...")
        
        for host in hosts:
            self.escanear_host(host)
            # Pequeña pausa entre escaneos para simular comportamiento real
            # time.sleep(0.5)
    
    def mostrar_reporte_vulnerabilidades(self, filtro_severidad=None, filtro_host=None):
        """
        Muestra un reporte detallado de vulnerabilidades encontradas
        
        Args:
            filtro_severidad (str): Filtrar por severidad (Crítica, Alta, Media, Baja)
            filtro_host (str): Filtrar por host específico
        """
        print("\n" + "="*120)
        print("REPORTE DE VULNERABILIDADES")
        print("="*120)
        
        vulnerabilidades_filtradas = self.vulnerabilidades
        
        if filtro_severidad:
            vulnerabilidades_filtradas = [v for v in vulnerabilidades_filtradas if v['severidad'] == filtro_severidad]
        
        if filtro_host:
            vulnerabilidades_filtradas = [v for v in vulnerabilidades_filtradas if v['host'] == filtro_host]
        
        if not vulnerabilidades_filtradas:
            print("No se encontraron vulnerabilidades con los filtros aplicados")
            return
        
        # Agrupar por host
        vulnerabilidades_por_host = defaultdict(list)
        for vuln in vulnerabilidades_filtradas:
            vulnerabilidades_por_host[vuln['host']].append(vuln)
        
        for host, vulns in vulnerabilidades_por_host.items():
            print(f"\n🏠 HOST: {host}")
            print("-" * 80)
            
            for vuln in vulns:
                emoji_severidad = {
                    'Crítica': '💀',
                    'Alta': '🔴',
                    'Media': '🟡',
                    'Baja': '🔵'
                }
                emoji = emoji_severidad.get(vuln['severidad'], '⚪')
                
                print(f"  {emoji} [{vuln['severidad']}] {vuln['servicio']} - {vuln['vulnerabilidad']}")
                print(f"     CVE: {vuln['CVE']}")
                print(f"     Descripción: {vuln['descripcion']}")
                print(f"     Versión: {vuln['version']}")
                print(f"     Fecha: {vuln['timestamp']}")
                print()
    
    def mostrar_reporte_servicios(self, filtro_host=None):
        """
        Muestra un reporte de servicios detectados
        """
        print("\n" + "="*80)
        print("REPORTE DE SERVICIOS DETECTADOS")
        print("="*80)
        
        servicios_filtrados = self.servicios_detectados
        
        if filtro_host:
            servicios_filtrados = [s for s in servicios_filtrados if s['host'] == filtro_host]
        
        if not servicios_filtrados:
            print("No se encontraron servicios con los filtros aplicados")
            return
        
        # Agrupar por host
        servicios_por_host = defaultdict(list)
        for servicio in servicios_filtrados:
            servicios_por_host[servicio['host']].append(servicio)
        
        for host, servicios in servicios_por_host.items():
            print(f"\n🏠 HOST: {host}")
            print(f"{'Puerto':<8} {'Servicio':<12} {'Versión':<20} {'Estado':<10}")
            print("-" * 60)
            
            for servicio in servicios:
                print(f"{servicio['puerto']:<8} {servicio['servicio']:<12} {servicio['version']:<20} {servicio['estado']:<10}")
    
    def mostrar_estadisticas_completas(self):
        """
        Muestra estadísticas completas del escaneo
        """
        print("\n" + "="*60)
        print("ESTADÍSTICAS COMPLETAS")
        print("="*60)
        
        print(f"Total de hosts registrados: {self.estadisticas['total_hosts']}")
        print(f"Hosts escaneados: {self.estadisticas['hosts_escaneados']}")
        print(f"Servicios detectados: {self.estadisticas['servicios_detectados']}")
        print(f"Vulnerabilidades encontradas: {self.estadisticas['vulnerabilidades_encontradas']}")
        
        # Estadísticas por severidad
        print(f"\n📊 VULNERABILIDADES POR SEVERIDAD:")
        severidades = defaultdict(int)
        for vuln in self.vulnerabilidades:
            severidades[vuln['severidad']] += 1
        
        for severidad, count in sorted(severidades.items(), key=lambda x: ['Crítica', 'Alta', 'Media', 'Baja'].index(x[0])):
            print(f"  {severidad}: {count} vulnerabilidades")
        
        # Servicios más comunes
        print(f"\n🔧 SERVICIOS MÁS COMUNES:")
        servicios_count = defaultdict(int)
        for servicio in self.servicios_detectados:
            servicios_count[servicio['servicio']] += 1
        
        for servicio, count in sorted(servicios_count.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {servicio}: {count} instancias")
        
        # Hosts con más vulnerabilidades
        print(f"\n⚠️ HOSTS CON MÁS VULNERABILIDADES:")
        host_vulns = defaultdict(int)
        for vuln in self.vulnerabilidades:
            host_vulns[vuln['host']] += 1
        
        for host, count in sorted(host_vulns.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {host}: {count} vulnerabilidades")
    
    def generar_reporte_riesgo(self):
        """
        Genera un reporte de riesgo consolidado
        """
        print("\n" + "="*80)
        print("REPORTE DE RIESGO CONSOLIDADO")
        print("="*80)
        
        if not self.vulnerabilidades:
            print("No se encontraron vulnerabilidades para generar reporte de riesgo")
            return
        
        # Calcular puntuación de riesgo por host
        puntuaciones_riesgo = {}
        pesos_severidad = {'Crítica': 10, 'Alta': 7, 'Media': 4, 'Baja': 1}
        
        for vuln in self.vulnerabilidades:
            host = vuln['host']
            if host not in puntuaciones_riesgo:
                puntuaciones_riesgo[host] = 0
            puntuaciones_riesgo[host] += pesos_severidad[vuln['severidad']]
        
        # Clasificar hosts por nivel de riesgo
        print("\n📈 NIVEL DE RIESGO POR HOST:")
        print("-" * 50)
        
        for host, puntuacion in sorted(puntuaciones_riesgo.items(), key=lambda x: x[1], reverse=True):
            if puntuacion >= 20:
                nivel = "🔴 CRÍTICO"
            elif puntuacion >= 10:
                nivel = "🟡 ALTO"
            elif puntuacion >= 5:
                nivel = "🟠 MEDIO"
            else:
                nivel = "🟢 BAJO"
            
            print(f"  {host}: {puntuacion} puntos - {nivel}")
        
        # Recomendaciones generales
        print(f"\n💡 RECOMENDACIONES:")
        if any(v['severidad'] == 'Crítica' for v in self.vulnerabilidades):
            print("  • Parchear inmediatamente vulnerabilidades CRÍTICAS")
        if any(v['servicio'] == 'FTP' for v in self.vulnerabilidades):
            print("  • Deshabilitar FTP o usar SFTP/FTPS")
        if any(v['servicio'] == 'RDP' for v in self.vulnerabilidades):
            print("  • Restringir acceso RDP y usar VPN")
        if any('SSL' in v['vulnerabilidad'] for v in self.vulnerabilidades):
            print("  • Actualizar configuración SSL/TLS")
        
        print("  • Implementar parches de seguridad regularmente")
        print("  • Realizar escaneos de vulnerabilidades periódicamente")
    
    def exportar_reporte_csv(self, archivo="reporte_vulnerabilidades.csv"):
        """Exporta el reporte de vulnerabilidades a CSV"""
        try:
            with open(archivo, 'w', newline='', encoding='utf-8') as csvfile:
                campos = ['host', 'servicio', 'version', 'vulnerabilidad', 'severidad', 'CVE', 'descripcion', 'timestamp']
                writer = csv.DictWriter(csvfile, fieldnames=campos)
                writer.writeheader()
                
                for vuln in self.vulnerabilidades:
                    writer.writerow(vuln)
            
            print(f"✅ Reporte exportado a {archivo}")
        except Exception as e:
            print(f"❌ Error exportando reporte: {e}")
    
    def guardar_datos(self):
        """Guarda todos los datos en archivo JSON"""
        try:
            datos = {
                'hosts': self.hosts,
                'servicios_detectados': self.servicios_detectados,
                'vulnerabilidades': self.vulnerabilidades,
                'intentos_escaneo': self.intentos_escaneo[-1000:],  # Solo últimos 1000
                'estadisticas': self.estadisticas,
                'metadata': {
                    'ultima_actualizacion': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'total_registros': len(self.vulnerabilidades)
                }
            }
            
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                json.dump(datos, f, indent=2, ensure_ascii=False, default=str)
            
        except Exception as e:
            print(f"Error guardando datos: {e}")
    
    def cargar_datos(self):
        """Carga los datos desde archivo JSON"""
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                datos = json.load(f)
            
            self.hosts = datos.get('hosts', [])
            self.servicios_detectados = datos.get('servicios_detectados', [])
            self.vulnerabilidades = datos.get('vulnerabilidades', [])
            self.intentos_escaneo = datos.get('intentos_escaneo', [])
            self.estadisticas = datos.get('estadisticas', self.estadisticas)
            
            print(f"✅ Datos cargados: {len(self.hosts)} hosts, {len(self.vulnerabilidades)} vulnerabilidades")
            
        except FileNotFoundError:
            print("ℹ️ No se encontró archivo de datos. Se creará uno nuevo.")
        except Exception as e:
            print(f"❌ Error cargando datos: {e}")

# Función principal para demostrar el sistema
def main():
    escaner = SimuladorEscaneoVulnerabilidades()
    
    print("🔍 SIMULADOR DE ESCANEO DE VULNERABILIDADES")
    print("="*50)
    
    # Agregar hosts de ejemplo si no hay datos
    if not escaner.hosts:
        print("Registrando hosts de ejemplo...")
        
        hosts_ejemplo = [
            ("192.168.1.1", "Router Principal", "Router"),
            ("192.168.1.10", "Servidor Web", "Servidor"),
            ("192.168.1.20", "Servidor Base de Datos", "Servidor"),
            ("192.168.1.50", "Estación de Trabajo", "PC"),
            ("192.168.1.100", "Servidor Archivos", "Servidor"),
        ]
        
        for host, descripcion, tipo in hosts_ejemplo:
            escaner.registrar_host(host, descripcion, tipo)
    
    while True:
        print("\n" + "="*40)
        print("MENÚ PRINCIPAL")
        print("="*40)
        print("1. Registrar nuevo host")
        print("2. Escanear host específico")
        print("3. Escanear todos los hosts")
        print("4. Mostrar reporte de vulnerabilidades")
        print("5. Mostrar reporte de servicios")
        print("6. Mostrar estadísticas completas")
        print("7. Generar reporte de riesgo")
        print("8. Exportar reporte CSV")
        print("9. Salir")
        
        opcion = input("\nSeleccione una opción: ").strip()
        
        if opcion == "1":
            host = input("Host (IP o hostname): ").strip()
            descripcion = input("Descripción: ").strip()
            tipo = input("Tipo (Router/Servidor/PC): ").strip() or "Servidor"
            escaner.registrar_host(host, descripcion, tipo)
        
        elif opcion == "2":
            if not escaner.hosts:
                print("❌ No hay hosts registrados")
                continue
            
            print("\nHosts disponibles:")
            for i, host in enumerate(escaner.hosts, 1):
                print(f"  {i}. {host['direccion']} - {host['descripcion']}")
            
            try:
                seleccion = int(input("\nSeleccione el número del host: ")) - 1
                if 0 <= seleccion < len(escaner.hosts):
                    host_seleccionado = escaner.hosts[seleccion]['direccion']
                    escaner.escanear_host(host_seleccionado)
                else:
                    print("❌ Selección inválida")
            except ValueError:
                print("❌ Ingrese un número válido")
        
        elif opcion == "3":
            if not escaner.hosts:
                print("❌ No hay hosts registrados")
                continue
            escaner.escanear_red_completa()
        
        elif opcion == "4":
            print("\nFiltros de reporte:")
            print("1. Todas las vulnerabilidades")
            print("2. Solo críticas")
            print("3. Solo altas")
            print("4. Por host específico")
            
            filtro_opcion = input("Seleccione filtro: ").strip()
            
            if filtro_opcion == "1":
                escaner.mostrar_reporte_vulnerabilidades()
            elif filtro_opcion == "2":
                escaner.mostrar_reporte_vulnerabilidades(filtro_severidad="Crítica")
            elif filtro_opcion == "3":
                escaner.mostrar_reporte_vulnerabilidades(filtro_severidad="Alta")
            elif filtro_opcion == "4":
                host = input("Host específico: ").strip()
                escaner.mostrar_reporte_vulnerabilidades(filtro_host=host)
            else:
                escaner.mostrar_reporte_vulnerabilidades()
        
        elif opcion == "5":
            host = input("Host específico (dejar vacío para todos): ").strip() or None
            escaner.mostrar_reporte_servicios(filtro_host=host)
        
        elif opcion == "6":
            escaner.mostrar_estadisticas_completas()
        
        elif opcion == "7":
            escaner.generar_reporte_riesgo()
        
        elif opcion == "8":
            escaner.exportar_reporte_csv()
        
        elif opcion == "9":
            print("¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()