from machine import Pin, SoftI2C
from time import sleep
import ssd1306

# Definimos el número de pin para el sensor KY
pin_ky = 4

# Configuramos el pin del sensor KY como entrada digital
ky = Pin(pin_ky, Pin.IN)

# Declaramos un objeto con los pines utilizados para la interfaz I2C
i2c = SoftI2C(sda=Pin(21), scl=Pin(22))

# Declaramos objeto de display OLED
display = ssd1306.SSD1306_I2C(128, 64, i2c)

while True:
    # Leemos el valor digital del sensor KY
    valor = ky.value()

    # Limpiamos el display
    display.fill(0)

    if valor == 1:  # Si no hay obstáculo
        display.text("Despejado :3", 0, 0)  # Imprime "Libre" en el display
    else:  # Si hay un obstáculo
        display.text("Obstaculo!!", 0, 0)  # Imprime "Obstáculo" en el display

    # Mostramos el mensaje en el display
    display.show()

    sleep(0.5)  # Espera 0.5 segundos antes de realizar nuevamente el proceso
