import tkinter as tk
from tkinter import ttk,Label,Button,filedialog
from...models.gestor_archivos.gestor_archivos import Gestor
from...controllers.lectura_archivos import LectorArchivoAT2
from..grafica import Grafica
from.frame5 import Frame5



class Frame6(tk.Frame):
    grafica=None
    
    
    
   
    
    
    def __init__(self, intancia_frame5=None, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()
        self.instancia_frame5=intancia_frame5
        
        

    def create_widgets(self):
        Label(self, text='Tipo de datos', bg='lavender', fg='#000', font=('Arial', 12, )).grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.combobox_sismos = ttk.Combobox(self, values=Gestor.subcarpetas, justify='center', width=12, font='Arial')
        self.combobox_sismos.grid(row=1, column=0, sticky='w', padx=5, pady=5)

    # Nuevo Label y Combobox a la derecha
        Label(self, text='Seleccion archivo', bg='lavender', fg='#000', font=('Arial', 12, )).grid(row=0, column=1, sticky='w', padx=5, pady=5)
        self.combobox_nuevo = ttk.Combobox(self,state="disabled",values=[], justify='center', width=12, font='Arial')
        self.combobox_nuevo.grid(row=1, column=1, sticky='w', padx=5, pady=5)

    # Botón de enviar
        enviar_sismo = Button(self, 
                      text='Enviar', 
                      font=('arial', 12, ), 
                      width=15, 
                      bg='pink', 
                      fg='black', 
                      command=lambda: self.obtener_sismos(self.combobox_sismos.get(), self.combobox_nuevo.get()))
        enviar_sismo.grid(row=2, column=0, columnspan=2, sticky='w', padx=5, pady=5)
    
        num_filas_adicionales = 5

# Agregar filas adicionales con pesos asignados
        for i in range(num_filas_adicionales):
            self.grid_columnconfigure(3 + i, weight=1)
    # Boton subida archivo
        boton_subir_archivo = tk.Button(self, text="Subir Archivos", command= Gestor.subir_archivo)
       
        boton_subir_archivo.grid(row=0, column=7, columnspan=20, sticky='e') 
        
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
        
    def obtener_sismos(self, carpeta, archivo):
        ruta=Gestor.generar_ruta(carpeta, archivo)
        ejex, ejey = LectorArchivoAT2.leer_archivo(ruta)
        self.instancia_frame5.actualizar_canvas(ejey, ejex)
        
    
        
        
        #self.grafica.actualizar_grafica(ejey, ejex)
        
        
        
