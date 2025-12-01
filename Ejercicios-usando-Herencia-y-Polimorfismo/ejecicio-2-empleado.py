class Empleado:
    """Clase base para todos los empleados"""
    
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
    
    def calcular_bono(self):
        """Método que debe ser implementado por las clases hijas"""
        raise NotImplementedError("Las subclases deben implementar este método")
    
    def mostrar_informacion(self):
        """Método común para todos los empleados"""
        return f"{self.__class__.__name__}: {self.nombre} - Salario base: ${self.salario:,.2f}"
    
    def salario_total(self):
        """Calcula el salario total (base + bono)"""
        bono = self.calcular_bono()
        return self.salario + bono


class Gerente(Empleado):
    """Clase hija que representa un Gerente"""
    
    def __init__(self, nombre, salario, departamento, objetivos_cumplidos=0):
        super().__init__(nombre, salario)
        self.departamento = departamento
        self.objetivos_cumplidos = objetivos_cumplidos  # Porcentaje de 0 a 100
    
    def calcular_bono(self):
        """Los gerentes reciben un bono del 30% del salario más un 1% por cada objetivo cumplido"""
        bono_base = self.salario * 0.30
        bono_objetivos = self.salario * (self.objetivos_cumplidos / 100)
        return bono_base + bono_objetivos
    
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        bono = self.calcular_bono()
        return f"{info_base} - Departamento: {self.departamento} - Bono: ${bono:,.2f}"


class Tecnico(Empleado):
    """Clase hija que representa un Técnico"""
    
    def __init__(self, nombre, salario, especialidad, horas_extra=0):
        super().__init__(nombre, salario)
        self.especialidad = especialidad
        self.horas_extra = horas_extra
    
    def calcular_bono(self):
        """Los técnicos reciben un bono fijo más pago por horas extra"""
        bono_fijo = self.salario * 0.15
        pago_horas_extra = (self.salario / 160) * self.horas_extra * 1.5  # 1.5x el valor hora normal
        return bono_fijo + pago_horas_extra
    
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        bono = self.calcular_bono()
        return f"{info_base} - Especialidad: {self.especialidad} - Bono: ${bono:,.2f}"


class Vendedor(Empleado):
    """Clase hija que representa un Vendedor"""
    
    def __init__(self, nombre, salario, ventas_mensuales=0, comision_porcentaje=10):
        super().__init__(nombre, salario)
        self.ventas_mensuales = ventas_mensuales
        self.comision_porcentaje = comision_porcentaje
    
    def calcular_bono(self):
        """Los vendedores reciben comisión sobre las ventas"""
        return self.ventas_mensuales * (self.comision_porcentaje / 100)
    
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        bono = self.calcular_bono()
        return f"{info_base} - Ventas: ${self.ventas_mensuales:,.2f} - Bono: ${bono:,.2f}"


class Desarrollador(Empleado):
    """Clase hija que representa un Desarrollador"""
    
    def __init__(self, nombre, salario, lenguaje_principal, proyectos_completados=0):
        super().__init__(nombre, salario)
        self.lenguaje_principal = lenguaje_principal
        self.proyectos_completados = proyectos_completados
    
    def calcular_bono(self):
        """Los desarrolladores reciben bono por proyectos completados"""
        bono_base = self.salario * 0.20
        bono_proyectos = self.proyectos_completados * 500  # $500 por proyecto
        return bono_base + bono_proyectos
    
    def mostrar_informacion(self):
        info_base = super().mostrar_informacion()
        bono = self.calcular_bono()
        return f"{info_base} - Lenguaje: {self.lenguaje_principal} - Bono: ${bono:,.2f}"


# Ejemplo de uso
if __name__ == "__main__":
    print("=== SISTEMA DE EMPLEADOS Y BONOS ===\n")
    
    # Crear diferentes tipos de empleados
    empleados = [
        Gerente("Ana García", 5000, "Ventas", objetivos_cumplidos=85),
        Tecnico("Carlos López", 3000, "Electrónica", horas_extra=20),
        Vendedor("María Rodríguez", 2500, ventas_mensuales=15000),
        Desarrollador("Pedro Martínez", 4000, "Python", proyectos_completados=3),
        Gerente("Laura Silva", 6000, "Tecnología", objetivos_cumplidos=95)
    ]
    
    # Mostrar información de todos los empleados
    print("=== INFORMACIÓN DE EMPLEADOS ===")
    for empleado in empleados:
        print(empleado.mostrar_informacion())
    
    # Calcular y mostrar salarios totales
    print("\n=== SALARIOS TOTALES ===")
    for empleado in empleados:
        bono = empleado.calcular_bono()
        salario_total = empleado.salario_total()
        print(f"{empleado.nombre}:")
        print(f"  - Salario base: ${empleado.salario:,.2f}")
        print(f"  - Bono: ${bono:,.2f}")
        print(f"  - Total: ${salario_total:,.2f}")
    
    # Demostración de polimorfismo
    print("\n=== DEMOSTRACIÓN DE POLIMORFISMO ===")
    for empleado in empleados:
        print(f"{empleado.nombre} - Bono calculado: ${empleado.calcular_bono():,.2f}")