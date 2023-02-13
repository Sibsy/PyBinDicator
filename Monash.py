import io
from ElementTree import parse, Element
from GlowBitController import RED,GREEN,YELLOW
import BinProcess
import json
import time

def testBinData(binData: json, wifiController) -> [Bin]:
    bins = [
        BinProcess.Bin("Landfill Waste", time.localtime(time.time()), RED),
        BinProcess.Bin("Food and Garden Waste", time.localtime(time.time()), GREEN)
    ]
    return bins

# def testBinDataFromFile(binData: json, wifiController) -> [Bin]:
#     htmlResult = open("monash-dirty.txt", "r").read()
#     htmlResult = htmlResult.replace("\r\n","")

#     stream = io.StringIO(htmlResult)
#     DOM = parse(stream)

#     return bins

def getBinData(binData: json, wifiController) -> [Bin]:
    try:
        htmlResult = wifiController.callURLJson(binData["bin_data_url"])["responseContent"]
        htmlResult = htmlResult.replace("\r\n","")
    except TypeError as e: # note this is the wrong error for the Recaptcha
        # most likely we got hit by a google captcha.
        raise Exception("[ERROR] GOOGLE CAPTCHA!", e)

    stream = io.StringIO(htmlResult)
    DOM = parse(stream)

    articleTags = searchTreeByTag("article", DOM.getroot())
    bins = []
    for article in articleTags:
        #printNodeDetails(article)
        heading = searchTreeByTag("h3", article)[0]
        binType = heading.text

        date = searchTreeByAttrib("class", "next-service", article)[0]
        dateparts = date.text.strip().split(" ")[1].split("/")
        collectionDate = time.struct_time([int(dateparts[2]),int(dateparts[1]),int(dateparts[0]),0,0,0,4,-1,-1])

        bins.append(BinProcess.Bin(heading.Text, collectionDate, getBinColor(binType)))

    return bins

def getBinColor(label: str) -> tuple:
    if (label == "Landfill Waste"):
        return RED
    elif (label == "Recycling"):
        return YELLOW
    elif (label == "Food and Garden Waste"):
        return GREEN
    else:
        raise Exception("Unknown bin type")


def print_sub_tree(node, depth=0):
    if node.text is not None:
        text = '"' + node.text + '"'
    else:
        text = ""
    print(" "*depth, "-", node.tag, text)
    for key, value in node.attrib.items():
        print(" "*depth, "|", key, ":", value)
    for subnode in node:
        print_sub_tree(subnode, depth+2)

def printNodeDetails(node: Element):
    print("TAG: ", node.tag)
    print("InnerHTML: ", node.text)
    for k, v in node.attrib.items():
        print('{}="{}"'.format(k, v))

    print("Children: ", len(node._children))
    print("="*10)

def searchTreeByTag(needle: str, stack: Element) -> [Element]:
    arr: [Element] = []
    if(stack.tag == needle):
        #printNodeDetails(stack)
        arr.append(stack)
        return arr
    else:
        for subnode in stack:
            nodes = searchTreeByTag(needle, subnode)
            if(len(nodes) > 0):
                arr.extend(nodes)

    #print("found items: ", len(arr))
    return arr

def searchTreeByAttrib(attribName: str, attribValue: str, stack: Element) -> [Element]:
    arr: [Element] = []
    value = stack.get(attribName)
    if(value is not None and value == attribValue):
        #printNodeDetails(stack)
        arr.append(stack)
        return arr
    else:
        for subnode in stack:
            nodes = searchTreeByAttrib(attribName, attribValue, subnode)
            if(len(nodes) > 0):
                arr.extend(nodes)

    #print("found items: ", len(arr))
    return arr

