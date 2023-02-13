import neopixel
from rainbowio import colorwheel
import board
import BinProcess
import random

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

    def __init__(self, config):
        self.pixel_brightness = config["brightness"]
        self.pixels = neopixel.NeoPixel(self.pixel_pin, self.num_pixels, brightness=self.pixel_brightness)

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

    def showNotifications(self, bins: [Bin]):
        print(bins)
        if(len(bins) == 0):
            return
        elif (len(bins) == 1):
            self.top(bins[0].Color)
            self.bottom(bins[0].Color)
            return
        elif (len(bins) == 2):
            #To Do: dont want the same pattern every time, so randomise the colors
            start = random.randint(0,1)
            if(start == 0):
                self.top(bins[0].Color)
                self.bottom(bins[1].Color)
            else:
                self.top(bins[1].Color)
                self.bottom(bins[0].Color)

        elif(len(bins) == 3):
            raise Exception("3 bins isnt supported yet")

