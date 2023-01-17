import GlowBitController
import TimeController
import ButtonController
import WifiController
from secrets import secrets
from config import config

import json
import Monash
import BlinkPatterns

address = '3/36 Panorama Street, Clayton 3168' #Replace your address to get geolocationid (Monash Council only for now)
gbit = GlowBitController.GlowBitController(config["glowbit"]) #Global gbit

def startDebug():
    ##instantiate the controllers.
    #button = ButtonController.ButtonController(config["button"])
    wifi = WifiController.WifiController(secrets)
    time = TimeController.TimeController(config["time"])

    gbit.initGlowbit() #glowbit booting up

    ##test the button
    #button.testButton() ##WARNING: this is an execution blocking infinite loop.

    ##test Wifi and set DateTime
    wifi.connect()
    time_now = wifi.setDateTime(config['timezone_offset'])
    print('The current date: ', time_now.tm_mday, time_now.tm_mon, time_now.tm_year)

    geolocationid = Monash.get_geo_location_id('https://www.monash.vic.gov.au/api/v1/myarea/search?keywords={}'.format(address), wifi, address) #get geolocationid with the address

    #exit(1) crash the program

    #geolocationid = '55090461-0157-430a-9e96-bf9673a3215f'
    print(geolocationid)

    #wifi.stop_access_point()
    #wifi.connect()

    bd = Monash.getBinData('https://www.monash.vic.gov.au/ocapi/Public/myarea/wasteservices?geolocationid='+ geolocationid +'&ocsvclang=en-AU', wifi)
    print('------------------------------------------------------------------------------------------------')
    for key, value in bd.items():
        print("{} : {}".format(key, value))
        if((int(value[0]) - time_now.tm_mday) < 7 and int(value[1]) == time_now.tm_mon and int(value[2]) == time_now.tm_year):
            print("->THIS WEEK<- === This bin ->{}<- will be collected in days: {} \n".format(key, int(value[0]) - time_now.tm_mday))
            bin_color_display(key)
        else:
            print("->NEXT WEEK<- === This bin ->{}<- will be collected in days: {} \n".format(key, int(value[0]) - time_now.tm_mday))
            bin_color_display(key)

    print('------------------------------------------------------------------------------------------------')

    #print(Monash.getBinData(tmpgeo, wifi))#test 2nd call request

    exit(1)# to crash the program

    ##test the sleepmode.
    pinAlarm = button.buildPinAlarm() ## need to dispose of the ButtonController to release the pin binding for the Pin_Alarm
    time.deepsleep(None, pinAlarm) ##restarts the bindicator program when it wakes ##pass None and get the default SleepTime from config

def startProgram():
    ##instantiate the controllers.
    button = ButtonController.ButtonController(config["button"])
    gbit = GlowBitController.GlowBitController(config["glowbit"])
    wifi = WifiController.WifiController(secrets)
    time = TimeController.TimeController(config["time"])
    ##Connect to wifi and set Date Time
    #wifi.connect()
    wifi.setDateTime(11)
    ##Get Bin Data
    ##Check Against Date
    ##Light Sleep Untill Notification Dismissal or Date Change.

def bin_color_display(key):
    global gbit
    if(key == 'Landfill Waste'):
        gbit.top(GlowBitController.RED)
    else:
        gbit.top(GlowBitController.YELLOW)
    gbit.bottom(GlowBitController.GREEN)


# class BinData:
#     UseURL: int
#     AlertPreviousNight: int
#     AlertTime: str
#     SleepTime: str
#     StoredData: StoredData

#     @staticmethod
#     def from_dict(obj) -> 'BinData':
#         _UseURL = int(obj.get("UseURL"))
#         _AlertPreviousNight = int(obj.get("AlertPreviousNight"))
#         _AlertTime = str(obj.get("AlertTime"))
#         _SleepTime = str(obj.get("SleepTime"))
#         _StoredData = StoredData.from_dict(obj.get("StoredData"))
#         return BinData(_UseURL, _AlertPreviousNight, _AlertTime, _SleepTime, _StoredData)


# class Datum:
#     Name: str
#     Dates: [str]


#     def from_dict(obj) -> 'Datum':
#         _Name = str(obj.get("Name"))
#         _Dates = [str.from_dict(y) for y in obj.get("Dates")]
#         return Datum(_Name, _Dates)

# class Root:
#     ssid: str
#     password: str
#     BinData: BinData

#     def from_dict(obj: Any) -> 'Root':
#         _ssid = str(obj.get("ssid"))
#         _password = str(obj.get("password"))
#         _BinData = BinData.from_dict(obj.get("BinData"))
#         return Root(_ssid, _password, _BinData)


# class StoredData:
#     format: str
#     Data: [Datum]


#     def from_dict(obj: Any) -> 'StoredData':
#         _format = str(obj.get("format"))
#         _Data = [Datum.from_dict(y) for y in obj.get("Data")]
#         return StoredData(_format, _Data)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
