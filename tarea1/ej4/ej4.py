class Bus:
    def __init__(self, empresa, ruta, capacidad_total, costo_pasaje=1.50):
        """
        Constructor de la clase Bus
        """
        self.empresa = empresa
        self.ruta = ruta
        self.capacidad_total = capacidad_total
        self.pasajeros_actuales = 0
        self.asientos_disponibles = capacidad_total
        self.costo_pasaje = costo_pasaje
    
    def subir_pasajeros(self, cantidad):
        """
        Sube una cantidad de pasajeros al bus
        """
        if cantidad <= 0:
            print("ERROR: La cantidad de pasajeros debe ser mayor a 0")
            return
        
        if cantidad > self.asientos_disponibles:
            print(f"ERROR: No hay suficientes asientos disponibles. Solo quedan {self.asientos_disponibles} asientos.")
            return
        
        self.pasajeros_actuales += cantidad
        self.asientos_disponibles -= cantidad
        print(f"{cantidad} pasajeros subieron al bus.")
    
    def cobrar_pasaje(self):
        """
        Cobra el pasaje a los pasajeros
        """
        total_recaudado = self.pasajeros_actuales * self.costo_pasaje
        print(f"Se cobró el pasaje a {self.pasajeros_actuales} pasajeros.")
        print(f"Total recaudado: {total_recaudado} Bs.")
        print(f"Costo por pasajero: {self.costo_pasaje} Bs.")
    
    def mostrar_asientos_disponibles(self):
        """
        Muestra cuántos asientos quedan disponibles
        """
        print(f"Asientos disponibles: {self.asientos_disponibles}")
        print(f"Asientos ocupados: {self.pasajeros_actuales}")
        print(f"Capacidad total: {self.capacidad_total}")
    
    def mostrar_datos(self):
        """
        Muestra todos los datos del bus
        """
        print("=== DATOS DEL BUS ===")
        print("Empresa:", self.empresa)
        print("Ruta:", self.ruta)
        print("Capacidad total:", self.capacidad_total)
        print("Pasajeros actuales:", self.pasajeros_actuales)
        print("Asientos disponibles:", self.asientos_disponibles)
        print("Costo del pasaje:", self.costo_pasaje, "Bs.")
    
    def get_asientos_disponibles(self):
        return self.asientos_disponibles


if __name__ == "__main__":

    bus = Bus("TransBolivia", "La Paz - El Alto", 40)
    
    print("=== BUS INICIAL ===")
    bus.mostrar_datos()
    
    print("\n=== SUBIENDO PASAJEROS ===")
    bus.subir_pasajeros(15)
    bus.mostrar_asientos_disponibles()
    
    print("\n=== COBRANDO PASAJE ===")
    bus.cobrar_pasaje()
    
    print("\n=== SUBIENDO MÁS PASAJEROS ===")
    bus.subir_pasajeros(20)
    bus.mostrar_asientos_disponibles()
    
    print("\n=== INTENTANDO SUBIR MÁS PASAJEROS DE LOS PERMITIDOS ===")
    bus.subir_pasajeros(10) 
    
    print("\n=== COBRANDO PASAJE NUEVAMENTE ===")
    bus.cobrar_pasaje()
    
    print("\n=== ESTADO FINAL DEL BUS ===")
    bus.mostrar_datos()