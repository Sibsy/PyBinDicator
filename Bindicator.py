import GlowBitController
import TimeController
import ButtonController
import WifiController
import MemoryController
from secrets import secrets
from config import config

import time
import Monash
import rtc

def startDebug():
    ##instantiate the controllers.
    button = ButtonController.ButtonController(config["button"])
    gbit = GlowBitController.GlowBitController(config["glowbit"])
    wifi = WifiController.WifiController(secrets, config["wifi"])
    tCont = TimeController.TimeController(config["time"])
    memory = MemoryController.MemoryController()

    ##test the glowbit.
    gbit.top(GlowBitController.WHITE)
    gbit.bottom(GlowBitController.WHITE)

    ##test the button
    button.testButton() ##WARNING: this is an execution blocking infinite loop.

    ##test Wifi and set DateTime
    wifi.connect()
    currentTime = wifi.setDateTime(config['timezone_offset'])
    #joke = wifi.callURL("https://api.chucknorris.io/jokes/random")
    #print(json.loads(joke)["value"])
    #second = wifi.callURL("https://www.monash.vic.gov.au/ocapi/Public/myarea/wasteservices?geolocationid=f8cda7aa-afec-41d8-9f41-9b0137f705ef&ocsvclang=en-AU")
    #print(second)

    print("Last Boot Time Was: ", memory.LastWakeTime)
    memory.LastWakeTime = currentTime

    bins = Monash.getBinData(secrets["bin_data"], wifi)
    activeBins = list(filter(lambda x: (x.isActive(tCont.alertBegin, tCont.alertEnd) == True), bins))
    memory.Notifications = activeBins

    gbit.showNotifications(memory.Notifications)

    ##Test the MemoryController
    memory.clearNotifications()
    memory.addNotification("test3", time.localtime(time.time()), GlowBitController.YELLOW)
    memory.saveToMem()


    ##test the sleepmode.
    #pinAlarm = button.buildPinAlarm()
    #time.lightsleep(None, pinAlarm) ##restarts the bindicator program when it wakes ##pass None and get the default SleepTime from config

def startProgram():
    ##instantiate the controllers.
    button = ButtonController.ButtonController(config["button"])
    gbit = GlowBitController.GlowBitController(config["glowbit"])
    wifi = WifiController.WifiController(secrets, config["wifi"])
    tCont = TimeController.TimeController(config["time"])
    memory = MemoryController.MemoryController()

    # Note: Currently we dont want to play any animations during the bootup sequence
    # Sleep() is code blocking and we want it to connect to wifi Whilst the animation plays.
    gbit.top(GlowBitController.WHITE)
    gbit.bottom(GlowBitController.WHITE)

    ##Connect to wifi and set Date Time
    wifi.connect()
    currentTime = wifi.setDateTime(config['timezone_offset'])
    print("Last Boot Time Was: ", memory.LastWakeTime)

    #was button hit?
    wokenUp = wasButtonHit(memory.LastWakeTime, currentTime)
    if(wokenUp):
        memory.clearNotifications()
    else:
        #check and remove expired notifications
        activeNotifs = list(filter(lambda x: (x.hasExpired() == False), bins))
        memory.Notifications = activeNotifs

        # replace this line with a function for your own council!
        bins = Monash.getBinData(secrets["bin_data"], wifi)
        memory.Notifications = bins
        gbit.showNotifications(memory.Notifications)


    #Determine Next Wake Time.
    nextWakeTime = tCont.getNextWakeTime(memory.Notifications)

    #Finaly, save the new memory state
    memory.LastWakeTime = currentTime
    memory.NextWakeTime = nextWakeTime
    memory.saveToMem()

    # now go back to sleep.
    pinAlarm = button.buildPinAlarm()
    tCont.deepsleep(nextWakeTime, pinAlarm)

    #end program untill next wake.
