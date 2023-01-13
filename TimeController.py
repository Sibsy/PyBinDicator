import alarm
import board
import digitalio
import time

class TimeController:
    def __init__(self, config):
        self.sleepTime = config["sleep_time"]
        self.useExternalWakeUp = config["use_external_wake_up"] ##TODO the plan is to have the BUTTON wake the bindicator on press.
        self.alertBegin = config["alert_begin"]

    def sleep(self, timeToSleep = None):
        if timeToSleep == None:
            timeToSleep = self.sleepTime

        time.sleep(timeToSleep)

    def lightsleep(self, timeToSleep = None, pin_alarm = None):
        if timeToSleep == None:
            timeToSleep = self.sleepTime

        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + timeToSleep)

        if self.useExternalWakeUp == True and pin_alarm != None:
            alarm.light_sleep_until_alarms(time_alarm, pin_alarm)
        else:
            alarm.light_sleep_until_alarms(time_alarm)

    def deepsleep(self, timeToSleep = None, pin_alarm = None):
        #Deepsleep restarts the board when it wakes... but you CAN preserve pin states whilst in sleep.
        if timeToSleep == None:
            timeToSleep = self.sleepTime

        print("================")
        print("going to sleep now...")

        time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + timeToSleep)

        if self.useExternalWakeUp == True and pin_alarm != None:
            alarm.exit_and_deep_sleep_until_alarms(time_alarm, pin_alarm)
        else:
            alarm.exit_and_deep_sleep_until_alarms(time_alarm)

