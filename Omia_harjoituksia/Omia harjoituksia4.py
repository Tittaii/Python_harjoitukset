
#while/else.... tämä kesken!!!!

komento = input("anna uusi komento; ")

while komento != "lopeta":
    if komento == "mayday":
        break
    print("suoritetaan komento:", komento)
    komento = input("anna uusi komento: ")

else: 
    print("tämä ")