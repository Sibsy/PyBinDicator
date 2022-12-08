import board
import digitalio
import time

class ButtonController:
    button_led_pin = board.A2
    button_pin = board.A3
    led = digitalio.DigitalInOut(button_led_pin)
    led.direction = digitalio.Direction.OUTPUT
    button = digitalio.DigitalInOut(button_pin)
    button.direction = digitalio.Direction.INPUT

    def enable(self):
        print('enabled button')
        self.led.value = True

    def disable(self):
        print('disabled button')
        self.led.value = False

    def blink(self):
        while True:
            self.led.value = True
            time.sleep(0.5)
            self.led.value = False
            time.sleep(0.5)

    def testButton(self):
        while True:
            time.sleep(1)
            #strangely the default for the button is True (if not pressed) and False if pressed.
            #if your button connections are a bit wonky this function can get weird and require the board to be reset.
            if(self.button.value == True):
                self.led.value = False
                print("Unpressed")
            else:
                print("Pressed")
                self.led.value = True
