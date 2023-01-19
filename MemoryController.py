# https://docs.circuitpython.org/en/latest/shared-bindings/nvm/index.html
# https://docs.circuitpython.org/en/latest/docs/library/io.html
# the non-volatile-memory everything has to be written in HEX bytes so maybe its easier if we use a txt file and Json to save data?
import json
from time import struct_time

class MemoryController:
    state: json

    def __init__(self):
        self.state = self.loadFromMem()

    # https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
    # When connected to a computer CircuitPython prevents from writting to memory.
    # This prevents corruption due to multiple simultaneus writes.
    def saveToMem(self) -> None:
        try:
            file = open("memory.txt", "w") # w for WRITE, a for APPEND, r for READ
            encodedstate = json.dumps(self.state)
            file.write(encodedstate)
            file.close()
            print("Saved Memory State to file.")
        except OSError:
            print("!!!Cannot save memory state!!!")
            print("To make the Filesystem writable by software you must connect the A0 pin to GND. See boot.py for details.");

    def loadFromMem(self) -> State:
        file = open("memory.txt", "r")
        encodedString = file.read()
        self.state = json.loads(encodedString)
        file.close()
        print("Loaded Memory State from file.")
        return self.state

    def clearNotifications(self) -> None:
        self.state['CurrentNotifications'] = []
        self.state['NotificationExpiryTime'] = None

    def addNotification(self, label: str, color: str) -> None:
        notif = { "Label": label, "Color": color }
        self.state['CurrentNotifications'].append(notif)

    def getNotifications(self) -> json:
        return self.state['CurrentNotifications']

    def getLastWakeTime(self) -> str:
        asStruct = stringToStruct_Time(self.state['LastWakeTime'])
        return asStruct

    def setLastWakeTime(self, input: str) -> None:
        asCSV = struct_TimeToString(input)
        self.state['LastWakeTime'] = asCSV

    def getNextWakeTime(self) -> str:
        asStruct = stringToStruct_Time(self.state['NextWakeTime'])
        return asStruct

    def setNextWakeTime(self, input: struct_time) -> None:
        asCSV = struct_TimeToString(input)
        self.state['NextWakeTime'] = asCSV

# ###########################
# Might move these to a helper/ utility file in future.

def stringToStruct_Time(input: str) -> struct_time:
    arr = input.split("/")
    return struct_time(arr)

def struct_TimeToString(input: struct_time) -> str:
    return "{}/{}/{}/{}/{}/{}/{}/{}/{}".format(
        input.tm_year,
        input.tm_mon,
        input.tm_mday,
        input.tm_hour,
        input.tm_min,
        input.tm_sec,
        input.tm_wday,
        input.tm_yday,
        input.tm_isdst)


