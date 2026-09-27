# peli, jossa tietokone arpoo kokonaisluvun väliltä 1-10

import random

luku=random.randint(1,10)

arvaus=int(input("arvaa luku 1-10: "))

while arvaus !=luku:

    if arvaus < luku:
        print("liian suuri arvaus")

    elif arvaus > luku:
        print("liian pieni arvaus")
    
    luku = int(input("arvaa uudelleen: "))

print("oikein")