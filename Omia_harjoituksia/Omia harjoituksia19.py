


def tervehdi(nimi):
    print("Morjens, " +nimi)
    return

def tervehdi_monesti(_nimi, kerrat): #heidi tallennetaan nimi paramentriin, huom! ei ole sama muuttuja alaviiva nimi! 
    while kerrat > 0:
        tervehdi(_nimi)
        kerrat -= 1
    return

#pääohjelma

tervehdi_monesti("Heidi", 3) #heidi lähettää sen ensimmäiselle funktiolle josta se lähetetään toiselle funkiolle