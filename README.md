# Simulación Sísmica - Mesa Vibratoria

Este repositorio contiene el código fuente para la mesa de simulación sísmica desarrollada como parte de un proyecto de integración de software y hardware. El sistema combina el control de una mesa vibratoria a través de un [Arduino](https://www.arduino.cc/) y una interfaz gráfica desarrollada en Python utilizando [Tkinter](https://docs.python.org/3/library/tkinter.html), [PySerial](https://pyserial.readthedocs.io/en/latest/), y otras librerías como [Matplotlib](https://matplotlib.org/) y [NumPy](https://numpy.org/) para la visualización y análisis de datos en tiempo real. También se utiliza [asyncio](https://docs.python.org/3/library/asyncio.html) para la programación asincrónica y manejo de tareas concurrentes.

## Descripción del Proyecto

El objetivo del proyecto es ofrecer una plataforma que permita simular y analizar datos sísmicos utilizando una mesa vibratoria controlada mediante un Arduino. La interfaz gráfica facilita la interacción con el sistema, permitiendo cargar datos de sismos, visualizar gráficas teóricas y en tiempo real, y controlar el movimiento de la mesa.

## Tecnologías Utilizadas

- **Arduino**: Controla los movimientos de la mesa y recopila datos de los sensores en tiempo real.
- **Python**: Lenguaje de programación para la interfaz gráfica y el procesamiento de datos.
- **[Tkinter](https://docs.python.org/3/library/tkinter.html)**: Para el desarrollo de la interfaz gráfica (GUI).
- **[PySerial](https://pyserial.readthedocs.io/en/latest/)**: Para la comunicación serial con el Arduino.
- **[Matplotlib](https://matplotlib.org/)**: Para la visualización de datos en gráficos.
- **[NumPy](https://numpy.org/)**: Para el manejo y procesamiento de datos numéricos.
- **[asyncio](https://docs.python.org/3/library/asyncio.html)**: Para la programación asincrónica y manejo de tareas concurrentes.

## Funcionalidades Principales

- **Conexión al Arduino**: Selección de puerto y configuración de parámetros de comunicación como el baud rate.
- **Carga de Datos**: Posibilidad de cargar archivos con datos de sismos en formato `.txt`, que contienen variables como desplazamiento, velocidad o aceleración.
- **Visualización Gráfica**:
  - **Gráfica Teórica**: Muestra el comportamiento esperado de los datos proporcionados por el usuario, lo cual guía los comandos enviados al Arduino.
  - **Gráfica en Tiempo Real**: Visualiza los resultados de la simulación ejecutada en la mesa vibratoria, reflejando en tiempo real el comportamiento del sistema.
- **Control de Simulación**: Permite iniciar, pausar y detener la simulación directamente desde la interfaz.
