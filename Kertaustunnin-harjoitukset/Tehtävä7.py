# Kirjoita ohjelma, joka laskee, kuinka monessa sanassa listassa on enemmän kuin 5 kirjainta. 
# Luo lista itse ja käytä len()-funktiota sanojen pituuden tarkistamiseen.

kaupunkilinnut = ["pulu", "lokki", "harakka", "naakka", "talitintti", "varis", "sorsa", "joutsen"]

for lintu in kaupunkilinnut: 
    if len(lintu) >5: 
        print("Lintu, jonka nimessä on enemmän kuin 5 kirjainta:", lintu)