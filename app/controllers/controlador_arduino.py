import serial
from logger import log
import time

class Controlador:
    _arduino = None
    _puerto = None

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
        if arduino:
            try:
                arduino.write((mensaje+'\n').encode())
                log.info(f"Mensaje enviado al Arduino: {mensaje}")
            except Exception as e:
                log.error(f"Error al enviar mensaje al Arduino: {e}")
        else:
            log.error("No hay conexión establecida con el Arduino.")

    @classmethod
    def recibir_mensaje(cls) -> str:
        """
        Recibe un mensaje del Arduino.

        Returns:
            str: El mensaje recibido del Arduino.
        """
        arduino = cls._obtener_conexion()
        if arduino:
            try:
                mensaje_recibido = arduino.readline().decode().strip()
                log.info(f"Mensaje recibido del Arduino: {mensaje_recibido}")
                return mensaje_recibido
            except Exception as e:
                log.error(f"Error al recibir mensaje del Arduino: {e}")
        else:
            log.error("No hay conexión establecida con el Arduino.")

if __name__ == "__main__":
    Controlador.establecer_puerto("COM3")
    estado = Controlador.recibir_mensaje()
    if estado == "Arduino ... OK":
        Controlador.enviar_mensaje("Python ... OK")
        estado = Controlador.recibir_mensaje()
        estado = Controlador.recibir_mensaje()
        
