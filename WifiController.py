import wifi
import rtc
import adafruit_ntp
import adafruit_requests
import ssl
import socketpool

CA_STRING = (
    "-----BEGIN CERTIFICATE-----\n"
    "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\n"
    "-----END CERTIFICATE-----"
)


class WifiController:
    def __init__(self, secrets):
        self.SSID = secrets["ssid"]
        self.Password = secrets["password"]

        if len(self.SSID) == 0 or len(self.Password) == 0:
            raise Exception(
                "WiFi secrets are kept in secrets.py, please add them there!"
            )

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
        print("------------------------------------------------------------------------------------------------")
        print("Connecting to WIFI: %s" % self.SSID)
        wifi.radio.connect(self.SSID, self.Password)
        print("Connected! My IP address is: ", wifi.radio.ipv4_address)

    def stop_access_point(self):
        wifi.radio.stop_ap()

    def setDateTime(self, timezone_offset):
        pool = socketpool.SocketPool(wifi.radio)
        ntp = adafruit_ntp.NTP(pool, tz_offset=timezone_offset)  # aussie gmt+10
        rtc.RTC().datetime = ntp.datetime
        return ntp.datetime

    def printNetworkInfo(self):
        print("==============")
        print("My MAC address:", [hex(i) for i in wifi.radio.mac_address])
        print("My IP address: ", wifi.radio.ipv4_address)
        print("==============")

    def callURL(self, url):
        pool = socketpool.SocketPool(wifi.radio)
        context = ssl.create_default_context()
        # context.load_verify_locations(cadata=CA_STRING)
        # context.check_hostname = False
        requests = adafruit_requests.Session(pool, context)
        # requests = adafruit_requests.Session(pool, ssl.create_default_context())
        print("------------------------------------------------------------------------------------------------")
        print("Calling URL(text): ", url)
        response = requests.get(url)
        result = response.text
        response.close()
        # pool.close()
        return result

    def callURLJson(self, url):
        pool1 = socketpool.SocketPool(wifi.radio)
        context = ssl.create_default_context()
        # context.load_verify_locations(cadata=CA_STRING)
        # context.check_hostname = False
        requests = adafruit_requests.Session(pool1, context)
        # requests = adafruit_requests.Session(pool, ssl.create_default_context())
        print("------------------------------------------------------------------------------------------------")
        print("Calling URL(json): ", url)
        response = requests.get(url)

        result = response.json()
        response.close()
        # pool.close()
        return result

    def ping(self, ipaddress):
        # "8.8.4.4" google
        ipv4 = ipaddress.ip_address(ipaddress)
        pingres = wifi.radio.ping(ipv4) * 1000
        if pingres > 0:
            print("internet connectivity is up")
            print("ping google.com: %f ms" % (pingres))
        else:
            print("no internet connection or google is down?")
