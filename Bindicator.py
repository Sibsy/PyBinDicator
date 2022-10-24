from typing import List
from typing import Any
from dataclasses import dataclass

# 9 json

@dataclass
class BinData:
    UseURL: int
    AlertPreviousNight: int
    AlertTime: str
    SleepTime: str
    BinJsonURL: str
    URLBinFormat: URLBinFormat
    StoredData: StoredData

    @staticmethod
    def from_dict(obj: Any) -> 'BinData':
        _UseURL = int(obj.get("UseURL"))
        _AlertPreviousNight = int(obj.get("AlertPreviousNight"))
        _AlertTime = str(obj.get("AlertTime"))
        _SleepTime = str(obj.get("SleepTime"))
        _BinJsonURL = str(obj.get("BinJsonURL"))
        _URLBinFormat = URLBinFormat.from_dict(obj.get("URLBinFormat"))
        _StoredData = StoredData.from_dict(obj.get("StoredData"))
        return BinData(_UseURL, _AlertPreviousNight, _AlertTime, _SleepTime, _BinJsonURL, _URLBinFormat, _StoredData)

@dataclass
class Datum:
    Name: str
    Dates: List[str]

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        _Name = str(obj.get("Name"))
        _Dates = [.from_dict(y) for y in obj.get("Dates")]
        return Datum(_Name, _Dates)

@dataclass
class GREEN:
    JsonKey: str
    DateFormat: str
    Seperator: str
    IsArray: int

    @staticmethod
    def from_dict(obj: Any) -> 'GREEN':
        _JsonKey = str(obj.get("JsonKey"))
        _DateFormat = str(obj.get("DateFormat"))
        _Seperator = str(obj.get("Seperator"))
        _IsArray = int(obj.get("IsArray"))
        return GREEN(_JsonKey, _DateFormat, _Seperator, _IsArray)

@dataclass
class RED:
    JsonKey: str
    DateFormat: str
    Seperator: str
    IsArray: int

    @staticmethod
    def from_dict(obj: Any) -> 'RED':
        _JsonKey = str(obj.get("JsonKey"))
        _DateFormat = str(obj.get("DateFormat"))
        _Seperator = str(obj.get("Seperator"))
        _IsArray = int(obj.get("IsArray"))
        return RED(_JsonKey, _DateFormat, _Seperator, _IsArray)

@dataclass
class Root:
    ssid: str
    password: str
    BinData: BinData

    @staticmethod
    def from_dict(obj: Any) -> 'Root':
        _ssid = str(obj.get("ssid"))
        _password = str(obj.get("password"))
        _BinData = BinData.from_dict(obj.get("BinData"))
        return Root(_ssid, _password, _BinData)

@dataclass
class StoredData:
    format: str
    Data: List[Datum]

    @staticmethod
    def from_dict(obj: Any) -> 'StoredData':
        _format = str(obj.get("format"))
        _Data = [Datum.from_dict(y) for y in obj.get("Data")]
        return StoredData(_format, _Data)

@dataclass
class URLBinFormat:
    RED: RED
    YELLOW: YELLOW
    GREEN: GREEN

    @staticmethod
    def from_dict(obj: Any) -> 'URLBinFormat':
        _RED = RED.from_dict(obj.get("RED"))
        _YELLOW = YELLOW.from_dict(obj.get("YELLOW"))
        _GREEN = GREEN.from_dict(obj.get("GREEN"))
        return URLBinFormat(_RED, _YELLOW, _GREEN)

@dataclass
class YELLOW:
    JsonKey: str
    DateFormat: str
    Seperator: str
    IsArray: int

    @staticmethod
    def from_dict(obj: Any) -> 'YELLOW':
        _JsonKey = str(obj.get("JsonKey"))
        _DateFormat = str(obj.get("DateFormat"))
        _Seperator = str(obj.get("Seperator"))
        _IsArray = int(obj.get("IsArray"))
        return YELLOW(_JsonKey, _DateFormat, _Seperator, _IsArray)

# Example Usage
# jsonstring = json.loads(myjsonstring)
# root = Root.from_dict(jsonstring)
