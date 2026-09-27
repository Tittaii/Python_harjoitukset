#TOISTON PYSÄYTTÄMINEN  ..... tilanne kun käyttäjä päättää toiston, looppi pyörähtää niin kauan kunnes käyttäjä antaa lopetus käskyn

komento = input("Anna uusi komento: ")  #tämä kysymys käynnistää silmukan

while komento != "lopeta":                      #järjestys näin koska muuttuja täytyy määrittää, ensin meidän täytyy määrittää komennto , kysyttävä silmukassa uudelleen
    print("suoritetaan komento:", komento)
    komento = input("Anna uusi komento: ")   #tämä pitää olla myös täällä, muuten tulee ikuinen looppi!!!!

print("ohjelma loppuu.")
