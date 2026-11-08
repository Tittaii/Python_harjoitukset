#määritellään funktio ennen kuin sitä voi kutsua, funktio pitää määritellä jotta se tekee jotain, muista tämä!

def tervehdi(kerrat):
    for i in range(kerrat): #kerrat parametri
        print("Hyvää päivää " + str(i+1) + ". kerran.") #str(i+1) tämä muokkaa sulkeiden sisällä olevan numeron merkkijonoksi 
    return

#pääohjelma

print("Testataan tervehdys-funkiota:")
tervehdi(3) #argumentti
print("Testataan vielä varmistukseksi..")
tervehdi(5) #argumentti pitää antaa joka kerran kun sitä kutsuu


def keskiarvo(luku):
    for i in range(luku):
    print("keskiarvo on " + str(i+1) + ". kerran. ")
    return

luku1 = int (input ("anna luku:"))
luku2 = int (input ("anna luku:"))
luku3 = int (input ("anna luku:"))

