#käyttäjätunnus ja salasana

käyttäjätunnus_salasana = input("anna käyttäjätunnus ja salasana: ")
yritykset = 0

while käyttäjätunnus_salasana != "titta 5555" and yritykset <5:
    print("pääsy evätty")
    yritykset += 1

    if yritykset == 5:
        break

    käyttäjätunnus_salasana = input("anna käyttäjätunnus ja salasana: ")

if käyttäjätunnus_salasana == "titta 5555":
    print("tervetuloa! ")

print("ohjelma päättyy")