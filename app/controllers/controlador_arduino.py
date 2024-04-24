import serial,time
from logger import log

class Controlador:
    _arduino = None
    _puerto = None

    @classmethod
    def _obtener_conexion(cls, puerto=None):
        if cls._arduino is None:
            if puerto is None and cls._puerto is None:
                log.error("Error estableciendo la conexión: No se ha definido el puerto del Arduino")
            else:
                try:
                    cls._arduino = serial.Serial(
                        cls._puerto if cls._puerto else puerto,
                        9600
                    )
                    log.info("Conexión al Arduino exitosa")
                    return cls._arduino
                except Exception as e:
                    log.error(f"Ocurrió un error generando la conexión: {e}")
        else:
            return cls._arduino

    @classmethod
    def establecer_puerto(cls, puerto):
        cls._puerto = puerto
        log.info(f"Puerto del Arduino establecido en {puerto}")

    @classmethod
    def enviar_mensaje(cls, mensaje):
        arduino = cls._obtener_conexion()
        if arduino:
            try:
                arduino.write(mensaje.encode())
                log.info(f"Mensaje enviado al Arduino: {mensaje}")
            except Exception as e:
                log.error(f"Error al enviar mensaje al Arduino: {e}")
        else:
            log.error("No hay conexión establecida con el Arduino.")

    @classmethod
    def recibir_mensaje(cls):
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
