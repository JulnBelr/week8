from time import sleep
from pyfirmata2 import Arduino
from lightsensor import LightSensor
board = Arduino("/dev/ttyACM0")
board.samplingOn(50)                       # T = 50 ms
sensor = LightSensor(board, pin=0, n=16)   # window: 16 × 50 ms = 0.8 s
try:
    while True:
        v, a = sensor.latest(), sensor.average()
        if a is not None:
            print(f"latest={v:.3f}   avg={a:.3f}")
        sleep(0.2)
except KeyboardInterrupt:
    board.exit()
