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


meeting1 = (
""" EGYDIMENZIÓS EMBEREK ÜZLETI TALÁLKOZÓJA\n\n
               |  |\n\n""")

skiers = (
""" SÍELŐ EGYDIMENZIÓS EMBEREK\n
         L
                         L
                         
                 L""")

porn = (
""" PORNÓJELENET EGYDIMENZIÓS EMBEREKKEL\n\n
                 _\n\n""")

human_centipede = (
""" EMBERI SZÁZLÁBÚ EGYDIMENZIÓS EMBEREKKEL\n\n\n
             ____________\n""")

meeting2 = (
""" EGYDIMENZIÓS EMBEREK ROMANTIKUS TALÁLKOZÓJA\n\n
                 ||\n\n""")

dancers = (
""" EGYMÁSSAL TÁNCOLÓ KÉT EGYDIMENZIÓS EMBER\n\n
                 |\n\n""")

family = (
""" EGYDIMENZIÓS EMBERPÁR GYEREKKEL\n\n
                 A\n\n""")

water = (
""" VÍZEN JÁRÓ EGYDIMENZIÓS EMBER\n\n
   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  ~~~~~~~~~~~~~~~|~~~~~~~~~~~~~~~
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")

sermon1 = (
""" HEGYIBESZÉD EGYDIMENZIÓS EMBEREKNEK\n
    |
    
    
                 ||||||||||||""")

sermon2 = (
""" HEGYIBESZÉD EGYDIMENZIÓS EMBEREKNEK – FELÜLRŐL\n\n
    .            ............\n\n""")

mirror = (
""" TÜKÖRBENÉZŐ EGYDIMENZIÓS EMBER\n\n
                | |\n\n""")

cross = (
""" KERESZTRE FESZÍTETT EGYDIMENZIÓS EMBER\n\n
                 +\n\n""")

grave = (
""" TÖMEGSÍR EGYDIMENZIÓS EMBEREKKEL\n\n\n\n
                 _""")

black_hole1 = (
""" FEKETELYUK KÖZELÉBEN ELHALADÓ EGYDIMENZIÓS EMBER\n\n
                 C\n\n""")

black_hole2 = (
""" FEKETELYUK KÖZELÉBEN ELHALADÓ EGYDIMENZIÓS EMBEREK RAJA\n
               C   C        
             C    C   C    
            C   C   C   C   
              C   C  C""")

last_judgement = (
""" UTOLSÓ ÍTÉLET EGYDIMENZIÓS EMBEREKKEL\n
 |||||||||||\n\n
                   |||||||||||""")

output_text_to_center(" EGYDIMENZIÓSEMBER-CIKLUS\n\n\n\n\n"
                      " A továbblépéshez nyomj mindig egy entert.")
input()
scenes = [meeting1, skiers, porn, human_centipede, meeting2, dancers, family,
          water, sermon1, sermon2, mirror, cross, grave, black_hole1, black_hole2,
          last_judgement, "\n\n               VÉGE\n\n"]
for scene in scenes:
    output_text_to_center(scene)
    input()

