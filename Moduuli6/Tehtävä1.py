# Kirjoita parametriton funktio, joka palauttaa paluuarvonaan satunnaisen nopan silmäluvun väliltä 1-6. 
# Kirjoita pääohjelma, joka heittää noppaa niin kauan kunnes tulee kutonen. 
# Pääohjelma tulostaa kunkin heiton jälkeen saadun silmäluvun. 

import random

def heita_noppaa():
    luku = random.randint(1,6)
    return luku

while True:
    luku = heita_noppaa()  
    print(luku)

    if luku == 6:
        break

print("ohjelma päättyy")