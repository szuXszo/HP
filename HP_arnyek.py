# haiku

from random import choice


first_line = ["ősz a nyárra", "tél az őszre", "év az évre", "nap a napra",
              "bú a bajra", "baj a búra", "bűn a szívbe", "szó a szájra",
              "bor a vérbe", "tűz a gallyra", "pénz a zsebbe", "láz a testre",
              "pap a faszra", "fagy az ágra", "hír a hírre"]

second_line = [["hegyek", "dombok", "sziklák", "felhők", "falak"],
                ["a Hold", "a fák", "a füst", "a köd", "a drót"]]

third_line = ["a kövezetre", "a sugárútra", "a kerületre", "a kikötőre",
              "az erőműre", "a helyőrségre", "a lábfejedre", "az asztalodra",
              "a társatokra", "a turistákra", "az állatokra", "a kirakatra",
              "a munkagépre", "a dédmamára", "a képernyőre", "a búzaföldre",
              "a sípályára", "a gyártelepre", "a Balatonra", "a puszta tájra",
              "a temetőre"]

count = choice([0, 1])
if count == 0:
    second_line = f'{choice(second_line[count])} árnyéka kúszik'
else:
    second_line = f'kúszik {choice(second_line[count])} árnyéka'

print("ÁRNYÉK\n")
print(f'Mint {choice(first_line)},\n{second_line}\n{choice(third_line)}.')