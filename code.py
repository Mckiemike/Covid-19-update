import urllib.request
import re

"""

COVID-19 Live Tracker

The data is based on the website
https://www.worldometers.info/coronavirus/

This code is to raise awareness of the virus.
Please stay safe everyone.

The data on the code updates quite often.

"""

try:
    p = urllib.request.urlopen('https://www.worldometers.info/coronavirus/')
except:
    print("We seem to be having trouble sending an HTTP request, please try again later!")
    exit()

cases = re.findall(r'[\d]{1,3},[\d]{3}', str(p.read()))

print("COVID-19 Live Tracker made by Otieno\n")

print("There are {0} COVID-19 cases in the world. {1} of which are currently infected, {2} are mild condition while {3} are in critical conditions.\n".format(cases[0], cases[5], cases[6], cases[7]))

print("Unfortunately, {0} people have died because of this virus. Luckily {1} have recovered.".format(cases[1], cases[4]))

print("\n Stay Safe Please :)")