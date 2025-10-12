import random


things = ["kalapács", "csavarhúzó", "harapófogó", "fűrész", "szög", "csavar",
          "ütvefúró", "szike", "csipesz", "sztetoszkóp", "sniccer", "vonalzó",
          "olló", "cellux", "kés", "villa", "só", "bors", "koriander",
          "fahéj", "Biblia", "rózsafüzér", "rúzs", "körömlakk", "festékszóró",
          "izzó", "kézfej", "lábfej", "hüvelykujj", "mutatóujj", "lábujj",
          "fül", "orr", "vér", "vér", "vér", "ondó", "szemfog", "metszőfog",
          "vastagbél", "vese", "máj", "kisagy", "ketamin", "morfium",
          "könyökcsont", "térdkalács", "ürülék", "lőpor", "töltény", "csikk",
          "ukulele", "misekehely", "tömjén", "kolomp", "koszorú", "köröm",
          "füldugó", "sósav", "számológép", "mérleg", "iránytű", "szappan",
          "hajszárító",  "lavór", "?", "?", "?", "L", ":-o", ":(", ":)",
          "+", "<3", "nagyító"]


print(f"TETTHELY\n\n")
random.shuffle(things)
count = 0
for r in range(7):
    words_in_line = []
    for k in range(random.randint(0, 2)):
        words_in_line.append(things[count])
        count += 1
    words_len = sum([len(word) for word in words_in_line])
    if len(words_in_line) == 0:
        print()
    elif len(words_in_line) == 1:
        space_num = random.randint(0, 50 - words_len)
        print(f"{space_num * ' '}{words_in_line[0]}")
    else:
        space_num1 = random.randint(0, 50 - (words_len + 1))
        space_num2 = random.randint(1, 50 - (words_len + space_num1))
        print(f"{space_num1 * ' '}{words_in_line[0]}{space_num2 * ' '}{words_in_line[1]}")
