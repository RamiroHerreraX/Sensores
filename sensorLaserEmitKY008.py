from machine import Pin, SoftI2C
from time import sleep
import ssd1306

# Definimos el número de pin para el láser
pin_laser = 4

# Configuramos el pin del láser como salida digital
laser = Pin(pin_laser, Pin.OUT)

# Declaramos un objeto con los pines utilizados para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

# Bucle principal
while True:
    # Encendemos el láser
    laser.on()
    sleep(0.2)  # Esperamos 200ms
    # Limpiamos el display
    display.fill(0)
    # Mostramos el mensaje correspondiente en el display
    display.text("Laser encendido", 0, 0)
    display.show()
    sleep(1)  # Esperamos 1 segundo antes de apagar el láser

    # Apagamos el láser
    laser.off()
    sleep(0.2)  # Esperamos 200ms
    # Limpiamos el display
    display.fill(0)
    # Mostramos el mensaje correspondiente en el display
    display.text("Laser apagado", 0, 0)
    display.show()
    sleep(1)  # Esperamos 1 segundo antes de encender el láser
