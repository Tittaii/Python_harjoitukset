# Kirjoita ohjelma, jossa on lista viiden tuotteen valmistuskustannuksista. 
# Ohjelma käy kustannukset läpi for-silmukan avulla ja tulostaa jokaisen kustannuksen. 
# Samalla ohjelma laskee kaikkien tuotteiden valmistuskustannukset yhteen. 
# Lopuksi ohjelma tulostaa kokonaiskustannuksen. 
# Esimerkki ohjelman tulostuksesta: 
# Tuotteen valmistuskustannus: 12.5 € 
# Tuotteen valmistuskustannus: 8.2 € 
# Tuotteen valmistuskustannus: 15.0 € 
# Tuotteen valmistuskustannus: 6.5 € 
# Tuotteen valmistuskustannus: 10.8 € 
# Valmistuskustannukset yhteensä: 53.0 € 

kustannukset = [12.5, 8.2, 15.0, 6.5, 10.8]

summa = 0
                
for kustannukset in kustannukset: 

    print("tuotteen valmistukustannus:" , kustannukset, "€") 

    summa += kustannukset

print("valmistuskustannukset yhteensä: ", summa, "€")








