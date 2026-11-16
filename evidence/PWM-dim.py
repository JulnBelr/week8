from pyfirmata2 import Arduino
from time import sleep
board = Arduino("/dev/ttyACM0")
led = board.get_pin("d:9:p")
try:
    while True:
        for duty in range(0, 101, 5):
            led.write(duty / 100)
            sleep(0.03)
        for duty in range(100, -1, -5):
            led.write(duty / 100)
            sleep(0.03)
except KeyboardInterrupt:
    led.write(0)
    board.exit()
