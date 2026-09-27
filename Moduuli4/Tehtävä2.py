# Tuumista senteiksi

while True:
    luku = int(input("anna luku senttimetreinä: "))

    tuuma = luku*2.54

    if tuuma < 0:
        print("negatiivinen tuumamäärä, ohjelma loppuu.")
        break

    print("senttimetrit on tuumina:", tuuma )
