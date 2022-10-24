secrets = {
    "ssid": "YourSSID",
    "password": "WIFIPass",
    "BinData": {
        "UseURL": 0,
        "AlertPreviousNight": 1,
        "AlertTime": "17:00",
        "SleepTime": "23:59",
        "BinJsonURL": "",
        "BinFormat": {
            "RED": {
                "JsonKey": "AllBinDays",
                "DateFormat": "D-M-YYYY",
                "Seperator": "-",
                "IsArray": 0,
            },
            "Yellow": {
                "JsonKey": "AllBinDays",
                "DateFormat": "D-M-YYYY",
                "Seperator": "-",
                "IsArray": 0,
            },
            "GREEN": {
                "JsonKey": "GreenWasteNext",
                "DateFormat": "D-M-YYYY",
                "Seperator": "-",
                "IsArray": 1,
            }
        },
        "StoredData" : {
            "format": "D-M-YYYY",
            "Data": {
                "Red" : [
                    "27-9-2022",
                    "4-1-2022"
                ],
                "Yellow": [
                   "4-1-2022"
                ],
                "Green": [
                    "4-1-2022"
                ],
            }
        }
    }
}
