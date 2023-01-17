import Bindicator
# import ipaddress
#import ssl
#import rtc
#import wifi
#import socketpool
#import adafruit_requests
#import adafruit_ntp
#import blinkpatterns
#import BinProcess
#import GenericFunctions
#import secrets
#  from collections import defaultdict

debugMode = True

print('\n------------------------------------------------------------------------------------------------')
if(debugMode == False):
    print("***Starting the Bindicator in ->Production<- Mode!")
    Bindicator.startProgram()
else:
    print("***Starting the Bindicator in ->Debug<- Mode!")
    Bindicator.startDebug()


    # if ParsedBinData['BinData']['UseURL'] == 1:
    #     print("Fetching json from: ", ParsedBinData['BinData'])
    #     try:
    #         response = requests.get(ParsedBinData['BinData']["BinJsonURL"])
    #         sleeptime = BinProcess.UrlProcessor()
    #         print(response.json())

    #     except RuntimeError:
    #         print("Issue making get request to ", ParsedBinData['BinData']["BinJsonURL"])
    #     print("Done URL Stuff")
    # else:
    #     print("Using Secrets BinData")
    #     try:
    #         print("You have {} bins to process"
    #             .format(len(ParsedBinData['BinData']['StoredData']['Data'])))
    #         print(ParsedBinData['BinData']['StoredData']['format'])
    #         sleeptime = BinProcess.StoredDataProcessor(ParsedBinData['BinData']['StoredData'])
    #     except RuntimeError:
    #         hasErrored = 1


    # print("done")
    # if hasErrored == 1:
     #   if errors will sleep for 3 s
    #     sleeptime = 3
    #this will occur if its not within 12 hours of the next bin day
    #(so from lunch day before it wil ltell you to put bins out)
    #and rest of time it will be in a super deep sleep state to conserve power

    # GenericFunctions.DeepSleep(sleeptime)
