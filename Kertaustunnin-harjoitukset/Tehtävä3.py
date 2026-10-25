#Kirjoita ohjelma, joka simuloi tuotantolinjan toimintaa. Ohjelma tulostaa viestin "Tuote valmistettu!" 
# ja kysyy sen jälkeen "Jatketaanko tuotantoa?" niin kauan, kunnes käyttäjä syöttää "Ei". 
# Tämän jälkeen ohjelma tulostaa "Tuotanto lopetettu!" ja päättyy

print("tuote valmistettu! ")

komento = input ("jatketaanko tuotanto? ")

while komento != "ei":
    print("jatketaanko tuotantoa? ")
    komento = input ("jatketaanko tuotanto? ")
    
print("tuotanto lopetettu")


