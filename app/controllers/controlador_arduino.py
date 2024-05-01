import serial
from logger import log
import time

class Controlador:
    _arduino = None
    _puerto = None
    _status = "OFF"

    @classmethod
    def _obtener_conexion(cls, puerto: str = None) -> serial.Serial:
        """
        Obtiene una conexión serial al Arduino.

        Args:
            puerto (str, opcional): El puerto serial al que se conectará el Arduino.

        Returns:
            serial.Serial: La conexión serial al Arduino.
        """
        if cls._arduino is None:
            if puerto is None and cls._puerto is None:
                log.error("Error estableciendo la conexión: No se ha definido el puerto del Arduino")
            else:
                try:
                    cls._arduino = serial.Serial(
                        cls._puerto if cls._puerto else puerto,
                        9600
                    )
                    time.sleep(0.1)
                    log.info("Conexión al Arduino exitosa")
                    cls.rutina_inicio()
                    return cls._arduino
                except Exception as e:
                    log.error(f"Ocurrió un error generando la conexión: {e}")
        else:
            return cls._arduino

    @classmethod
    def establecer_puerto(cls, puerto: str) -> None:
        """
        Establece el puerto serial del Arduino.

        Args:
            puerto (str): El puerto serial del Arduino.
        """
        cls._puerto = puerto
        log.info(f"Puerto del Arduino establecido en {puerto}")

    @classmethod
    def enviar_mensaje(cls, mensaje: str) -> None:
        """
        Envía un mensaje al Arduino.

        Args:
            mensaje (str): El mensaje a enviar al Arduino.
        """
        arduino = cls._obtener_conexion()
        if cls._status not in ["OFF","USE"]:
            if arduino:
                try:
                    arduino.write((mensaje+'\n').encode())
                    log.info(f"Mensaje enviado al Arduino: {mensaje}")
                except Exception as e:
                    log.error(f"Error al enviar mensaje al Arduino: {e}")
            else:
                log.error("No hay conexión establecida con el Arduino.")
        else:
            log.error("La conexion no esta disponible para uso")

    @classmethod
    def recibir_mensaje(cls) -> str:
        """
        Recibe un mensaje del Arduino.

        Returns:
            str: El mensaje recibido del Arduino.
        """
        arduino = cls._obtener_conexion()
        if cls._status not in ["OFF","WA"]:
            if arduino:
                try:
                    mensaje_recibido = arduino.readline().decode().strip()
                    log.info(f"Mensaje recibido del Arduino: {mensaje_recibido}")
                    return mensaje_recibido
                except Exception as e:
                    log.error(f"Error al recibir mensaje del Arduino: {e}")
            else:
                log.error("No hay conexión establecida con el Arduino.")
        else:
            log.error("La conexion no esta disponible para uso")
    
    @classmethod
    def rutina_inicio(cls) -> None:
        """
        Realiza una secuencia de inicialización al establecer la conexión con el Arduino.

        La rutina de inicio establece la conexión con el Arduino, envía un mensaje de inicio,
        y espera la respuesta del Arduino para cambiar el estado a "ON" si la respuesta es la
        esperada "Esperando Respuesta".

        """
        # Inicializa el estado como "STARTING" para indicar que la rutina de inicio está en progreso.
        cls._status = "STARTING"
        
        # Verifica si hay una conexión establecida con el Arduino.
        if cls._arduino:
            # Recibe el primer mensaje del Arduino.
            estado = cls.recibir_mensaje()
            
            # Si el primer mensaje es "Arduino ... OK", continúa con la secuencia de inicio.
            if estado == "Arduino ... OK":
                # Envía un mensaje al Arduino.
                cls.enviar_mensaje("Python ... OK")
                
                # Espera la respuesta del Arduino después de enviar el mensaje.
                estado = cls.recibir_mensaje()
                
                # Si la respuesta es la esperada "Esperando Respuesta", cambia el estado a "ON".
                if estado == "Esperando Respuesta":
                    cls._status = "ON"
                    log.info(f"Estatus del arduino: {cls._status}")
        else:
            # Si no hay conexión establecida con el Arduino, intenta establecerla.
            cls._obtener_conexion()

if __name__ == "__main__":
    Controlador.establecer_puerto("COM3")
    Controlador.enviar_mensaje("M-0.434")