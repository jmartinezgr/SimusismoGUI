import os
from pathlib import Path
import numpy as np

class LectorArchivoAT2:
   
   
    def __init__(self) -> None:
        pass
        
        
    
    
    


    @classmethod
    def leer_archivo(self,ruta_archivo)->None:
        ruta=Path(ruta_archivo)
        
        if ruta.exists():
            # Usar np.genfromtxt para cargar los datos directamente
            datos = np.genfromtxt(ruta, skip_header=4)
            ejey = datos.flatten()
            npts = len(ejey)
            ejex = self._calcular_ejex(npts)
            return  ejex,ejey
        else:
            print("El archivo no existe")
            return None
        
            
    @classmethod    
    def _calcular_ejex(self, npts, dt=0.001):
        return np.arange(0, npts * dt, dt)
        



