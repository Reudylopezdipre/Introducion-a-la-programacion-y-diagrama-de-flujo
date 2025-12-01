class CuentaBancaria:
    def __init__(self, titular, balance=0):
        """
        Constructor de la clase CuentaBancaria
        
        Args:
            titular (str): Nombre del titular de la cuenta
            balance (float): Saldo inicial de la cuenta (por defecto 0)
        """
        self.titular = titular
        self.balance = balance
    
    def depositar(self, monto):
        """
        Deposita un monto en la cuenta
        
        Args:
            monto (float): Cantidad a depositar
            
        Returns:
            str: Mensaje confirmando el depósito
        """
        if monto > 0:
            self.balance += monto
            return f"Depósito exitoso. Nuevo balance: ${self.balance:.2f}"
        else:
            return "Error: El monto a depositar debe ser mayor a cero"
    
    def retirar(self, monto):
        """
        Retira un monto de la cuenta
        
        Args:
            monto (float): Cantidad a retirar
            
        Returns:
            str: Mensaje confirmando el retiro o indicando error
        """
        if monto <= 0:
            return "Error: El monto a retirar debe ser mayor a cero"
        elif monto > self.balance:
            return "Error: Fondos insuficientes"
        else:
            self.balance -= monto
            return f"Retiro exitoso. Nuevo balance: ${self.balance:.2f}"
    
    def consultar_balance(self):
        """
        Consulta el balance actual de la cuenta
        
        Returns:
            str: Información del balance actual
        """
        return f"Titular: {self.titular}, Balance actual: ${self.balance:.2f}"
    
    def __str__(self):
        """
        Representación en string de la cuenta bancaria
        """
        return f"CuentaBancaria(Titular: {self.titular}, Balance: ${self.balance:.2f})"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cuenta bancari
    cuenta = CuentaBancaria("Juan Pérez", 1000)
    
    print("=== CUENTA BANCARIA ===")
    print(cuenta.consultar_balance())
    
    # Realizar operaciones
    print("\n--- Operaciones ---")
    print(cuenta.depositar(500))      # Depositar 500
    print(cuenta.retirar(200))        # Retirar 200
    print(cuenta.retirar(2000))       # Intentar retirar más del balance
    print(cuenta.depositar(-100))     # Intentar depositar monto negativo
    
    print(f"\nEstado final: {cuenta}")