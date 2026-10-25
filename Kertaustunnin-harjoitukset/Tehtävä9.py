#Kirjoita ohjelma, joka simuloi tehtaan tuotantoa. Ohjelma kysyy käyttäjältä, mitä tuotetta valmistetaan ja kuinka monta kappaletta sitä valmistetaan. 
# Tallenna tuotteiden nimet ja määrät omiin listoihinsa.
# Tämän jälkeen ohjelma kysyy "Jatketaanko tuotantoa?". 
# Jos käyttäjä vastaa "Kyllä", ohjelma kysyy seuraavan tuotteen ja sen määrän. 
# Ohjelma jatkaa kysymistä, kunnes käyttäjä syöttää "Ei". 
# Kun tuotanto lopetetaan, ohjelma tulostaa kaikki valmistetut tuotteet ja niiden määrät. 

tuotteet = []

kappaleet = []

while True:
    tuote = input("mitä tuotetta valmistetaan: ")
 
    kappale = int(input("kuinka monta kappaletta tuotetta valmistetaan: "))

    tuotteet.append(tuote)
    kappaleet.append(kappale)

    valmistus = input("jatketaanko tuotantoa? ")

    if valmistus == "kyllä":

        tuote = input("mitä tuotetta valmistetaan: ")
         
        kappale = int(input("kuinka monta kappaletta tuotetta valmistetaan: "))
        
        tuotteet.append(tuote)
        kappaleet.append(kappale)
        
        valmistus = input("jatketaanko tuotantoa? ")

    elif valmistus == "ei":
        print("valmistus päättyy")
        break
            
print("valmistetut tuotteet: ", tuotteet)
print("valmistetut kappaleet: ", kappaleet)

