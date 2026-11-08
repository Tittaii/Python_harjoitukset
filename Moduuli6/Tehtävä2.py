#Muokkaa edellistä funktiota siten, että funktio saa parametrinaan nopan tahkojen yhteismäärän. 
# Muokatun funktion avulla voit heitellä esimerkiksi 20-tahkoista roolipelinoppaa. 
# Edellisestä tehtävästä poiketen nopan heittelyä jatketaan pääohjelmassa kunnes saadaan nopan maksimisilmäluku, 
# joka kysytään käyttäjältä ohjelman suorituksen alussa.

import random

def heita_noppaa(tahko):
    luku = random.randint(1,tahko)
    return luku

tahkojen_maara=int(input("moni tahkoista noppaa haluat heittää?: "))

while True:
    luku = heita_noppaa(tahkojen_maara)  
    print(luku)

    if luku == tahkojen_maara:
        break

print("ohjelma päättyy")