#kirjoita ohjelma joka kysyy käyttjältä arpakuutioiden lukumäärän. Ohjelma heittaa kerran kaikkia arpakuutioita ja tulostaa silmälukujen summan

import random

numerot = []

määrä = int(input("monta arpakuutiota haluat heittää: "))

summa = 0

for heittokerta in range(määrä):
    heitto = random.randint(1,6)
    numerot.append(heitto)
    summa += heitto

    print("summa nyt: ", summa)

print("silmälukujen summa on: ", summa)