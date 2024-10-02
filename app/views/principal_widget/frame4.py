import tkinter as tk
from tkinter import ttk,Label,Entry,Button

class Frame4(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        bt_graficar = Button(self, text='graficar', font=('arial', 12, ), width=12, bg='pink', fg='black', command=self.iniciar)
        bt_graficar.pack(pady=5, expand=1)
        bt_pausar = Button(self, state='disabled', text='pausar', font=('arial', 12, ), width=12, bg='pink', fg='black', command=self.pausar)
        bt_pausar.pack(pady=5, expand=1)

        bt_reanudar = Button(self, state='disabled', text=' reanudar', font=('arial', 12, ), width=12, bg='pink', fg='light blue', command=self.reanudar)
        bt_reanudar.pack(pady=5, expand=1)
        
    def iniciar(self):
        pass
    def pausar(self):
        pass
    def reanudar(self):
        pass
       