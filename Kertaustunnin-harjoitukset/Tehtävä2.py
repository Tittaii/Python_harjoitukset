#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaisluvun. Jos luku on jaollinen kolmella, ohjelma tulostaa ”kolmella jaollinen”. 
# Jos luku on jaollinen viidellä, ohjelma tulostaa "viidellä jaollinen". 
# Jos luku on jaollinen sekä kolmella että viidellä, ohjelma tulostaa ”jaollinen molemmilla luvuilla!". 


kokonaisluku = int(input("anna kokonailuku: "))

if kokonaisluku % 3 == 0 and kokonaisluku % 5 == 0:
    print ("jaollinen molemmilla luvuilla!")

elif kokonaisluku % 5 == 0:
    print("viidellä jaollinen")

elif kokonaisluku % 3 == 0:
    print ("kolmella jaollinen")



