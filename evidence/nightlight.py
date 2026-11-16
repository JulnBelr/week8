from time import sleep
from pyfirmata2 import Arduino
from lightsensor import LightSensor
DARK, BRIGHT = 0.13, 0.90      # your anchors (docs/calibration.md)
LOW, HIGH = 30.0, 40.0         # on below LOW %, off above HIGH %
                               # the gap between them is the point
def light_pct(v):
    return max(0.0, min(100.0, (v - DARK) / (BRIGHT - DARK) * 100))
board = Arduino("/dev/ttyACM0")
board.samplingOn(50)
sensor = LightSensor(board, pin=0, n=8)
led = board.get_pin("d:9:p")
mode = "off"
try:
    while True:
        a = sensor.average()
        if a is not None:
            pct = light_pct(a)
            if mode == "off" and pct < LOW:
                mode = "on"
                led.write(1.0)
            elif mode == "on" and pct > HIGH:
                mode = "off"
                led.write(0.0)
            print(f"light={pct:5.1f}%  mode={mode}")
        sleep(0.2)
except KeyboardInterrupt:
    led.write(0)
    board.exit()
