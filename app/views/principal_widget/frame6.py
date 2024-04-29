import tkinter as tk
from tkinter import ttk,Label,Entry,Button
from...models.gestor_archivos.gestor_archivos import Gestor

class Frame6(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        Label(self, text='Tipo de datos', bg='lavender', fg='VioletRed1', font=('Arial', 12, 'bold')).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.combobox_sismos = ttk.Combobox(self, values=Gestor.subcarpetas, justify='center', width=12, font='Arial')
        self.combobox_sismos.grid(row=1, column=0, sticky='w', padx=5, pady=5)

    # Nuevo Label y Combobox a la derecha
        Label(self, text='Seleccion archivo', bg='lavender', fg='VioletRed1', font=('Arial', 12, 'bold')).grid(row=0, column=1, sticky='w', padx=5, pady=5)
        self.combobox_nuevo = ttk.Combobox(self,state="disabled",values=[], justify='center', width=12, font='Arial')
        self.combobox_nuevo.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    # Botón de enviar
        enviar_sismo = Button(self, text='Enviar', font=('arial', 12, 'bold'), width=15, bg='pink', fg='black', command=lambda: self.grafica2.actualizar_grafica(self.combobox_sismos.get(), self.canvas2))
        enviar_sismo.grid(row=2, column=0, columnspan=2, sticky='w', padx=5, pady=5)
        
    # manejo eventos 
        self.combobox_sismos.bind('<<ComboboxSelected>>', lambda event: self.habilitar_combobox())

    
    
    
    def habilitar_combobox(self):
        if self.combobox_sismos.get():  # Verifica si hay una selección en el primer combobox
            self.combobox_nuevo['state'] = 'readonly'# Habilita el segundo combobox
            self.combobox_nuevo.set('') 
            self.actualizar_combobox2()
        else:
            self.combobox_nuevo['state'] = 'disabled'  # Deshabilita el segundo combobox
    def actualizar_combobox2(self):
        carpeta_seleccionada = self.combobox_sismos.get()
        print("holaaaaaaaaaaaaaaaaaaaaaaaaaaaa", carpeta_seleccionada)
        archivos_asociados = Gestor.archivos_asociados(carpeta_seleccionada)
        self.combobox_nuevo['values'] = archivos_asociados
