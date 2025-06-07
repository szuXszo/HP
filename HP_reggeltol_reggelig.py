import time


def extend_characters(characters, direction, num_same_lines,  sleep, times):
    for n in range(times):
        for n in range(len(characters)):
            if direction == "+":
                new_characters = characters[:n + 1]
            elif direction == "-":
                new_characters = characters[:len(characters) - n]
            for n in range(num_same_lines):
                print(new_characters)
                time.sleep(sleep)


def wave_characters(characters, num_same_lines,  sleep, times):
    for n in range(times):
        extend_characters(characters, "+", num_same_lines, sleep, 1)
        extend_characters(characters, "-", num_same_lines, sleep, 1)


def open_characters(characters1, characters2, direction, max_space, num_same_lines,  sleep, times):
    for n in range(times):
        for n in range(max_space):
            if direction == "+":
                space = " " * n
                new_characters = f"{characters1}{space}{characters2}"
            elif direction == "-":
                space = " " * (max_space - n)
                new_characters = f"{characters1}{space}{characters2}"
            for n in range(num_same_lines):
                print(new_characters)
                time.sleep(sleep)


def open_and_close_characters(characters1, characters2, max_space, num_same_lines,  sleep, times):
    for n in range(times):
        open_characters(characters1, characters2, "+", max_space, num_same_lines,  sleep, 1)
        open_characters(characters1, characters2, "-", max_space, num_same_lines,  sleep, 1)


def open_path(characters1, characters2, direction, max_space, num_same_lines, sleep, times):
    for n in range(times):
        for n in range(max_space):
            if direction == "+":
                space = " " * n * 2
                new_characters = f"{characters1[:len(characters1) - n]}{space}{characters2[n:]}"
            elif direction == "-":
                space = " " * (((max_space - 1) * 2) - (n * 2))
                if len(space) != 0:
                    new_characters = f"{characters1[:(len(space) // 2) * -1]}{space}{characters2[len(space) // 2:]}"
                else:
                    new_characters = f"{characters1}{characters2}"
            for n in range(num_same_lines):
                print(new_characters)
                time.sleep(sleep)


def open_and_close_path(characters1, characters2, max_space, num_same_lines,  sleep, times):
    for n in range(times):
        open_path(characters1, characters2, "+", max_space, num_same_lines,  sleep, 1)
        open_path(characters1, characters2, "-", max_space, num_same_lines,  sleep, 1)


def output_window(characters, sleep):
    space = (" " * len(characters))[8:]
    for n in range(12):
        if n < 3 or n > 8:
            print(characters)
            time.sleep(sleep)
        elif n < 9:
            print(f"{characters[:4]}{space}{characters[-4:]}")
        time.sleep(sleep)


def output_face(characters, sleep):
    eye = " " * 5
    mouth = " " * 20
    for n in range(11):
        if n < 2 or 7 > n > 3 or n > 8:
            print(characters)
            time.sleep(sleep)
        elif 1 < n < 4:
            print(f"{characters[:6]}{eye}{characters[11:25]}{eye}{characters[30:]}")
        elif 9 > n > 6:
            print(f"{characters[:8]}{mouth}{characters[28:]}")
        time.sleep(sleep)

face_mirror = "meglátommagamatükörbenmeglátommagama"
face_window = "váratlanulegyembervisszanézrámváratl"
face_monitor = "újkollégávalbővültacsapatújkollégáva"
face_wall = "nézemazárnyékomatafalonnézemazárnyék"

window_window = "azablakonátnézekasemmibeazablakonátn"
window_monitor = "aképernyőnátnézekasemmibeaképernyőná"
window_fridge = "ahűtőszekrényisüresahűtőszekrényisür"
window_ceiling = "nézemaplafontnézemaplafontnézemaplaf"

shade = "lehúzomaredőnytlehúzomaredőnytlehúzo"

steps_bath1 = "kimegyeka"
steps_bath2 = "fürdőszobába"
steps_room1 = "visszamegyek"
steps_room2 = "aszobába"
steps_neighbour1 = "aszomszédfölle"
steps_neighbour2 = "járkálfelettem"
steps_toilet1 = "vécéremegyek"
steps_toilet2 = "vécéremegyek"
steps_drinking1 = "kimegyekegy"
steps_drinking2 = "pohárvízért"

