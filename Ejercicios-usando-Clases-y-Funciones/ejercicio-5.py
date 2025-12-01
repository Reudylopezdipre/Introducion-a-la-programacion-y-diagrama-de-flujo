class Estudiante:
    def __init__(self, nombre, calificaciones=None):
        """
        Constructor de la clase Estudiante
        
        Args:
            nombre (str): Nombre del estudiante
            calificaciones (list): Lista de calificaciones (por defecto lista vacía)
        """
        self.nombre = nombre
        self.calificaciones = calificaciones if calificaciones is not None else []
    
    def agregar_calificacion(self, calificacion):
        """
        Agrega una calificación a la lista del estudiante
        
        Args:
            calificacion (float): Calificación a agregar
            
        Returns:
            str: Mensaje de confirmación
        """
        if 0 <= calificacion <= 100:
            self.calificaciones.append(calificacion)
            return f"Calificación {calificacion} agregada exitosamente"
        else:
            return "Error: La calificación debe estar entre 0 y 100"
    
    def calcular_promedio(self):
        """
        Calcula el promedio de las calificaciones
        
        Returns:
            float or str: Promedio calculado o mensaje de error
        """
        if not self.calificaciones:
            return "No hay calificaciones para calcular el promedio"
        
        promedio = sum(self.calificaciones) / len(self.calificaciones)
        return round(promedio, 2)
    
    def obtener_calificacion_letra(self):
        """
        Convierte el promedio a calificación con letra
        
        Returns:
            str: Calificación en formato letra
        """
        promedio = self.calcular_promedio()
        
        if isinstance(promedio, str):  # Si no hay calificaciones
            return "Sin calificación"
        
        if promedio >= 90:
            return "A"
        elif promedio >= 80:
            return "B"
        elif promedio >= 70:
            return "C"
        elif promedio >= 60:
            return "D"
        else:
            return "F"
    
    def mostrar_informe(self):
        """
        Muestra un informe completo del estudiante
        """
        print(f"\n=== INFORME ACADÉMICO ===")
        print(f"Estudiante: {self.nombre}")
        print(f"Calificaciones: {self.calificaciones}")
        
        promedio = self.calcular_promedio()
        if isinstance(promedio, str):
            print(f"Promedio: {promedio}")
        else:
            print(f"Promedio: {promedio}")
            print(f"Calificación: {self.obtener_calificacion_letra()}")
    
    def __str__(self):
        """
        Representación en string del estudiante
        """
        promedio = self.calcular_promedio()
        if isinstance(promedio, str):
            return f"Estudiante: {self.nombre}, Calificaciones: {self.calificaciones}"
        else:
            return f"Estudiante: {self.nombre}, Calificaciones: {self.calificaciones}, Promedio: {promedio}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear estudiantes de diferentes formas
    estudiante1 = Estudiante("María González", [85, 92, 78, 90])
    estudiante2 = Estudiante("Pedro Sánchez")  # Sin calificaciones iniciales
    estudiante3 = Estudiante("Laura Martínez", [95, 88, 76, 91, 84])
    
    print("=== SISTEMA DE ESTUDIANTES ===")
    
    # Probar el primer estudiante
    print(f"\n--- {estudiante1.nombre} ---")
    estudiante1.mostrar_informe()
    
    # Probar el segundo estudiante (sin calificaciones iniciales)
    print(f"\n--- {estudiante2.nombre} ---")
    estudiante2.mostrar_informe()
    
    # Agregar calificaciones al segundo estudiante
    print("\nAgregando calificaciones...")
    print(estudiante2.agregar_calificacion(75))
    print(estudiante2.agregar_calificacion(82))
    print(estudiante2.agregar_calificacion(90))
    print(estudiante2.agregar_calificacion(105))  # Calificación inválida
    
    estudiante2.mostrar_informe()
    
    # Probar el tercer estudiante
    print(f"\n--- {estudiante3.nombre} ---")
    estudiante3.mostrar_informe()
    print(f"Calificación con letra: {estudiante3.obtener_calificacion_letra()}")
    
    # Mostrar representación string
    print(f"\nRepresentación string:")
    print(estudiante1)
    print(estudiante2)
    print(estudiante3)