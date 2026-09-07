class Auto:
    def __init__(self, marca, modelo, año, kilometraje, color):
        """
        Constructor de la clase Auto
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = kilometraje  
        self.color = color
    
    def mostrar_kilometraje(self):
        """
        Muestra el kilometraje en kilómetros y metros
        """
        km = int(self.kilometraje)
        metros = int((self.kilometraje - km) * 1000)
        print(f"Kilometraje: {km} km {metros} m")
    
    def cambiar_color(self, nuevo_color):
        """
        Cambia el color del auto
        """
        self.color = nuevo_color
        print(f"Color cambiado a: {nuevo_color}")
    
    def mostrar_info(self):
        """
        Muestra información completa del auto
        """
        print(f"Auto: {self.marca} {self.modelo} ({self.año})")
        print(f"Color: {self.color}")
        self.mostrar_kilometraje()
    
    def get_kilometraje(self):
        return self.kilometraje
    
    def get_color(self):
        return self.color

if __name__ == "__main__":

    auto1 = Auto("Toyota", "Corolla", 2020, 15000.5, "Rojo")
    auto2 = Auto("Honda", "Civic", 2021, 12000.3, "Azul")
    
    print("=== AUTOS INICIALES ===")
    auto1.mostrar_info()
    print()
    auto2.mostrar_info()
    
    
    print("\n=== CAMBIANDO COLORES ===")
    auto1.cambiar_color("Blanco")
    auto2.cambiar_color("Negro")
    
    print("\n=== AUTOS DESPUÉS DEL CAMBIO DE COLOR ===")
    auto1.mostrar_info()
    print()
    auto2.mostrar_info()