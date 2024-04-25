import os
from pathlib import Path
import numpy as np

class LectorArchivoAT2:
    def __init__(self):
        self.carpeta_base = Path('archivos_sismos')
        self.sub_carpetas = []
        self.archivos = []
        self.obtener_subcarpetas
        self.obtener_archivos

    def obtener_subcarpetas(self):
        self.sub_carpetas = [subcarpeta.name for subcarpeta in self.carpeta_base.iterdir() if subcarpeta.is_dir()]

    def obtener_archivos(self, subcarpeta):
        ruta_subcarpeta = self.carpeta_base / subcarpeta
        self.archivos = [archivo.name for archivo in ruta_subcarpeta.iterdir() if archivo.is_file()]

    def leer_archivo(self, subcarpeta, nombre_archivo):
        ruta_archivo = self.carpeta_base / subcarpeta / nombre_archivo
        if ruta_archivo.exists():
            # Usar np.genfromtxt para cargar los datos directamente
            datos = np.genfromtxt(ruta_archivo, skip_header=4)
            aceleracion = datos.flatten()
            npts = len(aceleracion)
            tiempo = self._calcular_ejex(npts)
            return aceleracion, tiempo

    def _calcular_ejex(self, npts, dt=0.001):
        return np.arange(0, npts * dt, dt)

        
        
        

    



