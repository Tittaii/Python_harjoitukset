


def neliosumma(eka, toka):
    ns=eka**2+toka**2
    return ns

luku1= float(input("anna ensimmäinen luku: "))
luku2=float(input("anna toinen luku: "))
tulos=neliosumma(luku1, luku2)
print(f"lukujen neliösumma on: {tulos:.2f}")

    # funktion palauttaminen, arvo on käytettävissä pääohjelmasa kun se on tallennettu paluuarvona
    # 
    # samaa tulosta voi käyttää myöhemminkin              