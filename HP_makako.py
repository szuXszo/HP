# Minden generáláshoz újra kell futtatni.

from random import choice
from random import choices
from random import randint

words = ["mak", "makmak", "makmakmak", "makmakmakmak", "makmakmakmakmak", "makmakmakmakmakmak"]
punctuations_1 = [",", ",", ",", ",", ",", ":", ";", ".", "?", "!"]
punctuations_2 = [",", ",", ",", ",", ",", ";", ".", "?", "!", ""]
punctuations_3 = [".", ".", ".", ".", "?", "!"]

print("EGY MAKÁKÓ KÖLTEMÉNYE A MAKÁKÓK ELBESZÉLŐ KÖLTEMÉNYEI CÍMŰ ANTOLÓGIÁBÓL\n")
poem = ""
num_stanzas = randint(8, 16)
num_lines = randint(3, 6)
for s in range(num_stanzas):
    stanza = ""
    quotation = "no"
    for l in range(num_lines):
        line = ""
        for b in range(2):
            bar = ""
            num_syllable = 0
            while num_syllable < 6:
                word = choice(words[:6 - num_syllable])
                if b != 2 and num_syllable != 6:
                    bar += f"{word}{choices([',',''], [0.15, 0.85], k=1)[0]} "
                num_syllable = bar.count("a")
            line += bar
        if line[-2] == ",":
            line = line[:-2] + " "

        if quotation == "start":
            punctuation = choice(punctuations_2)
            stanza += f"„M{line[1:-1]}{punctuation}\n"
            quotation = "end"
        elif quotation == "end":
            punctuation = choice(punctuations_2)
            stanza += f"M{line[1:-1]}{punctuation}\n"
        else:
            punctuation = choice(punctuations_1)
            stanza += f"M{line[1:-1]}{punctuation}\n"

        if punctuation == ":":
            quotation = "start"

    if quotation == "end":
        poem += f"{stanza[:-2]}{choice(punctuations_3)}”\n\n"
        quotation = "no"
    else:
        poem += f"{stanza[:-2]}{choice(punctuations_3)}\n\n"
print(f"{poem}{choice(words[1:3])} mak")
