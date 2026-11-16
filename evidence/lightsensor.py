from collections import deque
class LightSensor:
    """Keeps the last n samples Firmata pushes from an analog pin."""
    def __init__(self, board, pin=0, n=16):
        self.samples = deque(maxlen=n)    # drops the oldest by itself
        self.avg = None
        # get_pin once: a pin can be taken only once per board
        self.pin = board.get_pin(f"a:{pin}:i")
        # a method as the callback (Week 6, State & devices)
        self.pin.register_callback(self._on_sample)
        self.pin.enable_reporting()
    def _on_sample(self, value):
        # runs on pyfirmata2's reader thread, once per sample
        self.samples.append(value)
        self.avg = sum(self.samples) / len(self.samples)
    def latest(self):
        return self.samples[-1] if self.samples else None
    def average(self):
        return self.avg                   # None until the first sample
