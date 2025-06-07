# Itt csak egyszer kell nyomni a futtatást, aztán generálódnak a sorpárok a végtelenségig.

from random import choice
import time

nouns = ["fáraó", "maharadzsa", "török szultán", "ezredes", "kétkezi munkás", "elnök", "agitátor",
        "rendőr", "szolgabíró", "főispán", "őrgróf", "báró", "nagyherceg", "bíboros", "esperes",
        "földmérő", "sorkatona", "keretlegény", "pártfunkcionárius", "írástudó", "napszámos",
        "hétszilvafás nemes", "szőlősgazda", "államtitkár", "titkos tanácsos", "rendőrminiszter",
        "ápolónő", "háztartásbeli családanya", "szoptatós dajka", "királynő", "bárónő", "grófnő",
        "hercegnő", "kitartott", "színésznő", "apáca", "szerzetes", "messzeföldön híres zenész", "festő",
        "kőfaragó", "földműves", "uzsorás", "kisiparos", "pártvezér", "tűzoltóparancsnok", "elismert tudós",
        "szervezeti titkár", "kurtizán", "sebészorvos", "kisvárosi tanár", "kockázati tőkebefektető",
        "osztályvezető", "polgármester", "kisvállalkozó", "felügyelőbizottsági tag", "közmunkás",
         "próféta"]

clauses = ["a többiekkel együtt túrtam a földet", "kenyeret adtam az éhezők szájába",
          "bort öntöttem az üres poharakba", "szétosztottam mindenemet", "elhagytam a családomat",
          "megöltem a rosszakaróimat", "elherdáltam mindenemet", "megloptam, akit tudtam",
          "a többiekkel együtt néztem az eget", "piszkos kézzel az égre mutattam",
          "magamhoz vettem az elhagyott gyerekeket", "nem ismertem se istent, se embert",
          "magányos és kitaszított voltam", "nem néztem a nők szemébe",
          "véres kézzel törvényt lobogtattam", "kést szúrtam a szívembe", "megszakadt a szívem",
          "nevetés nem hagyta el a számat", "állandó rettegésben éltem",
          "akit tudtam, megmentettem önmagától", "csak a vér szavát ismertem", "csak a pénz szagát éreztem",
          "felemeltem az elesetteket", "nem ártottam és nem tettem jót", "eltaszítottam magamtól mindenkit",
          "akit tudtam, megaláztam", "felakasztottam magam", "a fölfelé igyekvőket visszarugdostam",
          "a fölfelé igyekvőknek segítő kezet nyújtottam", "egyedül voltam sok barát közt",
          "beleőrültem a bánatba", "csak szenvedés jutott osztályrészemül", "mindenkinek benyújtottam a számlát",
          "mindenki a vendégem volt", "mindenkinek a vendége voltam", "a senki földjén voltam valaki",
          "megtettem, amit kellett", "a törvény betűje szerint éltem", "vérrel mostam tisztára a nevem",
          "búzát vetettem a halál nyomába", "istent játszottam", "többre tartottam az álmokat a valóságnál",
          "két lábbal álltam a földön, és ez lett a vesztem"]

print("KARMA\n")
time.sleep(2)
last_nouns = []
last_clauses = []

while True:
    noun = choice(nouns)
    while noun in last_nouns:
        noun = choice(nouns)
    if len(last_nouns) < 5:
        last_nouns.append(noun)
    else:
        last_nouns.pop(0)
        last_nouns.append(noun)

    clause = choice(clauses)
    while clause in last_clauses:
        clause = choice(clauses)
    if len(last_clauses) < 5:
        last_clauses.append(clause)
    else:
        last_clauses.pop(0)
        last_clauses.append(clause)

    print(f"Amikor {noun} voltam,\n{clause}.\n")
    time.sleep(3.5)




