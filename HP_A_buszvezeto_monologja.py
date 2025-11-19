# Nem végtelen ciklus

from random import shuffle
from random import choice
import time


texts1 = ["Nem kell félni, napkeltére otthon vagyok.",

          "Még egy telet már nem bírok ki, ha elered\n"
          "a hó, nekihajtok a Dunának.",

          "Nyolc éve, három hónapja és 21 napja vagyok\n"
          "ezen a vonalon.",

          "Csukott szemmel is látom a reflektorokat.",

          "Édes Istenem, segíts ki a sötétből.",

          "Egy, kettő, három. Megelőzöm a párom."]

texts2 = ["A nagyapám járási bíró volt.\n"
         "Az ávósok verték agyon a kurafit.\n"
         "Legalábbis nagymama így mesélte.",

         "Nagymamát mindenki szerette,\n"
         "úgy szállt a haja a szélben,\n"
         "mint pernye a füstben.",

         "Nagymamának a pajzsmirigye miatt\n"
         "olyan fehér volt a bőre,\n"
         "mint a hó a seefeldi sípályákon.",

         "Szerettem\n"
         "a\n"
         "nagymamát.",

         "Nagymama egyszer azt mondta,\n"
         "hogy belőlem még nagy utazó lesz,\n"
         "olyan helyeken járok majd,\n"
         "ahol senki a családból.",

         "Nagymama azt mondta, hogy az anyám\n"
         "a nagyapám génjeit örökölte,\n"
         "ezért nem érte meg a 30-at se.\n"
         "Mondjuk ő csak felvágta az ereit\n"
         "a kádban.",

         "Az emberi vér 55%-a víz.\n"
         "A vérplazmának 90-92%-a.",

         "Bár az állatok nagyrészének a vére\n"
         "az emberi vérhez nagyon hasonló\n"
         "összetételt mutat, vannak azért\n"
         "kivételek is. A halak vérének\n"
         "például jóval nagyobb része,\n"
         "mintegy 70-80%-a víz.",

         "A rákok és a kagylók vérének 80-\n"
         "90%-a víz. A szó köznapi értelmé\n"
         "ben ezen állatok esetében már nem\n"
         "is beszélhetünk vérről.",

         "Laposférgek, fonálférgek, szivacsok.\n"
         "Mi a közös bennük?\n"
         "Többek között az, hogy egyiknek sincs\n"
         "vére.",

         "Fejfájás, hányinger, zavartság,\n"
         "görcsroham, agyduzzanat.\n"
         "Ha a vérben lévő víz mennyisége megnő,\n"
         "ezekkel a tünetekkel találkozhatunk.",
         
         "A Zichy gróf lánya Melbourne-ben\n"
         "egy szobakonyhába szülte a lányát.\n"
         "Szerencsére a gróf ezt már nem\n"
         "láthatta.",
         
         "Amikor a Zichy gróf apja elveszítette\n"
         "a bányászati koncessziókat, még\n"
         "párbajozott is az egyik rosszakarójával.",
         
         "A Zichy gróftól mindent elvettek,\n"
         "az inasa cipőjében és mellényében\n"
         "hagyta el a pusztafai vadászkastélyt.",
         
         "Bezzeg a Habsburgok ma is jól élnek,\n"
         "és számláznak Bécsből, Salzburgból,\n"
         "Berlinből, Madeiráról vagy éppen\n"
         "Sóskútról az ENSZ-nek, a WHO-nak,\n"
         "az Európa Tanácsnak vagy éppen a\n"
         "Vatikánnak.",

         "91-ben Amszterdamban találkoztam a\n"
         "Zichy gróf unokájával egy foglalt házban,\n"
         "ahol négy hónapot töltöttem. Ő már\n"
         "egy éve ott volt.",

         "Amikor utoljára láttam a Zichy gróf\n"
         "unokáját, nekem könny, neki ópium\n"
         "csillogott a szemében.",

         "Az 50-es években a japán gazdaság\n"
         "padlógázzal tör előre. 1950-ben\n"
         "9,2%-kal, 1951-ben 10,1%-kal nő a\n"
         "GDP.",

         "Az 1970-es\n"
         "évekre a japán\n"
         "ipari termelés az\n"
         "USA-t kivéve mindenkit\n"
         "megelőz. A 73-as olajválság\n"
         "hatására a japánok az energiaintenzív\n"
         "ágazatokról a high-tech ágazatokra váltanak.",

         "Amikor 1985-ben amerikai nyomásra a\n"
         "dollárt leértékelik a jennel szemben,\n"
         "a Japán gazdaság növekedése satufékkel áll\n"
         "meg.",

         "A dollár leértékeléséből következő\n"
         "exportvisszaesést a japán kormányzat\n"
         "a monetáris politika lazításával\n"
         "próbálja ellensúlyozni.\n"
         "Ez azonban zsákutcának bizonyul.",

         "1991-ben a japán pénzügyi buborék kippukad,\n"
         "a japán tőzsdeindex az 1989-es 38 957\n"
         "pontos csúcsról 92-re 15 ezer\n"
         "pont alá zuhan. A japán\n"
         "gazdaság azóta is\n"
         "parkolópályán\n"
         "van.",

         "A japán tőzsde földbeállása miatt nekem\n"
         "is sok gondom volt a befektetőkkel.",
         
         "A kormányt veszített tradicionális\n"
         "japán társadalom és az USA-ból importált\n"
         "liberális kapitalizmus szerelemgyereke\n"
         "az 1,2 körül mozgó reprodukciós ráta."]

shuffle(texts2)
print("A BUSZVEZETŐ MONOLÓGJA\n")
time.sleep(2.5)
for text2 in texts2:
    print(text2 + "\n")
    wait2 = (len(text2) * 0.05) + 1
    time.sleep(wait2)
    text1 = choice(texts1)
    print(text1 + "\n")
    wait1 = (len(text1) * 0.05) + 1
    time.sleep(wait1)





