import alarm
import time

class TimeController:
    sleepTime: int
    usExternalWakeUp: bool
    alertBegin: int # in seconds
    alertEnd: int # in seconds

    def __init__(self, config):
        self.sleepTime = int(config["sleep_time"])
        self.useExternalWakeUp = bool(config["use_external_wake_up"])
        # convert the time to seconds for easy math.
        self.alertBegin = convertStartTimeToSeconds(str(config["alert_begin"]))
        self.alertEnd = convertEndTimeToSeconds(str(config["alert_end"]))

    def sleep(self, timeToSleep: int = None):
        if timeToSleep == None:
            timeToSleep = self.sleepTime

        time.sleep(timeToSleep)

    def lightsleep(self, timeToSleep: int=None, pin_alarm=None):
        if timeToSleep is None:
            timeToSleep = self.sleepTime

        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + timeToSleep)

        if self.useExternalWakeUp is True and pin_alarm is not None:
            alarm.light_sleep_until_alarms(time_alarm, pin_alarm)
        else:
            alarm.light_sleep_until_alarms(time_alarm)

    def deepsleep(self, timeToSleep: int=None, pin_alarm=None):
        #Deepsleep restarts the board when it wakes... but you CAN preserve pin states whilst in sleep.
        if timeToSleep == None:
            timeToSleep = self.sleepTime

        print("================")
        print("going to sleep now...")

        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + timeToSleep)

        if self.useExternalWakeUp is True and pin_alarm is not None:
            alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)
        else:
            alarm.exit_and_deep_sleep_until_alarms(time_alarm)

    def getNextWakeTime(self, notifications: [Bin]) -> struct_time:
        if(len(notifications) > 0):
            newDate = notifications[0].NextCollectionDate
            newDate.tm_hour=23
            newDate.tm_min=59
            newDate.tm_sec=59
            return newDate
        else:
            newDate = time.localtime(time.time())
            newDate.tm_hour=23
            newDate.tm_min=59
            newDate.tm_sec=59
            return newDate

def wasButtonHit(nextWakeUpTime: struct_time, currentTime: struct_time) -> bool:
    # if the next wake time hasnt passed yet then the device was woken by either
    # the button being pressed or a power fluctuation.
    woken = (time.mktime(nextWakeUpTime) > time.mktime(currentTime))
    print("Bindicator Woken Up?: ", woken)
    return woken

def convertStartTimeToSeconds(input: str) -> int:
    rawTime = input.split(":")
    return ((24-int(rawTime[0])) * 60 * 60) + (int(rawTime[1]) * 60)

def convertEndTimeToSeconds(input: str) -> int:
    rawTime = input.split(":")
    return ((int(rawTime[0])) * 60 * 60) + (int(rawTime[1]) * 60)

