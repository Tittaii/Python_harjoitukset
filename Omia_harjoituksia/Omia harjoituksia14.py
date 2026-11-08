


def tervehdi(tervehdys, kerrat):
    for i in range(kerrat): #kerrat parametri
        print(tervehdys+ str(i+1) + ". kerran.") #str(i+1) tämä muokkaa sulkeiden sisällä olevan numeron merkkijonoksi 
    return

#pääohjelma

print("Testataan tervehdys-funkiota:")
tervehdi("Moi", 3) #argumentti
print("Testataan vielä varmistukseksi..")
tervehdi("Hello!", 5) #argumentti pitää antaa joka kerran kun sitä kutsuu

#parametrejä voi olla niin paljon kuin tarvitsee