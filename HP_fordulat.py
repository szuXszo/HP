from random import choice

first_lines = ["Amikor a nap\nvérrel festette a dombokat,",
               "Amikor a Szíriusz\nfelgyulladt az égen,",
               "Amikor a hó leple\nráakaszkodott a fákra,",
               "Amikor az éj sötétje\na városra borult,",
               "Amikor a lakások\nsápadt fénye kialudt,",
               "Amikor az első jégcsapok\nátszúrták a tájat,",
               "Amikor a hold metsző sugarai\na falaknak ütődtek,",
               "Amikor a temető csendje\nrátelepedett az utcákra,",
               "Amikor az éjféli mise\nhangjai elhaltak,",
               "Amikor az eső\ntisztára mosta az emberek arcát,",
               "Amikor a szél\nhamut hordott a szemetekbe,"]

agents = ["bíborosok", "apát", "fejedelem", "helytartó", "herceg",
          "bárók", "bírák", "alapítók", "kiválasztottak", "hegylakók",
          "ősi nemzetségek", "tábornokok", "földbirtokosok",
          "Igazak Szövetsége", "vidámgyermekek", "virágoskatonák",
          "vezér", "vének", "rózsalovagok"]

patients = ["a startup-vállalkozókra", "a projektmenedzserekre",
            "a tartalomgyártókra", "az AI-szakértőkre", "a képviselőkre",
            "a középvezetőkre", "az ételfutárokra", "a reklámipar robotosaira",
            "a pszichológusokra", "a szélszes szakemberekre", "a producerekre",
            "a sorozatszínészekre", "a külpolitikai elemzőkre", "az irodistákra",
            "a business analystekre", "a rendszerüzemeltető mérnökökre",
            "az equity-menedzserekre", "a gyorséttermi munkatársakra",
            "a márkanagykövetekre"]

adjectives = ["a visszatért", "a felesküdött", "a törvényt ülő",
              "a törvényt hozó", "a jogfosztott", "a száműzött",
              "a csillagszemű", "az égre emelt tekintetű",
              "az ígéret zászlaját kibontó", "a szavatartó",
              "a megalázott", "a könnyező", "a vasba öltözött",
              "a hit lándzsáját magasba emelő", "a meghasadt szívű",
              "a féligszületett", "a felkent"]

agent = choice(agents)
if agent[-1] == "k":
    verb = "lecsaptak"
else:
    verb = "lecsapott"

print("FORDULAT\n")
print(f'{choice(first_lines)}\n{choice(adjectives)} {agent}\n{verb} {choice(patients)}.')