from show import Window


class NeoPixel():
    def __init__(self, n: int, auto_write: bool = True):
        self._n = n
        self._pixels = [(0, 0, 0)] * n
        self._auto_write = auto_write
        self._window = Window()

    def show(self):
        self._window.show_pixels(self._pixels)

    def fill(self, color: tuple):
        self._pixels = [color] * self._n

    def __setitem__(self, key: int, value: tuple):
        self._pixels[key] = value
        if self._auto_write:
            self.show()

    def __getitem__(self, key: int) -> tuple:
        return self._pixels[key]

    @property
    def n(self) -> int:
        return self._n

    def deinit(self):
        self._window.cleanup()
