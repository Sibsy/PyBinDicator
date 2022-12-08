import neopixel
from rainbowio import colorwheel
import board

RED = (255, 0, 0)
ORANGE = (255, 34, 0)
YELLOW = (255, 170, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
VIOLET = (153, 0, 255)
MAGENTA = (255, 0, 51)
PINK = (255, 51, 119)
AQUA = (85, 125, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)

class GlowBitController:
    pixel_pin = board.A1
    num_pixels = 8
    pixel_brightness = 1
    pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=pixel_brightness)

    def top(self, color):
        #self.pixels.fill(color)
        self.pixels[0] = color
        self.pixels[1] = color
        self.pixels[2] = color
        self.pixels[3] = color
        self.pixels.show()

    def bottom(self, color):
        #self.pixels.fill(color)
        self.pixels[4] = color
        self.pixels[5] = color
        self.pixels[6] = color
        self.pixels[7] = color
        self.pixels.show()

    def turnOff(self):
        self.pixels.fill(OFF)

