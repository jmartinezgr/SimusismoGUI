import os
from pathlib import Path
import numpy as np

class LectorArchivoAT2:
    sub_carpetas=[]
    ruta_archivo="D:\Downloads\proyecto react\SimusismoGUI\data\datos_sismicos\datos_aceleracion\RSN5_NWCALIF.AB_A-FRN045.AT2"
    def __init__(self) -> None:
        self.ejex=[]
        self.ejey=[]
        
    
    
    


    @classmethod
    def leer_archivo(self,ruta_archivo):
        ruta_archivo = self.ruta_archivo
        if ruta_archivo.exists():
            # Usar np.genfromtxt para cargar los datos directamente
            datos = np.genfromtxt(ruta_archivo, skip_header=4)
            self.ejey = datos.flatten()
            npts = len(self.ejey)
            self.ejex = self._calcular_ejex(npts)
            
    @classmethod    
    def _calcular_ejex(self, npts, dt=0.001):
        return np.arange(0, npts * dt, dt)
        



