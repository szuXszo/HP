from random import choice


emotions = ["Rettegést.", "Gyűlöletet.", "Szomorúságot.", "Magányt."]

elaboration = ["Záródó ajtók mögött önmagába visszatérő végtelen folyosókon "
               "ülök egy székben, kezemben jogar, fejemen a Szent Korona.",

               "Célját soha el nem érő, féligszületett gyermek mászik felém "
               "a sivatag homokjában.",

               "Ragyogó napként világítom be az egykorvolt, kopár téli tájat.",

               "Jégbefagyott óceánon állok én és a tükörképem a déli verőfényben.",

               "Egy sanghaji parkolóházban ülök a főnököm bérelt autójában, a "
               "szemközti audi fényszórója elvakítja a látásom.",

               "Háromszögbe szerkesztett kör, abban egy újabb háromszög, a "
               "háromszögben egy négyzet, de a négyzetben már nincs semmi.",

               "A szórakozóhelyen egy turista illetlenül viselkedik a hölgyvendégekkel. "
               "A biztonsági őr észleli a problémát és közbeavatkozik. A szóváltás "
               "során a turista nem ismeri el, hogy hibázott. A vita egyre hevesebbé "
               "válik. A turista láthatólag nem az első sörét issza. A biztonsági őr "
               "kikíséri a turistát a helyiségből. A turista megfenyegeti a biztosági "
               "őrt, hogy másnap a legénybúcsús haverjaival fog visszatérni. A "
               "biztonsági őr biztosítja, hogy várni fogja. De én nem a turista "
               "vagyok, és nem is a biztonsági őr, hanem csak a pultos."]


print("TERÁPIA\n")
print(f'-Megfogalmazná, hogy most mit érez?\n-{choice(emotions)}\n-Kicsit pontosítaná?\n'
      f'-{choice(elaboration)}\n-Köszönöm.')