import sys
from tkinter import Tk
from app.views.principal_widget.widget_principal import Widget_Principal
sys.path.append(r'D:\Desktop\Interfaz-mesa\codigo_arduino')









if __name__=="__main__":
    
    ventana=Tk()
    ventana.geometry('742x535')
    ventana.config(bg='gray30', bd=4)
    ventana.wm_title("grafica animacion")
    ventana.minsize(width=700,height=400)
    
    app=Widget_Principal(ventana)
    app.mainloop()