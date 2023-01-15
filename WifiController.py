import wifi
import rtc
import adafruit_ntp
import adafruit_requests
import ssl
import socketpool

class WifiController:
    def __init__(self, secrets):
        self.SSID = secrets["ssid"]
        self.Password = secrets["password"]

        if len(self.SSID) == 0 or len(self.Password) == 0:
            raise Exception("WiFi secrets are kept in secrets.py, please add them there!")



    def scanNetwork(self):
        print("Available WiFi networks:")
        for network in wifi.radio.start_scanning_networks():
            print(
                "\t%s\t\trssi: %d\tchannel: %d"
                % (str(network.ssid, "utf-8"), network.rssi, network.channel)
            )
        wifi.radio.stop_scanning_networks()
        print("======================")

    def connect(self):
        print("Connecting to WIFI: %s" % self.SSID)
        wifi.radio.connect(self.SSID, self.Password)

        print("Connected! My IP address is: ", wifi.radio.ipv4_address)

    def setDateTime(self, timezone_offset):
        pool = socketpool.SocketPool(wifi.radio)
        ntp = adafruit_ntp.NTP(pool, tz_offset=timezone_offset)  # aussie gmt+10
        rtc.RTC().datetime = ntp.datetime
        print("The current Date Time is: ", ntp.datetime);

    def printNetworkInfo(self):
        print("==============")
        print("My MAC address:", [hex(i) for i in wifi.radio.mac_address])
        print("My IP address: ", wifi.radio.ipv4_address)
        print("==============")

    def callURL(self, url):
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())

        print("Calling URL: ", url)
        response = requests.get(url)
        result = response.text
        response.close()
        return result

    def callURLJson(self, url):
        pool = socketpool.SocketPool(wifi.radio)
        requests = adafruit_requests.Session(pool, ssl.create_default_context())

        print("Calling URL: ", url)
        response = requests.get(url)
        result = response.json()
        response.close()
        return result

    def ping(self, ipaddress):
        #"8.8.4.4" google
        ipv4 = ipaddress.ip_address(ipaddress)
        pingres = wifi.radio.ping(ipv4) * 1000
        if pingres > 0:
            print("internet connectivity is up")
            print("ping google.com: %f ms" % (pingres))
        else:
            print("no internet connection or google is down?")

