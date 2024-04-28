import os

class Gestor:
    subcarpetas = os.listdir("data/datos_sismicos")
    
    def __init__(self):
        try:
            print(self.subcarpetas)
            print("hola")
            self.archivos_asociados("datos_aceleracion")
            
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def archivos_asociados(self, carpeta)->list[str]:
        try:
            ruta_carpeta = os.path.join("data", "datos_sismicos", carpeta)
            lista_archivos = os.listdir(ruta_carpeta)
            print(lista_archivos)
            return lista_archivos
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return []

    def generar_ruta(self, carpeta, archivo)->str:
        try:
            ruta_carpeta = os.path.join("data", "datos_sismicos", carpeta)
            ruta_completa = os.path.join(ruta_carpeta, archivo)
            return ruta_completa
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return ""

        
        
        
    
    
    
    