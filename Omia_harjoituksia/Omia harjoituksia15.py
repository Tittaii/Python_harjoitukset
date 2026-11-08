

#määritelmä
def vaihda():
    kaupunki = "vantaa" #kaupunki tämä on lokaali muuttuja
    print("funkiossa lopuksi: " + kaupunki)
    return


#pääohjelma"
kaupunki = "helsinki" #kaupunki tämä on globaali muuttuja
print("globaalin kaupungin nimi: " + kaupunki)
vaihda()
print("globaalin kaupungin nimi: " + kaupunki)


#globaalit muuttujan on näkyvissä kaikkialle, lokaalit eli paikalliset muuttujat ovat olemassa vain funktuin määritelmän sisällä!! kaksi eri asiaa

#alaviivalla helppo erottaa _kaupunki lokaali muuttuja, kaupunki globaali muuttuja

#huom! nämä kokonaan muistiinpanoja

#GLOBAALIA MUUTTUJAA VOI KÄYTTÄÄ FUNKTIOSSA, MUTTA PAIKALLISTA MUUTTUJAA (FUNKTION SISÄLL OLEVAA)
#MUUTTUJAA EI VOI KÄYTTÄÄ PÄÄOHJELMASTA.
#GLOBAALI NÄKYY KAIKKIALLE! LOKAALI VAIN MUUTTUJASSA.


