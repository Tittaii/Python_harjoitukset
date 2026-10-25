# Kirjoita ohjelma, joka pyytää käyttäjää syöttämään arvoja ja lisää ne listaan. 
# Jokaisen lisäyksen jälkeen lista tulostetaan kahdella tavalla: lisäysjärjestyksessä ja pienimmästä suurimpaan järjestettynä. 
# Ohjelma lopettaa, kun käyttäjä syöttää 0.


numerot=[]

while True:
    luku = int(input("anna arvo: "))
    numerot.append(luku)
    print(numerot)

    numerot.sort()
    print(numerot)

    if luku == 0:
        print("syötit arvon 0, ohjelma loppuu.")
        break

