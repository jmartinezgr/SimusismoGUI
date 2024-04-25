import serial
import serial.tools.list_ports
from threading import Thread, Event
from tkinter import StringVar
import sys
sys.path.append(r'd:\Desktop\Interfaz-mesa\codigo_arduino')


class Comunicacion:
    baudrates = ['1200', '2400', '4800', '9600', '19200', '38400', '115200']
    puertos = []
    def __init__(self, *args):
        """
        Inicializa la clase de comunicación.

        Args:
        *args: Argumentos múltiples para pasar al inicializador.
        """
        super().__init__(*args)
        self.datos_recibidos = StringVar()# variable que permite actualización directa en la interfaz en tkinter 
        self.arduino = serial.Serial()
        self.arduino.timeout = 0.5
        
        
        self.señal = Event()
        self.hilo = None

    def puertos_disponibles(self):
        """
        Obtiene una lista de puertos COM disponibles.
        Esta función utiliza la librería serial.tools.list_ports para detectar los puertos COM disponibles en el sistema.
        Retorna una lista de nombres de los puertos COM, que pueden ser utilizados para la conexión serial.
    
        """
        self.puertos = [port.device for port in serial.tools.list_ports.comports()]

    def conexion_serial(self):
        """
        Establece la conexión serial con Arduino.
        """
        try:
            self.arduino.open()
        except Exception as e:
            print(f"Error al conectar con Arduino: {e}")
        else:
            if self.arduino.is_open:
                self.iniciar_hilo()
                print("Conectado")

    def enviar_datos(self, data):
        """
        Envía datos al dispositivo conectado por el puerto serial.

        Args:
        data: Los datos a enviar.
        """
        if self.arduino.is_open:
            self.dato = str(data) + "/n"
            self.arduino.write(self.dato.encode())
        else:
            print("Error, no se ha conectado con Arduino")

    def leer_datos(self):
        """
        Lee los datos recibidos del dispositivo conectado por el puerto serial.
        """
        try:
            while self.señal.isSet() and self.arduino.is_open:
                data = self.arduino.readline().decode("utf-8").strip()
                if len(data) > 1:
                    self.datos_recibidos.set(data)#cambio de valor de dato recibido que se pondrá en la gráfica
        except TypeError:
            pass

    def iniciar_hilo(self):
        """
        Inicia un hilo para leer los datos en paralelo.
        """
        self.hilo = Thread(target=self.leer_datos)
        self.hilo.setDaemon(1)# se utiliza este tipo de hilo para que se ejecute en un segundo plano y finalice con el programa 
        self.señal.set()
        self.hilo.start()

    def stop_hilo(self):
        """
        Detiene el hilo de lectura de datos.
        """
        if self.hilo is not None:
            self.señal.clear()
            self.hilo.join()# este metodo se utiliza para esperar a que algun hilo termine de ejecutar antes de continuar con el principal 
            self.hilo = None

    def desconectar(self):
        """
        Cierra la conexión serial y detiene el hilo.
        """
        self.arduino.close()
        self.stop_hilo()
   