import tkinter as tk
from tkinter import ttk,Label,Entry,Button

class Frame6(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        Label(self, text='Sismo', bg='lavender', fg='VioletRed1', font=('Arial', 12, 'bold')).pack(side='top', anchor='nw', padx=5, pady=5)
        #acá
        self.combobox_sismos = ttk.Combobox(self, values=[], justify='center', width=12, font='Arial')
        self.combobox_sismos.pack(side='top', anchor='nw', padx=5, pady=5)
        #Acá
        enviar_sismo = Button(self, text='Enviar', font=('arial', 12, 'bold'), width=15, bg='pink', fg='black',command=lambda: self.grafica2.actualizar_grafica(self.combobox_sismos.get(),self.canvas2))
        enviar_sismo.pack(side="top", anchor="nw", padx=5, pady=5)