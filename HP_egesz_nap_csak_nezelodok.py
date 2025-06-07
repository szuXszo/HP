import random
import time


things = ["szék", "karfa", "székláb", "cipő", "cipőfűző", "parketta", "póló",
         "gomb", "széktámla", "csavar", "ajtó", "fal", "plafon", "vezeték",
         "konnektor", "laptoptöltő", "pulóver", "párna", "szatyor", "táska",
         "szekrény", "szekrényajtó", "termosztát", "villanykapcsoló",
         "asztal", "asztalláb", "radiátor", "cső", "redőny", "pohár",
         "ablaküveg", "tányér", "villa", "laptop", "hangfal", "toll",
         "adapter", "fejhallgató", "ceruza", "könyv", "polc", "dezodor",
         "mérőszalag", "WD-40", "kilincs", "C-vitamin", "autó (matchbox)",
         "doboz", "összecsukott szék", "körömvágó olló", "kalapács",
         "csavarhúzó", "lámpa", "villanykörte", "lámpabúra", "láb", "térd",
         "lábfej", "zokni", "nadrág", "kézfej", "felkar", "ujj",
         "köröm", "tenyér", "póló", "ujjperc", "csokis papír", "takaró",
         "pénztárca", "hosszabbító", "páraelszívó", "fehér felirat",
         "fekete felirat", "kék felirat", "hajszárító", "angol-magyar szótár",
         "papírstóc", "pókháló", "lecsapott bogár", "folt", "internetkábel",
         "USB-vezeték", "sivatag (képen)", "ég (képen)", "sziklafal (képen)",
         "hold (képen)", "beduin (képen)", "ajtókeret", "füzet", "húszforintos",
         "papírfecni", "papír", "szék árnyéka", "asztal árnyéka",
         "cipő árnyéka", "karfa árnyéka", "kábel árnyéka", "lábfej árnyéka",
         "elszíneződés", "ablakkilincs", "füldugó",
         "ablak (fa, ház, autó)", "ablak (fa, ház, ember)","ablak (fa, ház, ég)",
         "ablak (fa, ég)", "ablak (fa, ház)", "óra", "szemüvegtok", "cellux",
         "telefontöltő", "csipszes zacskó", "vonal", "négyzet", "kör",
         "téglalap", "trapéz", "félkör", "szürke téglalap", "fekete téglatest",
         "fordított gúla", "fekete kör", "kék négyzet", "fehér négyzet",
         "fehér téglalap", "téglatestet formáló fekete téglalapok", "kék vonal",
         "szürke karika", "kék téglalap", "fehér félkör", "fehér átló", "?",
         "anyajegy", "szög", "telefon",
         "cipők", "asztallábak", "széklábak", "tollak", "könyvek", "dobozok",
         "lábak", "lábfejek", "ujjak", "papírok", "füldugók", "vonalak",
         "négyzetek", "fehér téglalapok", "fekete téglalapok", "szürke vonalak",
         "kábelek"]


print("EGÉSZ NAP CSAK NÉZELŐDÖK\n")
time.sleep(2)
while True:
    seconds = random.choice([0.1, 0.8, 2.2])
    events = random.randint(2, 6)
    for event in range(events):
        thing = random.choice(things)
        if thing[-2:] not in ["ak", "ek", "ok", "ók", "ők"]:
            thing = f'{random.choice(["egy ", ""])}{thing}'
        print(thing + "\n")
        time.sleep(seconds)
