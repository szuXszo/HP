# Minden generáláshoz újra kell futtatni.

from random import choice

time = ["Száz évvel", "Tizenötmilliárd évvel", "Hétezer évvel", "Harminchét évvel",
        "Három nappal", "Három másodperccel", "Százhuszonhét emberöltővel",
        "Harminchárom emberöltővel", "10823 éjszakával és 10822 nappallal",
        "154722 holdtöltével", "154721 holdfogyatkozással", "Sokszázezer évvel",
        "Tízezer holdévvel", "Hatezer tavasszal", "Tízezer hajnallal",
        "Hetvenkét aranykorral"]

actor = ["egy isten", "az isten", "az ördög", "egy kitagadott isten",
         "egy bizonyítani akaró bizonytalan félisten", "egy ügyes technikus",
         "egy agilis mérnökinformatikus", "egy tehetségtelen költő",
         "egy megtagadott amazon", "egy az övéitől elkóborolt kentaur",
         "egy halandóságra vágyó halhatatlan", "az űr megtévedt hajósa",
         "egy magányos szellem", "egy eltévedt égi lovas", "egy elaggott sárkány",
         "egy tüzet izzadó farkas", "egy szuperintelligencia",
         "egy gyémántszemű orángután", "egy gyöngyhajú tündér",
         "az egek királyának eltaszított menyasszonya", "egy háromfejű isten"]

state = ["mielőtt lelkét kilehelte", "munkájában megpihenve",
         "munkájában megfáradva", "dologtalanságában", "álmatlanul hánykolódva",
         "végtelen bánatában", "időtlen bánatában", "saját magától megrészegedve",
         "erejét és találékonyságát fitogtatva", "kicsinyes bosszúból",
         "magát mindenkinél jobbnak gondolva", "önmagától eltelve",
         "szeretőjétől elválva", "sorsát siratva", "magát vígasztalva",
         "színtiszta gonoszságtól vezérelve", "mérhetetlen szomorúságában",
         "beváltva egykori ígéretét", "vígasztalhatatlanságában"]

action = ["bolygókat és csillagokat böfögött az űrbe",
          "elválasztotta a fényt a sötétségtől",
          "körbekerítette az űr egy kicsiny szegletét",
          "könnyeivel permetezte a kietlen sivatagot",
          "ürülékéből embernek mondott lényeket alkotott",
          "néven nevezte a megnevezhetetlent",
          "szeme sugarával felolvasztotta a végtelen jégmezőket",
          "csillagporral hintette kedvese arcát",
          "csillogó könnyeivel borította az eget",
          "dalra fakadt és megrepesztette a kongó falakat",
          "embereket alkotott, hogy örökös terhét cipeljék",
          "négyszögesítette a kört", "meghajlította az egyenest",
          "véres szívét az égre akasztotta", "pénzre váltotta emlékeit",
          "pénzzé tette minden kincsét", "megmutatta magát gyermekeinek",
          "halállal fertőzte az ismert és ismeretlen csillagrendszereket",
          "vérével öntözte a kopár sziklákat", "belenézett a nap tükrébe"]

print(f"APOKRIF\n\n{choice(time)} ezelőtt\n{choice(actor)}\n{choice(state)}\n"
      f"{choice(action)}.")


