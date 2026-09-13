pituus =int(input("kuinka pitkä kuha on senttimetreinä?"))

if pituus >= 37:
    print("kuha on oikean mittainen, voit pitää sen")
else:
    print("kuhan pituudesta puuttuu senttejä", 37-pituus)

    print ("kuha on alamittainen, laske se takaisin järveen")
