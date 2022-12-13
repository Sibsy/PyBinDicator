import GlowBitController
import TimeController
import ButtonController

def startDebug():
    print("Debug Mode")

    #instantiate the controllers.
    button = ButtonController.ButtonController()
    gbit = GlowBitController.GlowBitController()

    #test the glowbit.
    gbit.top(GlowBitController.RED)
    gbit.bottom(GlowBitController.GREEN)

    #test the sleepmode.
    print("Going to Sleep.")
    #TimeController.sleep(10) fails for some reason.

    print("waking up!")
    gbit.turnOff()

def startProgram():
    print("Production Mode")

class BinData:
    UseURL: int
    AlertPreviousNight: int
    AlertTime: str
    SleepTime: str
    StoredData: StoredData

    @staticmethod
    def from_dict(obj) -> 'BinData':
        _UseURL = int(obj.get("UseURL"))
        _AlertPreviousNight = int(obj.get("AlertPreviousNight"))
        _AlertTime = str(obj.get("AlertTime"))
        _SleepTime = str(obj.get("SleepTime"))
        _StoredData = StoredData.from_dict(obj.get("StoredData"))
        return BinData(_UseURL, _AlertPreviousNight, _AlertTime, _SleepTime, _StoredData)


class Datum:
    Name: str
    Dates: [str]


    def from_dict(obj) -> 'Datum':
        _Name = str(obj.get("Name"))
        _Dates = [str.from_dict(y) for y in obj.get("Dates")]
        return Datum(_Name, _Dates)

class Root:
    ssid: str
    password: str
    BinData: BinData

    def from_dict(obj: Any) -> 'Root':
        _ssid = str(obj.get("ssid"))
        _password = str(obj.get("password"))
        _BinData = BinData.from_dict(obj.get("BinData"))
        return Root(_ssid, _password, _BinData)


class StoredData:
    format: str
    Data: [Datum]


    def from_dict(obj: Any) -> 'StoredData':
        _format = str(obj.get("format"))
        _Data = [Datum.from_dict(y) for y in obj.get("Data")]
        return StoredData(_format, _Data)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
