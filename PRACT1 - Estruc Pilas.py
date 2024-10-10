import matplotlib.pyplot as plt

class Pila:
    def __init__(self, tamaño=8):
        self.pila = []
        self.tope = 0
        self.tamaño = tamaño
    
    def insertar(self, letra):
        if self.tope < self.tamaño:
            self.pila.append(letra)
            self.tope += 1
            print(f"La letra '{letra}' ha sido insertada en la pila")
        else:
            print("Error: La pila está llena y no se puede insertar")
        self.dibujar_pilas()

    def eliminar(self):
        if self.tope > 0:
            eliminado = self.pila.pop()
            self.tope -= 1
            print(f"La letra '{eliminado}' ha sido eliminada de la pila")
        else:
            print("Error: La pila está vacía y no se puede eliminar")
        self.dibujar_pilas()

    def dibujar_pilas(self):
        plt.figure(figsize=(2, 4))
        plt.barh(range(self.tamaño), [1 if i < self.tope else 0 for i in range(self.tamaño)],
                 color=['blue' if i < self.tope else 'gray' for i in range(self.tamaño)])
        plt.yticks(range(self.tamaño), [f"Posición {i+1}" for i in range(self.tamaño)])
        plt.gca().invert_yaxis()  
        plt.title('Estado de la Pila')
        for i in range(self.tope):
            plt.text(0.5, i, f"{self.pila[i]}", ha='center', va='center', color='white', fontsize=12)
        plt.show()

mi_pila = Pila()

mi_pila.insertar("X")
mi_pila.insertar("Y")
mi_pila.eliminar()  # Z
mi_pila.eliminar()  # T
mi_pila.eliminar()  # U
mi_pila.insertar("V")
mi_pila.insertar("W")
mi_pila.eliminar()  # P
mi_pila.insertar("R")
