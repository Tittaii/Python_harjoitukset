print("------------------TERVETULOA LASKINOHJELMAAN-------------------")

while True:
    print("Valitse mitä toimintaa haluat käyttää:")
    print("A: Yhteenlasku, B: Vähennyslasku, C: Kertolasku, D: Jakolasku, Q = Lopeta ohjelma")
    valinta = input("Anna valintasi: ").upper()

    # kotitehtävä vastaus: 
    # testasin ja pohdin monta eri vaihtoehtoa minne laittaisin "virheellinen valinta" kohdan
    # jos se pitäisi laittaa jonnekin toiseen kohtaan missä se nyt on niin laittaisin sen suoraan tähän kohtaan valinta on tehty
    # miksi se olisi tuolla silmukassa viimeisenä missä se nyt on kun voisi olla suoraan tässä
    # en vain ymmärrä kuinka komento tähän kirjoitetaan, että se myös toimisi, mutta tämä olisi se kohta mihin sen laittaisin.
    # komennoksi kirjoittasin jotenkin siten, että jos valinta ei ole A, B, C, D, tai Q niin sitten tulostuu "virheellinen valinta" teksti


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


