import board
import digitalio
import time
import alarm

class ButtonController:
    button_led_pin = board.A2
    button_pin = board.A3
    led = digitalio.DigitalInOut(button_led_pin)
    led.direction = digitalio.Direction.OUTPUT

    #constructor
    def __init__(self, config):
        self.debounce = config['debounce']

    #de-constructor
    def __del__(self):
        self.releasePins()

    def releasePins(self):
        print("Button bindings released")
        self.button.deinit()
        self.led.deinit()

    def buildPinAlarm(self):
        self.releasePins()
        #pin must be released .deinit() from the ButtonController before the alarm can be placed.
        #https://docs.circuitpython.org/en/latest/shared-bindings/alarm/pin/index.html#alarm.pin.PinAlarm
        return alarm.pin.PinAlarm(pin=self.button_pin, value=False, pull=True)

    def enableButton(self):
        print('enabled button')
        self.led.value = True
        self.button = digitalio.DigitalInOut(self.button_pin)
        self.button.direction = digitalio.Direction.INPUT

    def disableButton(self):
        print('disabled button')
        self.led.value = False
        self.button.deinit()

    def readButtonState(self):
        #todo add debounce code here
        return self.button.value

    def blink(self):
        while True:
            self.led.value = True
            time.sleep(0.5)
            self.led.value = False
            time.sleep(0.5)

    def testButton(self):
        self.enableButton()
        while True:
            time.sleep(0.25)
            #strangely the default for the button is True (if not pressed) and False if pressed.
            #if your button connections are a bit wonky this function can get weird and require the board to be reset.
            if(self.button.value == True):
                self.led.value = False
                print("Pressed")
            else:
                print("Unpressed")
                self.led.value = True
