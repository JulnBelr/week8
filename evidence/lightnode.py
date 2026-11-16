from time import sleep
from pyfirmata2 import Arduino
from lightsensor import LightSensor
class LightNode:
    """Calibrated light sensor on A0, dimmable LED on pin 9."""
    def __init__(self, port="/dev/ttyACM0", sensor=0, led=9,
                 dark=0.05, bright=0.90, n=16, interval_ms=50):
        self.board = Arduino(port)
        self.board.samplingOn(interval_ms)    # start the reader thread
        self.sensor = LightSensor(self.board, sensor, n)
        self.led = self.board.get_pin(f"d:{led}:p")
        self.dark, self.bright = dark, bright # bench anchors, 0.0..1.0
        sleep(n * interval_ms / 1000 + 0.2)   # let the window fill once
    def read_pct(self):
        v = self.sensor.average()
        if v is None:
            return 0.0
        pct = (v - self.dark) / (self.bright - self.dark) * 100
        return max(0.0, min(100.0, pct))
    def set_brightness(self, pct):
        self.led.write(max(0.0, min(100.0, pct)) / 100)
    def update(self):
        light = self.read_pct()
        self.set_brightness(100 - light)      # darker room, brighter LED
        return light
    def close(self):
        self.led.write(0)
        self.board.exit()
if __name__ == "__main__":
    node = LightNode()
    try:
        while True:
            print(f"light={node.update():.1f}") # telemetry line, rung 4
            sleep(1.0)
    except KeyboardInterrupt:
        node.close()
