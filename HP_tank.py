# Ezt parancssorban érdemes futtatni, teljes képernyőn.

import time
import textwrap
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


output_text_to_center("A barátnőnmnek vettem egy tankot,")
time.sleep(3)
output_text_to_center("""
     @@@@@@@
    @@@@@@@@@ 
   @@@@ o o @@                     
   @@@   V   @@@                
  @@     O  @@@           
         I                                                
         I                                               
         I                  
         I__              
""")
time.sleep(3)
tank = """  
          ggggggg  
        ggggggggggggggggggggggggggggggggg
       gggggggggggg
  gggggggggggggggggggggggg                                
  gggggggggggggggggggggggg                               
  gggggggggggggggggggggggg  
  gggg                gggg
"""
output_text_to_center(tank)
time.sleep(2)
output_text_to_center("""
                      ggggggg  
                    ggggggggggggggggggggggggggggggggg
                   gggggggggggg
             gggggggggggggggggggggggg                                
   //}       gggggggggggggggggggggggg                               
    |        gggggggggggggggggggggggg  
    L        gggg                gggg
""")
time.sleep(2.5)
output_text_to_center("hogy ne kelljen a buszon ücsörögnie a reggeli dugóban,")
time.sleep(3)
vehicles = """
                 :::::::::::::::::::
 ______          ::   ::     ::   ::
 |_____\\___      :::::::::::::::::::         __________         
{   ____   |     :::::::::::::::::::      __ |_________\\____ 
 (o)    (o)      :::     :::     :::     J ::           ::  l
 """
output_text_to_center(vehicles)
time.sleep(2)
for i in range(4):
    vehicles = textwrap.indent(vehicles, "   ")
    output_text_to_center(vehicles)
    time.sleep(2)

output_text_to_center(tank)
time.sleep(0.2)
for i in range(7):
    tank = textwrap.indent(tank, "     ")
    output_text_to_center(tank)
    time.sleep(0.2)
time.sleep(0.5)
output_text_to_center("és így már a rosszemberektől sem fél.")
time.sleep(3)
output_text_to_center("""
                               _______
g                             |       |
gg                            |_______|___
ggggggggggggggggggggggg         O   O
ggggggggggggggggggggggg           U
ggg                              lll
gg                                C     Ich will ein Reich    
""")
time.sleep(3)
output_text_to_center("Azóta jól alszik,")
time.sleep(2.5)
output_text_to_center("nem álmodik távoli bolygók lakóiról")
time.sleep(2.5)
output_text_to_center("""
         Y  Y                 
         O  O       
          ()           
          ___                                                                
			                                                            
      |___III___|
         IIIII
         |   |
""")
time.sleep(2)
output_text_to_center("és lefejezett emberekről.")
time.sleep(2)
output_text_to_center("""
              o o    o o    |     |                    __|__  
. .    . .     u      v     |     |     (.. )    o o     |    
 c      C      _      O     L    / \\    ( o )     &     / \\   
""")
time.sleep(5)
