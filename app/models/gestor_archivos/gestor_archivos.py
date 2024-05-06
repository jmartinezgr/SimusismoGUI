import os
from tkinter import filedialog, messagebox
import shutil 
class Gestor:
    subcarpetas = os.listdir("data/datos_sismicos")
    
    def __init__(self):
        try:
            print(self.subcarpetas)
            print("hola")
            self.archivos_asociados("datos_aceleracion")
            print(Gestor.generar_ruta("datos_aceleracion","RSN1101_KOBE_AMA000.AT2"))
            
        except FileNotFoundError as e:
            print(f"Error: {e}")
    @staticmethod
    def archivos_asociados(carpeta)->list[str]:
        try:
            ruta_carpeta = os.path.join("data", "datos_sismicos", carpeta)
            lista_archivos = os.listdir(ruta_carpeta)
            print(lista_archivos)
            return lista_archivos
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return []
    @classmethod
    def generar_ruta(cls, carpeta, archivo=None)->str:
        try:
            ruta_carpeta = os.path.join("data", "datos_sismicos", carpeta)
            if archivo:
                ruta_completa = os.path.join(ruta_carpeta, archivo)
                return ruta_completa
            else:
                return ruta_carpeta
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return ""
    @classmethod
    def subir_archivo(cls):
        archivo_seleccionado = filedialog.askopenfilename()
        if archivo_seleccionado:
            ruta_destino = None

            try:
                nombre_archivo, extension = os.path.splitext(os.path.basename(archivo_seleccionado))
                if extension == ".VT2" or extension == ".AT2":
                    ruta_destino = Gestor.generar_ruta("datos_velocidad")
                elif extension == ".DT2":
                    ruta_destino = Gestor.generar_ruta("datos_desplazamiento")
                elif extension == ".AT2":
                    ruta_destino = Gestor.generar_ruta("datos_aceleracion")
                else:
                    raise ValueError("Extensión de archivo no válida")

                nueva_ruta = os.path.join(ruta_destino, nombre_archivo)
                shutil.copy2(archivo_seleccionado, nueva_ruta)
                print("Archivo seleccionado:", archivo_seleccionado)
            except ValueError as e:
                # Manejo de la excepción cuando se selecciona un archivo con extensión no válida
                print("Error:", e)
                messagebox.showerror("Error", "Archivo no válido: solo se admiten archivos .AT2, .VT2, o .DT2")
                

        
        
        
    
    
    
    