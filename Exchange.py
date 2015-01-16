# -*- coding: utf-8-*-
import re
import json
import urllib2
from urllib import urlopen

WORDS = ["CURRENCY", "EXCHANGE"]
API_URL = "http://rate-exchange.appspot.com/currency?"
FIRST_CURR = ""
FIRST_CURR_ACTUAL = ""
SECOND_CURR = ""
SECOND_CURR_ACTUAL = ""

def handle(text, mic, profile):
    def setFirstCurrency(text):
        global FIRST_CURR_ACTUAL
        FIRST_CURR_ACTUAL = "Dollars"

    def setSecondCurrency(text):
        global SECOND_CURR_ACTUAL
        SECOND_CURR_ACTUAL = "Yen"

    def convertToCode():
        global FIRST_CURR
        global FIRST_CURR_ACTUAL
        global SECOND_CURR
        global SECOND_CURR_ACTUAL
        code_list = {"Yen" : "JPY", "Dollars" : "USD"}

        for key, value in code_list.iteritems():
            if key == FIRST_CURR_ACTUAL:
                FIRST_CURR = value
            if key == SECOND_CURR_ACTUAL:
                SECOND_CURR = value

    mic.say("What is your first currency?")
    setFirstCurrency(mic.activeListen())

    mic.say("What is your second currency?")
    setSecondCurrency(mic.activeListen())

    convertToCode()

    #needs to make sure FIRST_CURR and SECOND_CURR are set

	mic.say("Getting exchange rate of " + FIRST_CURR + " against " + SECOND_CURR + ".")
	jsonurl = urlopen(API_URL + "from=" + FIRST_CURR + "&to=" + SECOND_CURR)

	try:
		rate = json.loads(jsonurl.read())
	except ValueError, e:
		pass # invalid json
        mic.say("An error occured. Maybe the API is offline?")
    else:
		pass # valid json
		mic.say("Okay, here is the exchange rate.")
		mic.say("It is " + str(rate["rate"]) + " " + SECOND_CURR + " for 1 " + FIRST_CURR + ".")


def isValid(text):
        return bool(re.search(r'\bcurrency|exchange\b', text, re.IGNORECASE))
