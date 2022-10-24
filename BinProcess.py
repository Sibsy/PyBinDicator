import json
import blinkpatterns

def ProcessBins(JSON, STRUCT):

    print("Doing Something")
    #  Well return data here for how long to sleep for
    calulatedsleep = 60  # placeholder for now
    maxsleep = 1 * 60 * 60 * 12  # in seconds. (so 12 hours)
    if calulatedsleep > maxsleep:
        return maxsleep
    else :
        return calulatedsleep


def StoredDataProcessor(storedData):
    try:
        print("DoLogic")
        print(storedData)
        BinData= json.loads(storedData)
        print("You have {} bins to process".format(len(BinData[Data])))
    except RuntimeError:
        return 3
    # Seconds in 12 hours
    # (i.e. If all goes well. we shouldnt have to do anything for 12 hours)
    return 43200


def UrlProcessor():
    print("I Do Nothing Right now, so eh")
