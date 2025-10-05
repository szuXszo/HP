from random import choice


print("NYERŐGÉP\n")

print(choice(["arannyal        ", "keserűséggel    ", "hittel          "]),
      choice(["érkezik         ", "távozik         "]),
      choice(["a pokolból      ", "a lakásodból    ", "a tengerpartról "]))

print(choice(["érkezik         ", "távozik         "]),
      "mint bukott     ",
      choice(["angyal          ", "ördög           "]))

print(choice(["a pokolba       ", "a lakásodba     ", "a tengerpartra  "]),
      choice(["angyal          ", "ördög           "]),
      choice(["érkezik         ", "távozik         "]))
