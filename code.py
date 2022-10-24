import ipaddress
import ssl
import rtc
import wifi
import socketpool
import adafruit_requests
import adafruit_ntp
import blinkpatterns
import BinProcess
import GenericFunctions
from collections import defaultdict

#  Quickboot skips the Startup animations and the checks
#  (i.e. that we have internet etc)
quickboot = 1

print("Starting the Bindicator!")
if quickboot == 0:
    blinkpatterns.bootup()

# Get wifi details and more from a secrets.py file
print("Get Secrets")
try:
    from secrets import secrets
except ImportError:
    print("Info we need is all in secrets. go populate it")

print("ESP32-S2 Info")
print("My MAC addr:", [hex(i) for i in wifi.radio.mac_address])

if quickboot == 0:
    print("Available WiFi networks:")
    for network in wifi.radio.start_scanning_networks():
        print(
            "\t%s\t\tRSSI: %d\tChannel: %d"
            % (str(network.ssid, "utf-8"), network.rssi, network.channel)
        )
    wifi.radio.stop_scanning_networks()

print("Connecting to %s" % secrets["ssid"])
wifi.radio.connect(secrets["ssid"], secrets["password"])
print("Connected to %s!" % secrets["ssid"])
print("My IP address is", wifi.radio.ipv4_address)

if quickboot == 0:
    ipv4 = ipaddress.ip_address("8.8.4.4")
    pingRes = wifi.radio.ping(ipv4) * 1000
    if pingRes > 0:
        print("Internet Connectivity is up")
        print("Ping google.com: %f ms" % (pingRes))
    else:
        print("No Internet connection or google is down?")

pool = socketpool.SocketPool(wifi.radio)
ctx = ssl.create_default_context()
requests = adafruit_requests.Session(pool, ctx)

ntp = adafruit_ntp.NTP(pool, tz_offset=10)  # Aussie gmt+10
rtc.RTC().datetime = ntp.datetime
# So if something goes wrong. well only sleep for 5 minutes and try again
sleeptime = 300
print("Fetching json from: ", secrets["BinJsonURL"])
try:
    response = requests.get(secrets["BinJsonURL"])
    sleeptime = BinProcess.ProcessBins(response.json(), secrets["BinData"])
    print(response.json())

except RuntimeError:
    print("Issue making get request to ", secrets["BinJsonURL"])
print()

bindata = secrets

print("done")
# this will occur if its not within 12 hours of the next bin day
# (so from lunch day before it wil ltell you to put bins out)
# and rest of time it will be in a super deep sleep state to conserve power

GenericFunctions.DeepSleep(sleeptime)
