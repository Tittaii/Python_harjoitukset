#Kirjoita ohjelma, joka kysyy käyttäjältä lukuja siihen saakka, kunnes tämä syöttää tyhjän merkkijonon lopetusmerkiksi. 
# Lopuksi ohjelma tulostaa saaduista luvuista viisi suurinta suuruusjärjestyksessä suurimmasta alkaen.  

# Vihje: listan alkioiden lajittelujärjestyksen voi kääntää antamalla sort-metodille argumentiksi reverse=True. 

numerot = []

while True:

    luku = input("anna luku: ")
    if luku == "":
        break
    numerot.append(int(luku))

numerot.sort(reverse=True)

print("viisi suurinta lukua on:", numerot[:5] )