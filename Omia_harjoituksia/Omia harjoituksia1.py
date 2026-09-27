#yksinkerainen toistorakenne

#alustetaan muuttujat

hinta = 5
kolikot = 0

while True:
    #päivitetään ehtoa    #ehto on aina totta, tarvitaan ehto jotta siitä päästään ulos, if kolikot == ...
    kolikot += 1
    print("Annettu", kolikot, "kolikkoa")

#tarkistetaan ehto
    if kolikot == hinta:    #tarkastetaan 5 on yhtä kuin 5
        break

print("kiitos näkemiin!")

#ehdollinen toistorakenne, käytetään jos on tarkka määrä esim kolikoita tiedossa
#testaa molemmilla tavoilla kotiläksyjä, suosi ehdollista toistorakennetta!!!