import os

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
    def generar_ruta(cls, carpeta, archivo)->str:
        try:
            ruta_carpeta = os.path.join("data", "datos_sismicos", carpeta)
            ruta_completa = os.path.join(ruta_carpeta, archivo)
            return ruta_completa
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return ""

        
        
        
    
    
    
    