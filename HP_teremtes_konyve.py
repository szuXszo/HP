# Ezt most a kedvedért úgy csináltam, hogy ne végtelen ideig fusson, hanem
# 81 018 518 és fél napig.

import random
import time

things1 = ["Világosság", "Sötétség", "Föld", "Ég", "Tenger", "Madár", "Hal", "Hegy", "Völgy",
          "Folyó", "Fa", "Fű", "Bokor", "Szél", "Villám", "Mennydörgés", "Eső", "Hullócsillag",
          "Én", "Te"]

things2 = [":-D", "^_^", "(^_^)", "(^^)", "T_T", "(._.)", "(T_T)", "(u_u)",
           "(>_<)", "(^o^)", "<3", "(^.^)", "(¬_¬)", "(-_-)", "O_o", "(._.?)",
           "(•_•?)"]

print("TEREMTÉS KÖNYVE\n")
time.sleep(2)
for count in range(0, 999999999999):
    if count < 3:
        things = things1
    elif count == 3:
        things = things2
    elif count == 4:
        things = things1
    else:
        things = random.choices([things1, things2], weights=[0.67, 0.33])[0]
    id_num = "000000000000"
    count = str(count + 1)
    id_num = id_num[:len(count) * -1] + count
    print(f"id_vilag: {id_num}")
    time.sleep(0.75)
    things_of_word = random.sample(things, 8)
    for n, thing in enumerate(things_of_word):
        thing = random.choices([thing, "Err:502"], weights=[0.95, 0.05])[0]
        if n < 7:
            print(thing, end='  ')
            time.sleep(0.75)
        else:
            print(thing)
            time.sleep(1)
            print("---------------------------------------------------------------")

