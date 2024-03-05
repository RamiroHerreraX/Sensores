# Obtenemos el modulo para el display
import ssd1306
# Obtenemos el modulo para el display
from machine import Pin, SoftI2C
from time import sleep

# Librería que permite trabajar con el sensor
import dht

# Declaro la instancia del sensor (cambiamos a DHT11)
sensor = dht.DHT11(Pin(15))

# Declaramos un objeto con los pines utilizados para la interfaz i2c
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Función para limpiar el display y mostrar los valores de temperatura y humedad
def show_temp_humidity():
    display.fill(0)
    # Llamamos a la función de medición del sensor
    sensor.measure()
    # Obtenemos los valores de temperatura y humedad
    t = sensor.temperature()
    h = sensor.humidity()
    # Mostramos los valores en el display
    display.text("Temp: %dC" % t, 0, 0, 1)
    display.text("Hum: %d%%" % h, 0, 20, 1)
    display.show()

# Mostrar los valores de temperatura y humedad en el display una vez al inicio
show_temp_humidity()

while True:
    # Mostrar los valores de temperatura y humedad en el display
    show_temp_humidity()
    # Esperar 5 segundos antes de la próxima lectura
    sleep(5)
