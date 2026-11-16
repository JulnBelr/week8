from time import sleep
from pyfirmata2 import Arduino
from lightsensor import LightSensor
board = Arduino("/dev/ttyACM0")
board.samplingOn(50)
sensor = LightSensor(board, pin=0, n=1)    # n=1 raw; 16 smooth (rung 2)
led = board.get_pin("d:9:p")
try:
    while True:
        v = sensor.latest()
        if v is not None:
            led.write(v)                   # bright room, bright LED
        sleep(0.05)
except KeyboardInterrupt:
    led.write(0)
    board.exit()
