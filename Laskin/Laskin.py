print("------------------TERVETULOA LASKINOHJELMAAN-------------------")

while True:
    print("Valitse mitä toimintaoa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q = Lopeta ohjelma")
    valinta = input("Anna valintasi: ").upper()
#virheellinen valinta, tähän kohtaan. kun se liittyy yllä oleviin valintoihin
    if valinta == "Q":
        print("Poistutaan....")
        break
    
    a = float(input("Anna ensimmäinen luku: "))
    b = float(input("Anna toinen luku: "))

    if valinta == "A":
        print(f"Lukujen {a} ja {b} summa on {a+b}.")
    elif valinta == "B":
        print(f"Lukujen {a} ja {b} erotus on {a-b}.")
    elif valinta == "C":
        print(f"Lukujen {a} ja {b} tulo on {a*b}.")
    elif valinta == "D":
        print(f"Lukujen {a} ja {b} osamäärä on {a/b}.")
    else:
        print("virheellinen valinta.")

print("Ohjelma päättynyt.")
      