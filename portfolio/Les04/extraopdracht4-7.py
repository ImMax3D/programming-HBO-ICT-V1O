def berekensomevengetallen(som1):
    som1=0
    for getal in getallenrij:
        if getal%2==0:
            som1+=getal
    return('De som van de even getallen bedraagt {}'.format(som1))
def berekensomonevengetallen(som1):
    som2=0
    for getal in getallenrij:
        if getal%2!=0:
            som2+=getal
    return('De som van de oneven getallen bedraagt {}'.format(som2))


getallenrij=[23,35,31,26,73,75,84,29,42,46]

print(berekensomevengetallen(getallenrij))

print(berekensomonevengetallen(getallenrij))