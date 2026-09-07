class CuentaBancaria:
    def __init__(self, titular, nro_cuenta, saldo):
        """
        Constructor de la clase CuentaBancaria
        """
        self.titular = titular
        self.nro_cuenta = nro_cuenta
        self.saldo = saldo
    
    def depositar(self, cantidad):
        """
        Deposita una cantidad en la cuenta
        """
        if cantidad <= 0:
            print("ERROR: No se puede depositar un número negativo o 0")
            return
        self.saldo += cantidad
        print(f"Depósito exitoso. Nuevo saldo: {self.saldo} Bs.")
    
    def retirar(self, cantidad):
        """
        Retira una cantidad de la cuenta
        """
        if cantidad > self.saldo:
            print("ERROR: No se puede retirar más dinero del que tiene en la cuenta")
            return
        self.saldo -= cantidad
        print(f"Retiro exitoso. Nuevo saldo: {self.saldo} Bs.")
    
    def mostrar_datos(self):
        """
        Muestra los datos de la cuenta
        """
        print("=== DATOS DE LA CUENTA ===")
        print("Titular:", self.titular)
        print("Número de cuenta:", self.nro_cuenta)
        print("Saldo:", self.saldo, "Bs.")


#
if __name__ == "__main__":
   
    cuenta = CuentaBancaria("Juan Pérez", "1234567890", 1000.0)
    
    print("=== CUENTA INICIAL ===")
    cuenta.mostrar_datos()
    
    print("\n=== REALIZANDO DEPÓSITOS ===")
    cuenta.depositar(500)  
    cuenta.depositar(-100)  
    cuenta.depositar(0)  
    
    print("\n=== REALIZANDO RETIROS ===")
    cuenta.retirar(300)  
    cuenta.retirar(1500)  
    
    print("\n=== CUENTA FINAL ===")
    cuenta.mostrar_datos()