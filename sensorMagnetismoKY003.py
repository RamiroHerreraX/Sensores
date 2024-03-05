from machine import Pin
from time import sleep
import network
from umqtt.simple import MQTTClient

pin_sensor = Pin(14, Pin.IN)

MQTT_BROKER = "192.168.43.135"
MQTT_USER = ""
MQTT_PASSWORD = ""
MQTT_CLIENT_ID = ""
MQTT_TOPIC = "utng/ahn/photoresistor"
MQTT_PORT = 1883

def conectar_wifi():
    print("Conectando...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Adrian', '123456ad')
    while not sta_if.isconnected():
        print(".", end="")
        sleep(0.3)
    print("WiFi Conectada!")

def publicar_mensaje(msg):
    client.publish(MQTT_TOPIC, msg)

def verificar_magnetismo():
    while True:
        estado = pin_sensor.value()
        if estado == 1:
            publicar_mensaje(b'true')
            sleep(15)
        else:
            publicar_mensaje(b'false')
            sleep(15)

conectar_wifi()
client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, port=MQTT_PORT, user=MQTT_USER, password=MQTT_PASSWORD, keepalive=0)
client.connect()

verificar_magnetismo()
