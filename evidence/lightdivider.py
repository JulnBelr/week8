from pyfirmata2 import Arduino
from time import sleep
# pyfirmata2 calls this once per sample, on its reader thread
def on_sample(value):
    raw = int(value * 1023)          # 10-bit, delivered as 0.0..1.0
    print(f"{value:.3f}  (raw {raw})")
board = Arduino("/dev/ttyACM0")
board.samplingOn(200)          # start the reader: a sample every 200 ms
light = board.get_pin("a:0:i")
light.register_callback(on_sample)
light.enable_reporting()
try:
    while True:
        sleep(1)               # samples arrive on their own
except KeyboardInterrupt:
    board.exit()
