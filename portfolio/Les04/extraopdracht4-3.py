def eindbedrag(x,y):
    eindbedrag=x*((y/100)+1)
    return eindbedrag

bedrag=eval(input('Geef een bedrag: '))
rente=eval(input('Geef een rentepercentage: '))
print(eindbedrag(bedrag,rente))