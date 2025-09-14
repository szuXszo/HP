import time
import os
import sys



def clear_terminal():
    """
    Törli a terminál korábbi tartalmát. Ha nem terminálban van futtatva,
    akkor 100 üres sort ír ki.
    """
    if not sys.stdout.isatty():
        print("\n" * 100)
    elif sys.platform.startswith('win'):  # Windows (cmd, PowerShell)
        os.system('cls')
    else:  # macOS/Linux
        os.system('clear')


def output_text_to_center(text):
    """
    A szöveget a terminál függőleges közepére írja ki, miután törölte a
    terminál korábbi tartalmát. Ha nem terminálban van futtatva (pl.
    PyCharmban), akkor 100 üres sor után írja ki a szöveget.
    :param text: string.
    :return: string, amely a bemenetként megadott szöveg plusz az előtte
    lévő üres sorok (\n) annak érdekében, hogy középen legyen a szöveg.
    """
    clear_terminal()
    if not sys.stdout.isatty():
        print(text)
    else:
        try:
            terminal_height =  os.get_terminal_size().lines
            padding = terminal_height // 2 - 4
            print("\n" * padding + text)
        except OSError:
            print("\n" * 8 + text)

output_text_to_center("DEKÁZOK A LEMENŐ NAPBAN")
time.sleep(3)

for k in range(5):
    output_text_to_center(f"{'\n' * k}O{'\n' * (5 - k)}          O")
    time.sleep(1)
    output_text_to_center(f"          O{'\n' + ('\n' * k)}O{'\n' * (4 - k)}")
    time.sleep(1)
output_text_to_center(f"{5 * '\n'}          O")
time.sleep(2)

