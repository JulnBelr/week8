from time import sleep
from pyfirmata2 import Arduino
# pyfirmata2 calls this once per sample, on its reader thread
def on_sample(value):
    print(f"{value:.3f}   (raw {int(value * 1023)})")
board = Arduino("/dev/ttyACM0")  # or Arduino(Arduino.AUTODETECT)
board.samplingOn(200)          # start the reader: a sample every 200 ms
light = board.get_pin("a:0:i")
light.register_callback(on_sample)
light.enable_reporting()
try:
    while True:
        sleep(1)               # samples arrive on their own
except KeyboardInterrupt:
    board.exit()
