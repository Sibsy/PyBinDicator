# Write your code here :-)
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
