# Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuja. 
# Jos luku on pienempi kuin nolla, ohjelma tulostaa viestin "Virheellinen numero". 
# Jos luku on suurempi kuin nolla, ohjelma tulostaa luvun neliöjuuren Pythonin sqrt-funktiolla. 
# Molemmissa tapauksissa ohjelma kysyy sen jälkeen uutta lukua. 
# Jos käyttäjä syöttää luvun nolla, ohjelma lopettaa kysymisen ja poistuu silmukasta. 
# 
# Esimerkki sqrt-funktion käytöstä:
# from math import sqrt 
# print(sqrt(9)) 

from math import sqrt 

while True:
    kokonaisluku = int(input("Anna luku: "))

    if kokonaisluku == 0:
        print("Ohjelma päättyy.")
        break

    elif kokonaisluku <= 0:
        print("Virheellinen numero.")
        
    else:
        print(sqrt(kokonaisluku))
