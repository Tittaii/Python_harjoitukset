


def inventaario(tavarat):
    print("sinulla on seuraavat tavarat: ")
    for t in tavarat:
        print("- " + t)
        tavarat.clear() #tällä tyhjennetään aluperäinen lista!
        return

reppu = ["kartta", "juomapullo", "kompassi"]
inventaario(reppu)
reppu.append("sämpylä")
inventaario(reppu)

# selvitä miksi reppuun ei tule kuin kartta??? juomapullo ja kompassi jää puuttumaan