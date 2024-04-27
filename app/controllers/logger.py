import logging as log

log.basicConfig(
    level=log.ERROR,
    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
    datefmt= '%I:%M:%S %p',
    handlers=[
        log.FileHandler("logging.log"),
        log.StreamHandler()
    ]
)

if __name__ == "__main__":
    log.error("Este es un mensaje de error, se mostrará")