import alarm
import board
import digitalio
import neopixel
import time


def DeepSleep(TimeToSleep):
    np_power = digitalio.DigitalInOut(board.NEOPIXEL_POWER)
    np_power.switch_to_output(value=False)
    np = neopixel.NeoPixel(board.NEOPIXEL, 1)
    np[0] = (50, 50, 50)
    time.sleep(0.5)
    np[0] = (0, 0, 0)
    time.sleep(0.5)
    np[0] = (50, 50, 50)
    time.sleep(1)
    np[0] = (0, 0, 0)
    time_alarm = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + TimeToSleep)
    alarm.exit_and_deep_sleep_until_alarms(time_alarm)


