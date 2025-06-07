# Megihletett ez a dolog, ez nem olyan, hogy magától generálódik, mindig nyomni kell a play gombot, hogy az olvasó

# kellő mértékben el tudjon mélyülni.


from random import choice

noun1 = ["a gyerekek", "a szülők", "a barátok", "a régi barátok", "az új barátok", "a tanárok", "a tanítványok",
         "a csoporttársak", "a kollégák", "a beosztottak", "az orvosok", "a diáktársak", "a volt kollégák",
         "a leendő kollégák", "a zenészek", "a festők", "a színészek", "a rendezők", "az operatőrök", "a lányok",
         "a fiúk", "a táncosok", "a munkások", "a tigrisek", "az elődök", "a feleségem szülei", "az apám munkatársai",
         "a húgom barátnői", "az öcsém volt tanárai", "a tigris évei", "a felesége szülei", "az apja munkatársai",
         "a húga barátnői"]

negation = choice([" nem ", " "])

verb = ["követnek", "ismernek", "szeretnek", "látnak", "hagynak el", "találnak meg", "adnak el", "tartanak meg",
        "mennek el", "érkeznek meg", "utaznak el", "vonulnak be", "fizetnek ki", "üldöznek",
        "ölnek meg", "adnak kést a kezembe", "várnak rám", "várnak rád", "indulnak keletre"]

clause = ["Itt a vége.", "Ez egy új kezdet.", "Ugyanaz megint.", "Már semmi sem ugyanaz."]

adjective1 = ["Hideg", "Sötét", "Kopár", "Kietlen", "Lakatlan", "Elhagyott", "Vakító"]

noun2 = ["falak között", "sziklák között", "erdőben", "házak között", "jégmezőn", "hegyek között",
         "hómezőn", "tisztáson", "kertben"]

verb2 = ["állok", "ülök", "várok", "haladok"]

noun3 = ["vöröslő homály", "sóval hintett város", "ugyanazok ugyanúgy", "elmaradó barátok", "égő csipkebokor",
         "négyzet háromszöggel", "árnyék és sötétség", "szétnyílik a tenger", "... nem ... semmi", "lángoszlop",
         "esik az eső", "megnyílik a föld", "végtelen tér", "kongó üresség", "élőholtak serege", "leszáll a hold",
         "angyalok serege", "sugárzó űrhajó", "nagymama és nagypapa"]

print(f"NÉGYSOROS\n\nMost már tudom, hogy {choice(noun1)}{negation}{choice(verb)}.\n{choice(clause)}\n"
      f"{choice(adjective1)} {choice(noun2)} {choice(verb2)},\nelőttem {choice(noun3)}.")


