# lukuja pyydettäessä, kunnes tyhjä merkkijono lopettaa sen, kirjaa isoimmat ja pienimmät luvut

komento = input("anna luku: ")

while komento!="lopeta":
    if komento=="":
        break
    print("luku: ", komento)
    komento =input ("anna luku: ")

print ("tyhjä merkkijono, ohjelma päättyy")

###en ymmärrä kuinka saan tähän lajiteltua pienimmän ja suurimman luvun "muistin" kuinka se tähän vielä tulostuisi