#for OpenAPI
from unittest import result
import requests
import xml.etree.ElementTree as ET
import time

#for Messenger
import telegram

#for common
import time

#for OpenAPI
shipping_number = str(oooooooooooo)
URL = "oooooooooooo"+shipping_number

shippingFinishedText = "배달완료"
space = " "

lastTreeCount = 0
currentTreeCount = 0

#for Messenger
telegram_token = 'oooooooooooo'
private_chat_id = 'oooooooooooo'
bot = telegram.Bot(token = telegram_token)

while True:

        response = requests.get(URL)

        tree = ET.fromstring(response.text)

        currentTrees = tree.find("trackInfo").findall("detaileTrackList")

        currentTreeCount = len(currentTrees)

        if (currentTreeCount > lastTreeCount):
                for i in range(lastTreeCount, currentTreeCount):
                        date = currentTrees[i].find("date").text
                        hourMinute = currentTrees[i].find("time").text
                        location = currentTrees[i].find("location").text
                        status = currentTrees[i].find("statue").text

                        resultText = shipping_number + space + date + space + hourMinute \
                                + '\n' + location + space + status

                        print( bot.send_message(private_chat_id, text = resultText) )

                        if (shippingFinishedText in status):
                                print("프로그램을 종료합니다.")
                                exit()

                lastTreeCount = currentTreeCount

        time.sleep(300)
