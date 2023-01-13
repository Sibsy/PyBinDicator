import GlowBitController
import TimeController
import ButtonController
import WifiController
from secrets import secrets
from config import config

import json
import Monash

def startDebug():
    ##instantiate the controllers.
    button = ButtonController.ButtonController(config["button"])
    gbit = GlowBitController.GlowBitController(config["glowbit"])
    wifi = WifiController.WifiController(secrets)
    time = TimeController.TimeController(config["time"])

    ##test the glowbit.
    gbit.top(GlowBitController.WHITE)
    gbit.bottom(GlowBitController.WHITE)

    ##test the button
    #button.testButton() ##WARNING: this is an execution blocking infinite loop.

    ##test Wifi and set DateTime
    wifi.connect()
    wifi.setDateTime(10)
    joke = wifi.callURL("https://api.chucknorris.io/jokes/random")
    print(json.loads(joke)["value"])
    #Monash.getBinData(secrets["bin_data_url"], wifi)

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
    wifi.setDateTime(10)
    ##Get Bin Data
    ##Check Against Date
    ##Light Sleep Untill Notification Dismissal or Date Change.


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
