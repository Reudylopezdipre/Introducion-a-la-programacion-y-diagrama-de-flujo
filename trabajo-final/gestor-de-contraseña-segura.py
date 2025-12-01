import hashlib
import secrets
import string
import re
import json
import csv
import getpass
from datetime import datetime
from cryptography.fernet import Fernet
import base64
import os

class GestorContraseñasSeguras:
    def __init__(self, archivo_datos="contraseñas.dat", archivo_clave="clave.key"):
        # Vectores para almacenamiento en memoria
        self.usuarios = []
        self.contraseñas_hash = []
        self.fechas_creacion = []
        self.estados_contraseña = []  # "fuerte", "media", "débil"
        
        # Configuración de seguridad
        self.longitud_minima = 8
        self.requerimientos = {
            'mayusculas': True,
            'minusculas': True,
            'numeros': True,
            'simbolos': True,
            'longitud_minima': 8
        }
        
        # Archivos de almacenamiento
        self.archivo_datos = archivo_datos
        self.archivo_clave = archivo_clave
        self.clave_cifrado = self._cargar_o_crear_clave()
        self.cipher_suite = Fernet(self.clave_cifrado)
        
        # Cargar datos existentes
        self._cargar_datos()
    
    def _cargar_o_crear_clave(self):
        """Carga la clave de cifrado o crea una nueva"""
        try:
            if os.path.exists(self.archivo_clave):
                with open(self.archivo_clave, 'rb') as f:
                    return f.read()
            else:
                clave = Fernet.generate_key()
                with open(self.archivo_clave, 'wb') as f:
                    f.write(clave)
                return clave
        except Exception as e:
            print(f"Error con la clave de cifrado: {e}")
            return Fernet.generate_key()
    
    def _cifrar(self, texto):
        """Cifra un texto usando Fernet"""
        return self.cipher_suite.encrypt(texto.encode()).decode()
    
    def _descifrar(self, texto_cifrado):
        """Descifra un texto cifrado"""
        return self.cipher_suite.decrypt(texto_cifrado.encode()).decode()
    
    def _cargar_datos(self):
        """Carga los datos desde el archivo cifrado"""
        try:
            if os.path.exists(self.archivo_datos):
                with open(self.archivo_datos, 'r', encoding='utf-8') as f:
                    lineas = f.readlines()
                    
                for linea in lineas:
                    if linea.strip():
                        try:
                            datos = json.loads(self._descifrar(linea.strip()))
                            self.usuarios.append(datos['usuario'])
                            self.contraseñas_hash.append(datos['contraseña_hash'])
                            self.fechas_creacion.append(datos['fecha_creacion'])
                            self.estados_contraseña.append(datos['estado'])
                        except Exception as e:
                            print(f"Error descifrando línea: {e}")
                            
                print(f"Datos cargados: {len(self.usuarios)} usuarios")
        except Exception as e:
            print(f"Error cargando datos: {e}")
    
    def _guardar_datos(self):
        """Guarda todos los datos en el archivo cifrado"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as f:
                for i in range(len(self.usuarios)):
                    datos = {
                        'usuario': self.usuarios[i],
                        'contraseña_hash': self.contraseñas_hash[i],
                        'fecha_creacion': self.fechas_creacion[i],
                        'estado': self.estados_contraseña[i]
                    }
                    linea_cifrada = self._cifrar(json.dumps(datos))
                    f.write(linea_cifrada + '\n')
            print("Datos guardados exitosamente")
        except Exception as e:
            print(f"Error guardando datos: {e}")
    
    def _calcular_hash(self, contraseña):
        """Calcula el hash SHA-256 de una contraseña"""
        return hashlib.sha256(contraseña.encode()).hexdigest()
    
    def verificar_fortaleza_contraseña(self, contraseña):
        """
        Verifica la fortaleza de una contraseña
        
        Returns:
            dict: Resultado del análisis de fortaleza
        """
        puntuacion = 0
        debilidades = []
        recomendaciones = []
        
        # Verificar longitud
        if len(contraseña) >= 12:
            puntuacion += 3
        elif len(contraseña) >= 8:
            puntuacion += 2
        elif len(contraseña) >= 6:
            puntuacion += 1
            debilidades.append("Contraseña muy corta")
            recomendaciones.append("Usar al menos 8 caracteres")
        else:
            debilidades.append("Contraseña extremadamente corta")
            recomendaciones.append("Usar al menos 8 caracteres")
        
        # Verificar mayúsculas
        if re.search(r'[A-Z]', contraseña):
            puntuacion += 1
        else:
            debilidades.append("Sin letras mayúsculas")
            recomendaciones.append("Incluir al menos una letra mayúscula")
        
        # Verificar minúsculas
        if re.search(r'[a-z]', contraseña):
            puntuacion += 1
        else:
            debilidades.append("Sin letras minúsculas")
            recomendaciones.append("Incluir al menos una letra minúscula")
        
        # Verificar números
        if re.search(r'[0-9]', contraseña):
            puntuacion += 1
        else:
            debilidades.append("Sin números")
            recomendaciones.append("Incluir al menos un número")
        
        # Verificar símbolos
        if re.search(r'[!@#$%^&*(),.?":{}|<>]', contraseña):
            puntuacion += 2
        else:
            debilidades.append("Sin caracteres especiales")
            recomendaciones.append("Incluir al menos un carácter especial")
        
        # Verificar patrones comunes
        patrones_debiles = [
            '123456', 'password', 'qwerty', 'admin', '111111',
            'abc123', 'contraseña', '000000', '123123'
        ]
        
        if contraseña.lower() in patrones_debiles:
            puntuacion = 0
            debilidades.append("Contraseña comúnmente usada")
            recomendaciones.append("Elegir una contraseña más única")
        
        # Verificar secuencias
        if re.search(r'(.)\1{2,}', contraseña):  # Caracteres repetidos
            debilidades.append("Muchos caracteres repetidos")
            recomendaciones.append("Evitar caracteres repetidos consecutivos")
        
        # Determinar nivel de fortaleza
        if puntuacion >= 7:
            estado = "fuerte"
            color = "🟢"
        elif puntuacion >= 4:
            estado = "media"
            color = "🟡"
        else:
            estado = "débil"
            color = "🔴"
        
        return {
            'puntuacion': puntuacion,
            'estado': estado,
            'color': color,
            'debilidades': debilidades,
            'recomendaciones': recomendaciones,
            'longitud': len(contraseña)
        }
    
    def generar_contraseña_segura(self, longitud=12):
        """Genera una contraseña segura automáticamente"""
        if longitud < 8:
            longitud = 8
        
        # Definir conjuntos de caracteres
        mayusculas = string.ascii_uppercase
        minusculas = string.ascii_lowercase
        numeros = string.digits
        simbolos = "!@#$%^&*()_+-=[]{}|;:,.<>?"
        
        # Asegurar al menos un carácter de cada tipo
        contraseña = [
            secrets.choice(mayusculas),
            secrets.choice(minusculas),
            secrets.choice(numeros),
            secrets.choice(simbolos)
        ]
        
        # Completar con caracteres aleatorios
        todos_caracteres = mayusculas + minusculas + numeros + simbolos
        contraseña.extend(secrets.choice(todos_caracteres) for _ in range(longitud - 4))
        
        # Mezclar la contraseña
        secrets.SystemRandom().shuffle(contraseña)
        
        return ''.join(contraseña)
    
    def registrar_usuario(self, usuario, contraseña=None):
        """
        Registra un nuevo usuario con su contraseña
        
        Args:
            usuario (str): Nombre de usuario
            contraseña (str): Contraseña (si None, se genera automáticamente)
        """
        # Verificar si el usuario ya existe
        if usuario in self.usuarios:
            print(f"Error: El usuario '{usuario}' ya existe")
            return False
        
        # Generar contraseña si no se proporciona
        if contraseña is None:
            contraseña = self.generar_contraseña_segura()
            print(f"Contraseña generada automáticamente: {contraseña}")
        
        # Verificar fortaleza
        analisis = self.verificar_fortaleza_contraseña(contraseña)
        
        # Mostrar resultados de verificación
        print(f"\nAnálisis de contraseña para '{usuario}':")
        print(f"Fortaleza: {analisis['color']} {analisis['estado'].upper()}")
        print(f"Puntuación: {analisis['puntuacion']}/8")
        print(f"Longitud: {analisis['longitud']} caracteres")
        
        if analisis['debilidades']:
            print("\nDebilidades encontradas:")
            for debilidad in analisis['debilidades']:
                print(f"  • {debilidad}")
        
        if analisis['recomendaciones']:
            print("\nRecomendaciones:")
            for recomendacion in analisis['recomendaciones']:
                print(f"  • {recomendacion}")
        
        # Preguntar confirmación si la contraseña es débil
        if analisis['estado'] == "débil":
            confirmar = input("\n⚠️  La contraseña es débil. ¿Desea registrarla de todos modos? (s/n): ")
            if confirmar.lower() != 's':
                print("Registro cancelado")
                return False
        
        # Registrar el usuario
        contraseña_hash = self._calcular_hash(contraseña)
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        self.usuarios.append(usuario)
        self.contraseñas_hash.append(contraseña_hash)
        self.fechas_creacion.append(fecha_actual)
        self.estados_contraseña.append(analisis['estado'])
        
        # Guardar datos
        self._guardar_datos()
        
        print(f"✅ Usuario '{usuario}' registrado exitosamente")
        self.generar_alertas(usuario, analisis)
        
        return True
    
    def verificar_contraseña(self, usuario, contraseña):
        """
        Verifica si una contraseña es correcta para un usuario
        
        Args:
            usuario (str): Nombre de usuario
            contraseña (str): Contraseña a verificar
        
        Returns:
            bool: True si la contraseña es correcta
        """
        try:
            indice = self.usuarios.index(usuario)
            contraseña_hash = self._calcular_hash(contraseña)
            return self.contraseñas_hash[indice] == contraseña_hash
        except ValueError:
            return False
    
    def generar_alertas(self, usuario, analisis_contraseña):
        """Genera alertas sobre la seguridad de las contraseñas"""
        alertas = []
        
        if analisis_contraseña['estado'] == "débil":
            alertas.append(f"ALERTA: Contraseña DÉBIL para usuario '{usuario}'")
        
        if analisis_contraseña['puntuacion'] < 4:
            alertas.append(f"ALERTA CRÍTICA: Contraseña MUY DÉBIL para usuario '{usuario}'")
        
        # Verificar si la contraseña tiene más de 90 días (simulación)
        try:
            indice = self.usuarios.index(usuario)
            fecha_creacion = datetime.strptime(self.fechas_creacion[indice], "%Y-%m-%d %H:%M:%S")
            dias_desde_creacion = (datetime.now() - fecha_creacion).days
            
            if dias_desde_creacion > 90:
                alertas.append(f"ALERTA: Contraseña antigua para '{usuario}' ({dias_desde_creacion} días)")
        except:
            pass
        
        # Mostrar alertas
        for alerta in alertas:
            print(f"🚨 {alerta}")
        
        # Guardar alertas en archivo
        self._guardar_alertas(usuario, alertas)
    
    def _guardar_alertas(self, usuario, alertas):
        """Guarda las alertas en un archivo de log"""
        try:
            with open("alertas_contraseñas.log", "a", encoding="utf-8") as f:
                for alerta in alertas:
                    f.write(f"{datetime.now()} - {alerta}\n")
        except Exception as e:
            print(f"Error guardando alertas: {e}")
    
    def mostrar_usuarios(self):
        """Muestra todos los usuarios registrados con su estado de contraseña"""
        print("\n" + "="*80)
        print("USUARIOS REGISTRADOS")
        print("="*80)
        print(f"{'Usuario':<20} {'Fecha Creación':<20} {'Estado Contraseña':<15} {'Hash'}")
        print("-"*80)
        
        for i in range(len(self.usuarios)):
            estado_color = {
                "fuerte": "🟢 FUERTE",
                "media": "🟡 MEDIA", 
                "débil": "🔴 DÉBIL"
            }.get(self.estados_contraseña[i], "DESCONOCIDO")
            
            hash_corto = self.contraseñas_hash[i][:16] + "..."
            print(f"{self.usuarios[i]:<20} {self.fechas_creacion[i]:<20} {estado_color:<15} {hash_corto}")
    
    def mostrar_estadisticas(self):
        """Muestra estadísticas de seguridad"""
        print("\n" + "="*50)
        print("ESTADÍSTICAS DE SEGURIDAD")
        print("="*50)
        
        total_usuarios = len(self.usuarios)
        if total_usuarios == 0:
            print("No hay usuarios registrados")
            return
        
        # Contar estados de contraseña
        contraseñas_fuertes = self.estados_contraseña.count("fuerte")
        contraseñas_medias = self.estados_contraseña.count("media")
        contraseñas_debiles = self.estados_contraseña.count("débil")
        
        print(f"Total de usuarios: {total_usuarios}")
        print(f"Contraseñas fuertes: {contraseñas_fuertes} ({contraseñas_fuertes/total_usuarios*100:.1f}%)")
        print(f"Contraseñas medias: {contraseñas_medias} ({contraseñas_medias/total_usuarios*100:.1f}%)")
        print(f"Contraseñas débiles: {contraseñas_debiles} ({contraseñas_debiles/total_usuarios*100:.1f}%)")
        
        # Usuarios que necesitan atención
        if contraseñas_debiles > 0:
            print(f"\n⚠️  {contraseñas_debiles} usuarios necesitan cambiar sus contraseñas")
    
    def exportar_reporte(self, archivo="reporte_contraseñas.csv"):
        """Exporta un reporte de seguridad a CSV"""
        try:
            with open(archivo, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['Usuario', 'Fecha_Creacion', 'Estado_Contraseña', 'Hash'])
                
                for i in range(len(self.usuarios)):
                    writer.writerow([
                        self.usuarios[i],
                        self.fechas_creacion[i],
                        self.estados_contraseña[i],
                        self.contraseñas_hash[i]
                    ])
            
            print(f"Reporte exportado a {archivo}")
        except Exception as e:
            print(f"Error exportando reporte: {e}")
    
    def cambiar_contraseña(self, usuario, contraseña_actual, nueva_contraseña):
        """Permite a un usuario cambiar su contraseña"""
        try:
            indice = self.usuarios.index(usuario)
            
            # Verificar contraseña actual
            if not self.verificar_contraseña(usuario, contraseña_actual):
                print("❌ Contraseña actual incorrecta")
                return False
            
            # Verificar fortaleza de nueva contraseña
            analisis = self.verificar_fortaleza_contraseña(nueva_contraseña)
            
            if analisis['estado'] == "débil":
                confirmar = input("⚠️  La nueva contraseña es débil. ¿Continuar? (s/n): ")
                if confirmar.lower() != 's':
                    return False
            
            # Actualizar contraseña
            nueva_hash = self._calcular_hash(nueva_contraseña)
            self.contraseñas_hash[indice] = nueva_hash
            self.estados_contraseña[indice] = analisis['estado']
            self.fechas_creacion[indice] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            
            self._guardar_datos()
            print("✅ Contraseña cambiada exitosamente")
            self.generar_alertas(usuario, analisis)
            return True
            
        except ValueError:
            print("❌ Usuario no encontrado")
            return False

# Función principal para demostrar el sistema
def main():
    gestor = GestorContraseñasSeguras()
    
    print("🔐 GESTOR DE CONTRASEÑAS SEGURAS")
    print("="*50)
    
    while True:
        print("\nOpciones:")
        print("1. Registrar nuevo usuario")
        print("2. Verificar contraseña")
        print("3. Mostrar usuarios")
        print("4. Mostrar estadísticas")
        print("5. Cambiar contraseña")
        print("6. Verificar fortaleza de contraseña")
        print("7. Generar contraseña segura")
        print("8. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            usuario = input("Nombre de usuario: ")
            usar_generada = input("¿Generar contraseña automáticamente? (s/n): ")
            
            if usar_generada.lower() == 's':
                gestor.registrar_usuario(usuario)
            else:
                contraseña = getpass.getpass("Contraseña: ")
                gestor.registrar_usuario(usuario, contraseña)
        
        elif opcion == "2":
            usuario = input("Usuario: ")
            contraseña = getpass.getpass("Contraseña: ")
            
            if gestor.verificar_contraseña(usuario, contraseña):
                print("✅ Contraseña correcta")
            else:
                print("❌ Contraseña incorrecta o usuario no existe")
        
        elif opcion == "3":
            gestor.mostrar_usuarios()
        
        elif opcion == "4":
            gestor.mostrar_estadisticas()
        
        elif opcion == "5":
            usuario = input("Usuario: ")
            contraseña_actual = getpass.getpass("Contraseña actual: ")
            nueva_contraseña = getpass.getpass("Nueva contraseña: ")
            gestor.cambiar_contraseña(usuario, contraseña_actual, nueva_contraseña)
        
        elif opcion == "6":
            contraseña = getpass.getpass("Contraseña a verificar: ")
            analisis = gestor.verificar_fortaleza_contraseña(contraseña)
            print(f"\nResultado: {analisis['color']} {analisis['estado'].upper()}")
            print(f"Puntuación: {analisis['puntuacion']}/8")
        
        elif opcion == "7":
            longitud = int(input("Longitud de la contraseña (mínimo 8): ") or "12")
            contraseña = gestor.generar_contraseña_segura(longitud)
            print(f"Contraseña generada: {contraseña}")
        
        elif opcion == "8":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()