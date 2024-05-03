import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Frame5(tk.Frame):
    
   
    def __init__(self, instancia_grafica, master=None):
        super().__init__(master)
        self._instancia_grafica = instancia_grafica
        self.configure(bg='lavender')
        
        
        # Crear el canvas como un atributo de la clase
        self.canvas2 = FigureCanvasTkAgg(self._instancia_grafica.fig, master=self)
        self.canvas2.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')
        self.instancia_unica=self
    
    
    
    
      
    def actualizar_canvas( self, aceleracion, tiempo )->None:
        # Borra la gráfica actual del canvas
        """self.canvas2.get_tk_widget().destroy()
        
        # Crea un nuevo canvas con la nueva gráfica
        self.canvas2 = FigureCanvasTkAgg(nueva_grafica.fig, master=self)
        self.canvas2.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')
        """
        self._instancia_grafica.actualizar_grafica(aceleracion,tiempo)
        self.canvas2.draw()
    
    
    @staticmethod
    def obtener_instancia_grafica():
        return Frame5._instancia_grafica
    @staticmethod
    def actualizar_instancia_grafica( nueva_instancia_grafica):
        Frame5._instancia_grafica = nueva_instancia_grafica
        
    

    
    
   
        
        
        