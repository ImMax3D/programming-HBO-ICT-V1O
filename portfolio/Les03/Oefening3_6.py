getallenrij = [2, 4, 6, 8, 10, 7]
zoekgetal = eval(input('geef een getal'))
gevonden = False
for getal in getallenrij:
   if zoekgetal == getal:
       gevonden=True

if gevonden == True:
    print('het zoekgetal '+str(zoekgetal)+' zit in de getallenrij')
else:
    print('het getal '+str(zoekgetal)+' is niet gevonden')
