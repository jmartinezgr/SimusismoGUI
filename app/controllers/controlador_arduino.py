import serial
from logger import log
import time

class Controlador:
    _arduino = None
    _puerto = None
    _status = "OFF"

    @classmethod
    def __obtener_conexion(cls, puerto: str = None) -> serial.Serial:
        """
        Obtiene una conexión serial al Arduino.

        Args:
            puerto (str, opcional): El puerto serial al que se conectará el Arduino.

        Returns:
            serial.Serial: La conexión serial al Arduino.
        """
        # Verifica si ya hay una conexión establecida con el Arduino.
        if cls._arduino is None:
            # Si no hay conexión establecida, intenta establecerla.
            if puerto is None and cls._puerto is None:
                log.error("Error estableciendo la conexión: No se ha definido el puerto del Arduino")
            else:
                try:
                    # Intenta establecer la conexión serial.
                    cls._arduino = serial.Serial(
                        cls._puerto if cls._puerto else puerto,
                        9600
                    )
                    time.sleep(0.1)
                    log.info("Conexión al Arduino exitosa")
                    # Realiza la rutina de inicio después de establecer la conexión.
                    cls._rutina_inicio()
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
        # Intenta obtener la conexión serial con el Arduino.
        arduino = cls.__obtener_conexion()
        # Verifica si el estado de la conexión permite el envío de mensajes.
        if cls._status not in ["OFF","USE"]:
            if arduino:
                cls._status = "USE"
                try:
                    # Envía el mensaje al Arduino y registra el evento.
                    arduino.write((mensaje+'\n').encode())
                    log.info(f"Mensaje enviado al Arduino: {mensaje}")
                except Exception as e:
                    log.error(f"Error al enviar mensaje al Arduino: {e}")
            else:
                log.error("No hay conexión establecida con el Arduino.")
            cls._status = "ON"
        else:
            log.error("La conexión no está disponible para uso")

    @classmethod
    def recibir_mensaje(cls) -> str:
        """
        Recibe un mensaje del Arduino.

        Returns:
            str: El mensaje recibido del Arduino.
        """
        # Intenta obtener la conexión serial con el Arduino.
        arduino = cls.__obtener_conexion()
        # Verifica si el estado de la conexión permite la recepción de mensajes.
        if cls._status not in ["OFF","WA"]:
            if arduino:
                try:
                    cls._status = "WA"
                    # Lee el mensaje recibido del Arduino y registra el evento.
                    mensaje_recibido = arduino.readline().decode().strip()
                    log.info(f"Mensaje recibido del Arduino: {mensaje_recibido}")
                    cls._status = "ON"
                    return mensaje_recibido
                except Exception as e:
                    log.error(f"Error al recibir mensaje del Arduino: {e}")
                    cls._status = "ON"
            else:
                log.error("No hay conexión establecida con el Arduino.")

        else:
            print(cls._status)
            log.error("La conexión no está disponible para uso")
    
    @classmethod
    def _rutina_inicio(cls) -> None:
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
                    log.info(f"Estatus del Arduino: {cls._status}")
        else:
            # Si no hay conexión establecida con el Arduino, intenta establecerla.
            cls.__obtener_conexion()

    @classmethod
    def get_status(cls) -> str:
        """
        Retorna la variable de clase estatus que refleja el estado de la conexión en cualquier
        instancia.
        """
        return cls._status
    
    @classmethod
    def finalizar_conexion(cls):
        """
        Finaliza la conexión con el Arduino.

        Cierra el puerto serial y restablece las variables de clase relacionadas.
        """
        cls._arduino.close()
        log.info(f"Conexión con el Arduino cerrada exitosamente.")
        cls._arduino = None


if __name__ == "__main__":
    Controlador.establecer_puerto("COM3")
    Controlador.enviar_mensaje("PPM")
    Controlador.recibir_mensaje()   
    Controlador.recibir_mensaje()
    if Controlador.recibir_mensaje() == "Preparado":
        for dato in [1,2,3]:
            Controlador.enviar_mensaje(str(dato))