from random import sample


statements = ["Alkoholista lett", "Elhagyta a felesége", "A főnöke kirúgta",
              "Elbukta a befektetéseit"]

print("ÍGY JÁRT\n")
statements = sample(statements, len(statements))
for count, statement in enumerate(statements):
      if count == 0:
            print(f"{statement},")
      elif count == 1:
            print(f"emiatt {statement.lower()},")
      elif count == 2:
            print(f"ezért {statement.lower()},")
      elif count == 3:
            print(f"emiatt {statement.lower()}.")

