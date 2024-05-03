import os
import sys
sys.path.append(r'D:\Desktop\Interfaz-mesa\codigo_arduino')
from tkinter import Tk, Frame, Button, Label, ttk, PhotoImage, Entry 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#from codigo_arduino import comunicacion
import matplotlib.animation as animation
import tkinter as tk

import collections
from..grafica import Grafica
from...controllers.lectura_archivos import LectorArchivoAT2
from .frame import Frame0
from .frame1 import Frame1
from .frame2 import Frame2
from .frame3 import Frame3
from .frame4 import Frame4
from .frame5 import Frame5
from .frame6 import Frame6







 #Datos archivo
lector=LectorArchivoAT2()
ruta_carpeta = 'D:\Desktop\Interfaz-mesa\archivos_sismos'






class Widget_Principal(Frame):
    
    """Clase que define el widget principal de la interfaz gráfica."""
    datos_señal1 = collections.deque([0.0] * 100, maxlen=100)
    datos_señal2 = collections.deque([0.0] * 100, maxlen=100)
    grafica1 = Grafica("grafica desplazamiento vs tiempo", muestra=100, ejey=10, datos_señal1=datos_señal1, datos_señal2=datos_señal2)# instancia objeto grafica
    grafica2 = Grafica("grafica desplazamiento vs tiempo", muestra=100, ejey=10)
    #lista_archivos = tk.Listbox(Frame)##
    #datos_arduino=comunicacion.Comunicacion()
    #logo = PhotoImage(file="D:\Desktop\Interfaz-mesa\interfaz\logo1.png").subsample(3, 3)

    def __init__(self, master, *args):
        """Inicializa el widget principal."""
        super().__init__(master, *args)
        self.frame=None
        self.frame1=None
        self.frame2=None
        self.frame3=None
        self.frame4=None
        self.frame5=None
        self.frame6=None
        
        
        

        self.widgets()

    def widgets(self):
        """Crea los widgets de la interfaz gráfica."""
        self.frame = Frame0(self.master)
        self.frame.grid(column=0, columnspan=2, row=0, sticky='nsew')
        self.frame1 = Frame1(self.master)
        self.frame1.grid(column=2, row=0, sticky='nsew')
        self.frame4 = Frame4(self.master)
        self.frame4.grid(column=0, row=1, sticky='nsew')
        self.frame2 = Frame2(self.master)
        self.frame2.grid(column=1, row=1, sticky='nsew')
        self.frame3 = Frame3(self.master)
        self.frame3.grid(column=2, row=1, sticky='nsew')
        self.frame5 = Frame5(self.grafica2, self.master)
        self.frame5.grid(column=3, row=0, columnspan=2, sticky='nsew')
        self.frame6 = Frame6(self.frame5,self.master)
        self.frame6.grid(column=3, row=1, columnspan=2, sticky='nsew')

        self.master.columnconfigure(0, weight=2)
        self.master.columnconfigure(1, weight=2)
        self.master.columnconfigure(2, weight=1)
        self.master.columnconfigure(3, weight=2)  # Doble peso para las columnas 3 y 4
        self.master.columnconfigure(4, weight=2)

        self.master.rowconfigure(0, weight=1)
        self.master.rowconfigure(1, weight=1)
        """_summary_
        organización de los frames dentro del widget 
        """
        

# Crear una instancia de la clase Grafica
        
     
        


        #port = self.datos_arduino.puertos# instancia de los puertos disponibles 
        #baud = self.datos_arduino.baudrates# instancia de los baudrates disponibles 

      
        
 
        

    def actualizar_puertos(self):
        """Actualiza los puertos disponibles."""
        self.datos_arduino.puertos_disponibles()

    def conectar_serial(self):
        """Conecta al puerto serial."""
        """"
        self.bt_conectar.config(state='disable')
        self.bt_desconectar.config(state='normal')
        self.bt_graficar.config(state='normal')
        self.bt_reanudar.config(state='disabled')
        

        self.datos_arduino.arduino.port = self.combobox_port.get()
        self.datos_arduino.arduino.baudrate = self.combobox_baud.get()
        self.datos_arduino.conexion_serial()
       """

    def desconectar_serial(self):
        
         """" 
        self.bt_conectar.config(state='normal')
        self.bt_desconectar.config(state='disabled')
        self.slider_uno.config(state='disabled')
        self.slider_dos.config(state='disabled')
        self.bt_pausar.config(state='disabled')

        try:
            self.ani.event_source.stop()
        except AttributeError:
            pass
        self.datos_arduino.desconectar() 
        
        """
        
        
        
    def dato_amplitud(self):
         
        """
        amplitud = '1' + self.amplitud_entry.get()
        self.datos_arduino.enviar_datos(amplitud)
        """
        
        
       
    
    def dato_velocidad(self):
         """"
        velocidad = '2' + self.velocidad_entry.get()
        self.datos_arduino.enviar_datos(velocidad)
        """
        
        
    def iniciar(self):
        """""
        self.ani = animation.FuncAnimation(self.grafica1.fig, self.grafica1.animate(self.datos_arduino.datos_recibidos.get()), interval=100, blit=False)
        self.bt_graficar.config(state='disable')
        self.bt_pausar.config(state='normal')
        self.canvas.draw()
        """ 
        
        
        
        
       

    def pausar(self):
        
        """
        self.ani.event_source.stop()
        self.bt_reanudar.config(state='normal')
        
        """
        

    def reanudar(self):
       
        """"
        self.ani.event_source.start()
        self.bt_reanudar.config(state='disable')
        """
        
        
       