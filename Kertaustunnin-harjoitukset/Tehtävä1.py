# if - elif - else: 
# Kirjoita ohjelma, joka kysyy tuntipalkan, tehdyt tunnit ja viikonpäivän. 
# Ohjelma tulostaa päiväpalkan, joka on tuntipalkka kerrottuna tehdyillä tunneilla, paitsi sunnuntaina, jolloin tuntipalkka on kaksinkertainen.


tuntipalkka = int(input("Anna tuntipalkkasi €: "))

työtunnit = int(input("montako tuntia työskentelit: "))

viikonpäivä = input("minä päivänä työskentelit: ")

if viikonpäivä == "maanantai" :

    palkka= tuntipalkka*työtunnit

    print("palkkasi on: ", palkka ,"euroa")

elif viikonpäivä == "tiistai" :

    palkka= tuntipalkka*työtunnit

    print("palkkasi on: ", palkka ,"euroa")

elif viikonpäivä == "keskiviikko" :

    palkka= tuntipalkka*työtunnit

    print("palkkasi on: ", palkka ,"euroa")

elif viikonpäivä == "torstai" :

    palkka= tuntipalkka*työtunnit

    print("palkkasi on: ", palkka ,"euroa")

elif viikonpäivä == "perjantai" :

    palkka= tuntipalkka*työtunnit

    print("palkkasi on: ", palkka ,"euroa")

elif viikonpäivä == "lauantai" :

    palkka= tuntipalkka*työtunnit

    print("palkkasi on: ", palkka ,"euroa")

elif viikonpäivä == "sunnuntai" :

    palkka= (tuntipalkka*työtunnit)*2

    print("palkkasi on: ", palkka ,"euroa")

else:
    print ("väärä tieto, anna tiedot uudelle, kiitos!")





    

     


    



