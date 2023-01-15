import io
from ElementTree import parse
import sys

def getBinData(url, wifiController):
    htmlResult = wifiController.callURLJson(url)["responseContent"]
    #htmlResult = open("monash-dirty.txt", "r").read()

    htmlResult = htmlResult.replace("\r\n","")

    ##NOTE: will need to strip() (trim) the fields

    stream = io.StringIO(htmlResult)
    DOM = parse(stream)
    print_sub_tree(DOM.getroot())
    #getMyData(DOM.getroot())

def getMyData(root, type):
    if node.attrib['class'] = type:
        print("horray")
    else:
        print("no")

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
