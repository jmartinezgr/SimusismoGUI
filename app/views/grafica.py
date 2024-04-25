from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, Entry
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from ..models.lectura_archivos import LectorArchivoAT2


class Grafica:
    """
    Clase para gestionar la creación y actualización de gráficas en tiempo real.

    Attributes:
        titulo (str): El título de la gráfica.
        muestra (int): El número de muestras a mostrar en la gráfica.
        ejey (int): El límite del eje y de la gráfica.
        datos_señal1 (collections.deque): Cola para los datos de la señal 1.
        datos_señal2 (collections.deque): Cola para los datos de la señal 2.
        fig (matplotlib.figure.Figure): La figura de la gráfica.
        ax (matplotlib.axes.Axes): Los ejes de la gráfica.
        line (matplotlib.lines.Line2D): La línea de la señal 1 en la gráfica.
        line2 (matplotlib.lines.Line2D): La línea de la señal 2 en la gráfica.
    """
    def __init__(self, titulo: str, muestra: int, ejey: int, datos_señal1=None, datos_señal2=None):
        self.datos_señal1 = datos_señal1
        self.datos_señal2 = datos_señal2 
        self.muestra = muestra
        self.ejey = ejey
        self.titulo = titulo

        self.fig, self.ax = plt.subplots(facecolor="#FF69B4", dpi=100, figsize=(4, 2))
        plt.title(titulo, color="white", size=12, family='Arial')
        self.ax.tick_params(direction='out', length=5, width=2, color="white", grid_color='r', grid_alpha=0.5)
        self.line, = self.ax.plot([], [], color='m', marker='o', linewidth=12, markersize=1, markeredgecolor='m')
        self.line2, = self.ax.plot([], [], color='g', marker='o', linewidth=2, markersize=1, markeredgecolor='g')
        plt.xlim(0, self.muestra)
        plt.ylim(0, self.ejey)
        self.ax.set_facecolor('#6E6D7000')
        for spine in self.ax.spines.values():
            spine.set_color("red")

    def animate(self, dato_arduino):
        """
        Método para actualizar los datos de la gráfica en cada iteración de la animación.

        Args:
            i (int): El índice de la iteración.
        """
        self.datos = dato_arduino
        dato = self.datos.split(",")
        dato1 = float(dato[0])
        dato2 = float(dato[1])
        self.datos_señal1.append(dato1)
        self.datos_señal2.append(dato2)
        self.line.set_data(range(self.muestra), self.datos_señal1)
        self.line2.set_data(range(self.muestra), self.datos_señal2)

    
    def actualizar_grafica(self,nombre,canvas):
        
        aceleracion, tiempo = LectorArchivoAT2.leer_archivo(nombre)
        print(aceleracion)
        print(tiempo)
       
        
        if aceleracion is not None and tiempo is not None:
        
            
            
            self.line3[0].set_data(tiempo,aceleracion )
            self.ax2.set_xlim(0, max(tiempo))
            self.ax2.set_ylim(min(aceleracion), max(aceleracion))
            canvas.draw()
    