#Gib den Preis und das erhaltene Geld ein, ausgegeben wird die Menge an zu gebendem Rückgeld
preis = float(input("Preis: "))
bezahlt = float(input("Bezahlt: "))

rückgeld = bezahlt - preis

if rückgeld >= 0 :
    print ("Rückgeld: " + str(rückgeld))
else :
    print ("ZUUU WEEEENIIIIG!!!!!!!") 