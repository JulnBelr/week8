from pyfirmata2 import Arduino
from time import sleep

board = Arduino("/dev/ttyACM0")   # or Arduino(Arduino.AUTODETECT)
led = board.get_pin("d:13:o")     # digital, pin 13, output

try:
    while True:
        led.write(1)
        sleep(0.5)
        led.write(0)
        sleep(0.5)
except KeyboardInterrupt:
    led.write(0)
    board.exit()
