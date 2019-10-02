import sys
from time import sleep
import Adafruit_DHT
import os

pin = 4
delay = 2
sensor_type = 11


        
print("Realizando Leitura")

try:
    def clear():
        os.system("cls" if os.name == "nt" else "clear")
            
    while True:

        sleep(delay)

        humidity, temperature = Adafruit_DHT.read_retry(sensor_type, pin)

        if humidity is not None and temperature is not None:
            clear()
            print("Temperatura atual: %s °C" % (temperature))
            print("Umidade do ar: %s " % (humidity))
        else:
            print('Cannot read')

except KeyboardInterrupt:
    sys.exit()

