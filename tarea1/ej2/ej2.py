class Computadora:
    def __init__(self, marca, modelo, memoria_ram=8, capacidad_almacenamiento=512):
        """
        Constructor de la clase Computadora
        Puede recibir 2 o 4 parámetros
        """
        self.marca = marca
        self.modelo = modelo
        self.memoria_ram = memoria_ram  
        self.capacidad_almacenamiento = capacidad_almacenamiento  
    
    def ram_es_igual_a(self, x):
        """
        Determina si la cantidad de memoria RAM es igual a X
        """
        return self.memoria_ram == x
    
    def mostrar_datos(self):
        """
        Muestra los datos de la computadora
        """
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Memoria RAM:", self.memoria_ram, "GB")
        print("Capacidad de almacenamiento:", self.capacidad_almacenamiento, "GB")
    
    def get_capacidad_almacenamiento(self):
        return self.capacidad_almacenamiento



if __name__ == "__main__":
 
    comp1 = Computadora("Dell", "XPS 13")  
    comp2 = Computadora("HP", "Pavilion", 16, 1024)  
    
    print("=== COMPUTADORA 1 ===")
    comp1.mostrar_datos()
    print("\n¿RAM es igual a 8?", comp1.ram_es_igual_a(8))
    print("¿RAM es igual a 16?", comp1.ram_es_igual_a(16))
    
    print("\n=== COMPUTADORA 2 ===")
    comp2.mostrar_datos()
    print("\n¿RAM es igual a 8?", comp2.ram_es_igual_a(8))
    print("¿RAM es igual a 16?", comp2.ram_es_igual_a(16))
    

    print("\n=== COMPUTADORA CON MAYOR CAPACIDAD ===")
    if comp1.get_capacidad_almacenamiento() > comp2.get_capacidad_almacenamiento():
        comp1.mostrar_datos()
    elif comp2.get_capacidad_almacenamiento() > comp1.get_capacidad_almacenamiento():
        comp2.mostrar_datos()
    else:
        print("Ambas computadoras tienen la misma capacidad de almacenamiento")