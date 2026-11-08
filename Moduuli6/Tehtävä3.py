# Kirjoita funktio, joka saa parametrinaan bensiinin määrän Yhdysvaltain nestegallonoina ja palauttaa paluuarvonaan vastaavan litramäärän. 
# Kirjoita pääohjelma, joka kysyy gallonamäärän käyttäjältä ja muuntaa sen litroiksi. 
# Muunnos on tehtävä funktiota hyödyntäen. 
# Muuntamista jatketaan siihen saakka, kunnes käyttäjä syöttää negatiivisen gallonamäärän. 
# Yksi gallona on 3,785 litraa. 

def bensan_maara(gallona):
    litrat=gallona*3.785
    return litrat


while True:
    gallona=float(input("montako gallonaa? "))

    if gallona < 0:
        print("negatiivinen gallonamäärä, kysely päättyy")
        break
        

    litrat = bensan_maara(gallona)
    print("gallonat on litroina: ", litrat)