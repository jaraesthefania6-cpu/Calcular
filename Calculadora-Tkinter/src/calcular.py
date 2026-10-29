import tkinter as tk

class Calculadora:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Calculadora")

        self.operacion = ""

        # Textbox (Pantalla de visualización)
        self.pantalla = tk.Entry(ventana, font=("Arial", 18), justify="right")
        self.pantalla.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Matriz de 4x4 con números y operaciones
        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)
        ]

        # Crear los botones en la cuadrícula
        for (texto, fila, col) in botones:
            if texto == "=":
                btn = tk.Button(ventana, text=texto, width=5, height=2, command=self.calcular)
            elif texto == "C":
                btn = tk.Button(ventana, text=texto, width=5, height=2, command=self.limpiar)
            else:
                btn = tk.Button(ventana, text=texto, width=5, height=2, command=lambda t=texto: self.agregar(t))
            
            btn.grid(row=fila, column=col, padx=2, pady=2)

    def agregar(self, valor):
        self.operacion += str(valor)
        self.pantalla.delete(0, tk.END)
        self.pantalla.insert(0, self.operacion)

    def limpiar(self):
        self.operacion = ""
        self.pantalla.delete(0, tk.END)

    def calcular(self):
        try:
            resultado = str(eval(self.operacion))
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, resultado)
            self.operacion = resultado
        except Exception:
            self.pantalla.delete(0, tk.END)
            self.pantalla.insert(0, "Error")
            self.operacion = ""

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculadora(root)
    root.mainloop()