import time
from MemoryController import struct_TimeToString, stringToStruct_Time
import json

class Bin:
    Label: str
    NextCollectionDate: struct_time
    Color: tuple

    def __init__(self, _label: str, _nextCollectionDate: struct_time, _color: tuple):
        self.Label = _label
        self.NextCollectionDate = _nextCollectionDate
        self.Color = _color

    def toJson(self) -> json:
        return { "Label": self.Label, "Color": self.Color, "NextCollectionDate": struct_TimeToString(self.NextCollectionDate) }

    def hasExpired(self) -> bool:
        return (time.mktime(NextCollectionDate) < time.time())

    def isActive(self, startTime: int=0, endTime: int=0) -> bool:
        nextCollectionDateInSeconds = time.mktime(NextCollectionDate)
        alertStartTime = nextCollectionDateInSeconds - startTime
        alertEndTime = nextCollectionDateInSeconds + endTime
        return ( alertStartTime < time.time() and self.hasExpired() == False)
