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
