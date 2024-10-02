import tkinter as tk
from tkinter import ttk,Label,Entry,Button

class Frame2(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        Label(self, text='Amplitud:', font=('arial', 12, ), bg='lavender', fg='#000').pack(pady=5, expand=1)
        amplitud_entry = Entry(self, font=('arial', 12,))
        amplitud_entry.pack(pady=5, expand=1)

        Label(self, text='Velocidad:', font=('arial', 12, ), bg='lavender', fg='#000').pack(pady=5, expand=1)
        velocidad_entry = Entry(self, font=('arial', 12))
        velocidad_entry.pack(pady=5, expand=1)

        bt_enviar_amplitud = Button(self, text='Enviar Amplitud', font=('arial', 12, ), width=15, bg='pink', fg='black', command=self.dato_amplitud)
        bt_enviar_amplitud.pack(pady=5, expand=1)

        bt_enviar_velocidad = Button(self, text='Enviar Velocidad', font=('arial', 12, ), width=15, bg='pink', fg='black', command=self.dato_velocidad)
        bt_enviar_velocidad.pack(pady=5, expand=1)
        
    def dato_velocidad(self):
        pass
    def dato_amplitud(self):
        pass