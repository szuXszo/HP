# Miután megcsináltam ezt, rájöttem, hogy részben hasonló a logikája, mint SZD
# Valahol című versének. A második személyű mondásige + kettősponttal való átvezetést
# ő már ott megcsinálta korábban.

from random import choice
import time

empty_things = ["fejjel", "tekintettel", "szemekkel", "szívvel", "kézzel", "gyomorral",
         "zsebekkel", "ígéretekkel", "szavakkal", "borosüveggel", "tárral",
         "vászonnal", "vággyal", "reménnyel", "tarisznyával", "csekkel", "szelvénnyel"]

settings = ["a sarjadó vetésben", "a száradó fák alatt", "az égő bokrok mellett",
           "a szakadó esőben", "a holdfényes parkban", "a játszótér homokozójában",
           "az éjszaka csendjében", "a bevásárlóközpont derengésében",
           "nap nap után", "hétről hétre", "évről évre", "egy végigrobotolt életen át",
           "városról városra", "rendelőről rendelőre", "a rehabilitációs központban",
           "az iroda hajnali folyosóján", "az altemplom homályában", "a Király utcában",
           "a rákospalotai bekötőúton", "a gyermekmegőrzőben", "az olcsójános haverokkal",
           "a megvadult tanítványokkal", "a felhergelt munkatársakkal",
           "az árvaház lakóival", "három távolkeleti túristával", "a csuhába bújt koldusokkal",
           "az élősködő unokatestvérekkel", "a vért kiáltó gyerekekkel", "a befektetők seregével"]

wishes = ["Az isten irgalmazzon rajtad", "Rajtad az isten se irgalmazzon",
        "A szentek legyenek örök pártfogóid", "A teremtő sújtson le rád végtelen haragjával",
        "Mária oltalmazzon utadon", "A pokol tüzében égjen el a lelked",
        "Az angyalok vegyenek maguk közé", "Az ördög egye ki a szíved",
        "Az orrodon folyjon ki a szemed", "Amerre jársz, a szerencse csillaga ragyogjon",
        "Fizetséged vég nélküli álmatlanság legyen", "Rohadjanak le a végtagjaid",
        "Legfőbb tanácsosod a Sátán legyen", "Álom és ébrenlét közt tévelyegj, míg eszedet tudod",
        "Amihez hozzáérsz, pusztulás legyen sorsa", "Mást többé ne hallj, mint saját hangodat",
        "Mást többé ne láss, mint saját tükörképed", "Mást többé ne szeress, mint saját magadat"]

last_empty_things = []
last_settings = []
last_wishes = []


def choose_text(texts, last_texts, num):
    text = choice(texts)
    while text in last_texts:
        text = choice(texts)
    if len(last_texts) < num:
        last_texts.append(text)
    else:
        last_texts.pop(0)
        last_texts.append(text)
    return text


print("ÜRES\n")
time.sleep(2)
while True:
    print(f'"Üres {choose_text(empty_things, last_empty_things, 11)} követtelek\n'
          f'{choose_text(settings, last_settings, 21)}.\n'
          f'{choose_text(wishes, last_wishes, 11)}.\n'
          f'De te csak motyogtál magad elé:"\n')
    time.sleep(6)




