
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from app.views.grafica import Grafica
import collections


class Frame0(tk.Frame):
    datos_señal1 = collections.deque([0.0] * 100, maxlen=100)
    datos_señal2 = collections.deque([0.0] * 100, maxlen=100)
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()
    
    
    
    def create_widgets(self):
        grafica1 = Grafica("grafica desplazamiento vs tiempo", muestra=100, ejey=10, datos_señal1=self.datos_señal1, datos_señal2=self.datos_señal2)# instancia objeto grafica
        canvas = FigureCanvasTkAgg(grafica1.fig, master=self)#contenedor con primera gráfica
        canvas.get_tk_widget().pack(padx=0, pady=0, expand=True, fill='both')
    
        
