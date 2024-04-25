import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.views.grafica import Grafica

class Frame5(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        grafica2 = Grafica("grafica desplazamiento vs tiempo", muestra=100, ejey=10)
        
        
        self.canvas2 = FigureCanvasTkAgg(grafica2.fig, master=self)#contenedor con segunda gráfica
        self.canvas2.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')