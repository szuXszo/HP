# nem végtelen ciklus, 10 kör és vége

from random import shuffle
from random import choice
import time


places = ["a pályára", "a kormányba", "a szülőkhöz", "a hazámba", "a mozivásznakra",
           "az állatok közé", "a növények közé", "a pusztába", "az apparátusba",
           "a földbe", "a jövőbe", "a lakásodba", "az előző életembe", "a színpadra",
           "az óceánba", "az éjszakába", "az utcára", "a Holdra", "a tudatalattidba",
           "az álmodba", "a munkahelyedre", "az alapkérdésekhez", "a könyv lapjaira",
            "a hírekbe", "a kövek alá"]

events = ["elfelejtené", "megunná", "semmibe venné", "beárazná",
            "megutálná", "megszokná", "kiismerné", "nevetségessé tenné",
            "megsajnálná"]

person = choice([["ek", "l"], ["", "d"]])

shuffle(places)
shuffle(events)

print("VISSZATÉRÉS\n")
time.sleep(2)

for n in range(9):
    print(f'Visszatér{person[0]} {places[n]},\nmielőtt {events[n]}{person[1]}.\n')
    time.sleep(3)
print((f'Visszatér{person[0]} {places[10]},\nmielőtt feljön a nap.\n'))
time.sleep(3)
print(f"Visszatér{person[0]} a szívedbe.")




