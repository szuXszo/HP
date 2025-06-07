# végtelenciklus

from random import choice
import time

dict_options = {
"actors" : ["András", "Noel", "Péter", "Judit", "Gábor", "Eszter", "Núr", "Dorottya",
         "Sugárka", "Benett", "Mihály", "Laci", "Tibi", "Anna", "Hannus", "Alex",
         "Kata", "Zsuzsa", "Liza", "a szeretője", "a fia", "a lánya", "az anyja",
         "az apja", "a nagyapja", "a nagymamája", "az unokája", "az unokatestvére",
         "a beosztottja", "a főnöke", "a nagybátyja", "az üzlettársa", "az áldozópapja",
         "a könyvelője", "az ápolója", "a titkos szerelme", "egy ismeretlen ember",
         "a kertésze", "a mentora", "a tanítványa"],

"settings" : ["a temetésen", "a keresztelőn", "a konklávén", "a szertartás végén",
           "a negyven napos utazáson", "a turné utolsó napján", "egy lehetséges világban",
           "egy távoli galaxisban", "a szomszéd pincéjében", "az iskolai foglalkozáson",
           "Los Angelesben", "egy folyami hajón", "egy párhuzamos dimenzióban",
           "a börtönudvaron", "a törzshelyén", "az irodában", "a születésnapján",
           "a házassági évfordulóján", "a városházán", "a csapatépítőn",
           "a meditációs elvonuláson", "a barátja jachtján", "az állásinterjún",
           "az anyósánál", "a fény és a sötétség határán", "pontban napkeltekor",
           "napnyugta után", "az utolsó vacsorán", "a feltámadása után", "a díjátadón",
           "az aratás végén", "egy szilveszteri buliban", "egy vidéki kivonuláson",
           "a napfogyatkozás órájában", "a karriernapon", "2013 március 13-án",
           "a megvilágosodásakor", "a felügyelőbizottsági ülésen", "a szükségszálláson"],

"states" : ["minden erejét összeszedve", "végső elkeseredésében", "egy jobb világban bízva",
            "egy gyermekkori látomástól vezérelve", "határtalan unalmában", "magát jobb színben feltüntetve",
            "a családját megutálva", "magát szórakoztatva", "a pokoltól való félelmében",
            "a mennybejutás reményében", "drogoktól elkábulva", "alkoholban tobzódva",
            "kitisztult elmével", "pénzt várva", "a hatalomtól eszét vesztve",
            "a múlt súlyától nyomorítva", "a vér szagát érezve", "egy próféta magabiztosságával",
            "kisebbségi érzését ellensúlyozva", "egy testen kívüli tapasztalat konzekveciáit levonva",
            "őrjítő féltékenységében", "gyógyszerektől leszedálva", "a győzelem eksztázisában",
            "a biztos halál tudatában", "a jóhírét mentve"],

"verbs" : ["azt gondolta", "elhitette", "azt mesélte", "azt énekelte", "felvette",
           "megidézte", "eljátszotta", "elismerte", "aranyba öntötte", "kifaragta",
           "a homokba rajzolta", "smaragdból kirakta", "az oltár fölé festette",
           "márványba véste", "a lábára tetoválta", "a csillagokból kiolvasta",
           "a madarak röptéből megjósolta", "elmondta", "elbábozta", "azt képzelte",
           "továbbadta", "azt hallucinálta", "vérével a falra írta", "betűtésztából kirakta",
           "versbe szedte", "a párnahuzatra hímezte", "a húsvéti tojásra festette",
           "azt hazudta", "azzal áltatta magát", "az ellensége szájába adta", "letagadta",
           "nem mondta el", "nem ismerte be", "kifakadt"]}

print("CÍM NÉLKÜL\n")
time.sleep(2)

dict_last_items = {"actors": [], "settings": [], "states": [], "verbs": []}

while True:
    dict_choices = {"actors": choice(dict_options["actors"]), "settings": choice(dict_options["settings"]),
                    "states": choice(dict_options["states"]), "verbs": choice(dict_options["verbs"])}
    for item in dict_choices:
        while dict_choices[item] in dict_last_items[item]:
            dict_choices[item] = choice(dict_options[item])
        if len(dict_last_items[item]) < 8:
            dict_last_items[item].append(dict_choices[item])
        else:
            dict_last_items[item].pop(0)
            dict_last_items[item].append(dict_choices[item])

    print(f'{dict_choices["actors"]} {dict_choices["settings"]}\n{dict_choices["states"]} {dict_choices["verbs"]}, hogy\n')
    time.sleep(4.5)




