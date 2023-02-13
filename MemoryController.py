# https://docs.circuitpython.org/en/latest/shared-bindings/nvm/index.html
# the non-volatile-memory everything has to be written in HEX bytes so maybe its easier if we use a txt file and Json to save data?
# foamyguy wrote a wrapper for the NVM library which makes it more convenient to use. hells yeah!
import json
from time import struct_time
import foamyguy_nvm_helper as nvm_helper
import BinProcess

class MemoryController:
    _state: json
    Notifications: [BinProcess.Bin]
    LastWakeTime: struct_time
    NextWakeTime: struct_time
    NotificationExpiryTime: struct_time

    def __init__(self):
        self._state = self.loadFromMem()

    def saveToMem(self) -> None:
        notifs = []
        for notif in self.Notifications:
            notifs.append(notif.toJson())

        jsonObj = {
            "LastWakeTime": struct_TimeToString(self.LastWakeTime),
            "NextWakeTime": struct_TimeToString(self.LastWakeTime),
            "NotificationExpiryTime": struct_TimeToString(self.NotificationExpiryTime),
            "CurrentNotifications": notifs
        }

        encodedState = json.dumps(jsonObj)
        print(encodedState)
        nvm_helper.save_data(encodedState, test_run=False, verbose=False)
        print("Saved Memory State to NVM.")

    def loadFromMem(self) -> None:
        try:
            encodedString = nvm_helper.read_data()
            print(encodedString)
            self._state = json.loads(encodedString)
            self.LastWakeTime = stringToStruct_Time(self._state["LastWakeTime"])
            self.NextWakeTime = stringToStruct_Time(self._state["NextWakeTime"])
            self.NotificationExpiryTime = stringToStruct_Time(self._state["NotificationExpiryTime"])
            self.Notifications = []
            for notif in self._state["CurrentNotifications"]:
                self.Notifications.append(BinProcess.Bin(notif["Label"],stringToStruct_Time(notif["NextCollectionDate"]),notif["Color"]))

            print("Loaded Memory State from NVM.")
        except EOFError:
            print("[EOFError] memory state error; re-loaded default memory state")
            self.initializeMemoryState() # on first boot there is no saved memory.
        except KeyError:
            print("[KeyError] memory state error; re-loaded default memory state")
            self.initializeMemoryState()
            # memory object was updated in code but not in memory.
            # make sure you update memory.txt with the new structure and default values.
        except ValueError:
            print("[ValueError] memory state error; re-loaded default memeory state")
            self.initializeMemoryState() # corrupted json?


    def initializeMemoryState(self):
        file = open("memory.txt", "r")
        encodedString = file.read()
        nvm_helper.save_data(encodedString, test_run=False, verbose=False)
        file.close()
        print("Initialised Memory State into NVM.")

    def clearNotifications(self) -> None:
        self.Notifications = []
        self.NotificationExpiryTime = None

    def addNotification(self, label: str, collectionDate: struct_time, color: str ) -> None:
        notif = BinProcess.Bin(label, collectionDate, color)
        self.Notifications.append(notif)

# ###########################
# Might move these to a helper/ utility file in future.

def stringToStruct_Time(input: str) -> struct_time:
    if(input == None):
        return None

    arr = input.split("/")
    return struct_time(arr)

def struct_TimeToString(input: struct_time) -> str:
    if(input == None):
        return None

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