path_clock1 = "nézemahogytelnek"
path_clock2 = "azóránamásodpercek"

text_clock = "hallgatomazébresztőórát"
text_sleep = "megpróbálokelaludni"
text_cities = "összeszámolom, hogy hány megyeszékhelyen voltam"
text_mails = "összeszámolom, hogy hány embernek írtam ímélt az utóbbi héten"
text_error = "elrontottam, elölről kezdem"
text_power = "egytől haladva egyesével négyzetre emelem a számokat"


print("REGGELTŐL REGGELIG\n")
time.sleep(3)

extend_characters(text_clock, "+", 1, 0.15, 3)
extend_characters(text_clock, "+", 1, 0.05, 3)
extend_characters(text_clock, "+", 1, 0.025, 6)
extend_characters(text_clock, "+", 1, 0.01, 12)

open_characters(steps_bath1, steps_bath2, "+", 15, 1,  0.1, 3)
open_characters(steps_bath1, steps_bath2, "+", 15, 1,  0.04, 4)
time.sleep(1)
print()

output_face(face_mirror, 0.05)
time.sleep(6)
print()

open_characters(steps_room1, steps_room2, "+", 15, 1,  0.1, 3)
open_characters(steps_room1, steps_room2, "+", 15, 1,  0.04, 4)
time.sleep(2)
print()

output_window(window_monitor, 1)
time.sleep(2)
print()

output_face(face_monitor, 0.01)
time.sleep(6)
print()

open_and_close_path(path_clock1, path_clock2, 15, 1, 0.05, 5)
time.sleep(4)
open_and_close_path(path_clock1, path_clock2, 15, 1, 0.05, 5)
time.sleep(4)
print()

open_and_close_characters(steps_toilet1, steps_toilet2, 15, 1,  0.08, 3)
open_and_close_characters(steps_toilet1, steps_toilet2, 15, 1,  0.04, 4)
time.sleep(2)
print()

output_face(face_wall, 0.05)
time.sleep(4)
print()

open_and_close_characters(steps_drinking1, steps_drinking2, 15, 1,  0.08, 3)
open_and_close_characters(steps_drinking1, steps_drinking2, 15, 1,  0.04, 4)
time.sleep(2)
print()

output_window(window_fridge, 0.5)
time.sleep(2)
print()

open_characters(steps_neighbour1, steps_neighbour2, "+", 15, 1,  0.1, 3)
open_characters(steps_neighbour1, steps_neighbour2, "+", 15, 1,  0.04, 9)
time.sleep(1)
print()

output_window(window_monitor, 1)
time.sleep(2)
print()

open_and_close_characters(steps_toilet1, steps_toilet2, 15, 1,  0.08, 3)
open_and_close_characters(steps_toilet1, steps_toilet2,15, 1,  0.04, 4)
time.sleep(2)
print()

output_window(window_window, 0.5)
time.sleep(2)
print()

output_face(face_window, 0.01)
time.sleep(5)
print()

for n in range(12):
    print(shade)
    time.sleep(0.5)
time.sleep(3)
print()

output_window(window_ceiling, 0.5)
time.sleep(3)
print()

wave_characters(text_sleep, 1,  0.1, 6)
print(f"\n{text_mails}\n")
time.sleep(3)
for n in range(1, 20):
    print(n)
    time.sleep(1)
wave_characters(text_sleep, 1,  0.1, 6)
print(f"\n{text_cities}\n")
time.sleep(3)
for n in range(1, 7):
    print(n)
    time.sleep(2)
print(f"\n{text_error}\n")
time.sleep(2)
for n in range(1, 10):
    print(n)
    time.sleep(2)
print(f"\n{text_power}\n")
time.sleep(2)
for n in range(1, 11):
    print(n * n)
    time.sleep(1)
print("?")
time.sleep(1)
print()

extend_characters(text_clock, "+", 1, 0.15, 3)
extend_characters(text_clock, "+", 1, 0.05, 3)
extend_characters(text_clock, "+", 1, 0.025, 6)
extend_characters(text_clock, "+", 1, 0.01, 12)





