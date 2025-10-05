from random import choice


print("NYERŐGÉP 2 – transzgender verzió\n")

print(choice(["gyerekkel       ", "keserűséggel    ", "hittel          "]),
      choice(["érkezik         ", "távozik         "]),
      choice(["a kórteremből   ", "a lakásodból    ", "a miséről       "]))

print(choice(["érkezik         ", "távozik         "]),
      "mint bukott     ",
      choice(["férfi           ", "nő              "]))

print(choice(["a kórterembe    ", "a lakásodba     ", "a misére        "]),
      choice(["férfi           ", "nő              "]),
      choice(["érkezik         ", "távozik         "]))
