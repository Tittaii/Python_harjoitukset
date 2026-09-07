#tehtävä 5 keskiaikaiset mittayksiköt

luoti = float(input("anna luoti: "))

naula = float(input("anna naula: "))

tulo1 = luoti * 32

print ("yksi naula on", tulo1)

leiviskä = float(input("anna leiviskä: "))

tulo2 = tulo1 * 20

print ( "yksi leiviskä on", tulo2)

tulo3 = (luoti*13.5)+(tulo1*9)+(tulo2*3)

print ("massa on grammoina", tulo3)

kilot = int (tulo3//1000)

grammat = tulo3 % 1000

print (f"massa nykymittojen mukaan:{kilot:.0f} kilogrammaa ja {grammat:.2f} grammaa.")
