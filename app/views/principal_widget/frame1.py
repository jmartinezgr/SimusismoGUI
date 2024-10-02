# frame1.py

import tkinter as tk
from tkinter import ttk,Label,Button
from ...controllers.controlador_arduino import Controlador as cl

class Frame1(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        Label(self, text='Puertos Entrada', bg='lavender', fg='#000', font=('Arial',12)).pack(padx=5,expand=1)
        
        self.combobox_port=ttk.Combobox(self, values=cl.get_puerto, justify='center', width=12, font='Arial' )
        self.combobox_port.pack(pady=0, expand=1)
        #self.combobox_port.current(0)
        Label(self,text='Braudates', bg='lavender', fg='#000', font=('Arial',12)).pack(pady=0,expand=1)
        self.combobox_baud=ttk.Combobox(self, values=[], justify='center',width=12, font='Arial')
        self.combobox_baud.pack(padx=20, expand=1)
        
        
        
        self.bt_conectar=Button(self, text='conectar', font=('Arial', 12), width=12, bg='pink', command=self.conectar_serial)
        
        self.bt_conectar.pack(pady=5,expand=1)
       
        self.bt_actualizar=Button(self, text='actualizar', font=('Arial',12),width=12,bg='pink', command=self.actualizar_puertos)
       
        self.bt_actualizar.pack(pady=5,expand=1)
        
        self.bt_desconectar=Button(self, text='desconectar', font=('Arial',12), width=12,bg='pink', command=self.desconectar_serial )
        
        self.bt_desconectar.pack(pady=5,expand=1)
        
        
    def conectar_serial(self):
        pass
    def desconectar_serial(self):
        pass
    def actualizar_puertos(self):
        pass
        """
        se dejan vacíos estos metodos por ahora mientras se actualiza
        la clase comunicación
        """
        
        
        
        
