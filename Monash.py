import io
from ElementTree import parse, fromstring
import sys
import json

bin_data = []


def getBinData(url, wifiController):
    htmlResult = wifiController.callURLJson(url)["responseContent"]
    # htmlResult = open("monash-dirty.txt", "r").read()

    htmlResult = htmlResult.replace("\r\n", "")

    ##NOTE: will need to strip() (trim) the fields

    stream = io.StringIO(htmlResult)
    DOM = parse(stream)

    print_sub_tree(DOM.getroot())

    return dict(zip(bin_data[::2], bin_data[1::2]))


def get_geo_location_id(url, wifiController, address):
    htmlResult = wifiController.callURL(url)

    stream = json.loads(htmlResult)["Items"]

    for i in stream:
        if i["AddressSingleLine"] == address:
            print("------------------------------------------------------------------------------------------------")
            print("Address is found, getting Geo Location ID.")
            return i["Id"]


def print_sub_tree(node, depth=0):
    global bin_data

    if node.text is not None:
        text = '"' + node.text + '"'
    else:
        text = ""
    if depth in (8, 10) and text != "" and "Collected" not in text:
        # print(" " * depth, "-", node.tag, text)
        if depth == 8:
            bin_data.append(node.text.strip())
        else:
            bin_data.append(node.text.strip().split(" ")[1].split("/"))

    for key, value in node.attrib.items():
        if key != "class":
            print(" " * depth, "|", key, ":", value)
    for subnode in node:
        print_sub_tree(subnode, depth + 2)
