#Kirjoita ohjelma, joka kysyy käyttäjältä viiden kaupungin nimet yksi kerrallaan (käytä for-toistorakennetta nimien kysymiseen) 
# ja tallentaa ne listarakenteeseen. 
# Lopuksi ohjelma tulostaa kaupunkien nimet yksi kerrallaan allekkain samassa järjestyksessä kuin ne syötettiin. 
# käytä for-toistorakennetta nimien kysymiseen ja for/in toistorakennetta niiden läpikäymiseen.

kaupungit = []

for kysely in range(5):
    kaupunki = input("anna kaupungin nimi: ")
    kaupungit.append(kaupunki)

print("kaupungit ovat: ")
for kaupunki in kaupungit:
    print(kaupunki)

print("kysely päättyy.")
