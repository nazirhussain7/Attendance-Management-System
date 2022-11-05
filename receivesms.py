import requests
import ssl
import xml.etree.ElementTree as ET


def main():
    username = "john"
    password = "Xc3ffs"
    httpUrl = "https://127.0.0.1:9508/"
    folder = "inbox";
    limit = "3";

    sendString = (httpUrl + "api?action=receivemessage&username="
                  + username + "&password="
                  + password + "&folder=" + folder + "&limit="
                  + limit + "&afterdownload=delete")

    print("Sending html request: " + sendString + "\n")
    requests.packages.urllib3.disable_warnings()

    response = requests.get(sendString, verify=False)
    print("Http response received: ")
    DisplayMessages(response.text)


def DisplayMessages(response):
    root = ET.fromstring(response)
    if root.findall('data/message/*') == []:
        print('The inbox is empty')
        return


for child in root.findall('data/message'):
    sender = child.find('originator').text
    text = child.find('messagedata').text
    DisplayMessage(sender, text)


def DisplayMessage(sender, text):
    print(sender + ": " + text)


if __name__ == "__main__":
    main()
