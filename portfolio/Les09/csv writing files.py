import csv

with open('gamers.csv', 'w',newline='') as myCSVFile:
    writer=csv.writer(myCSVFile,delimiter=';')

    while True:
        name=input('wat is je naam? ')
        if name=='einde':
            break
        voorletter=input('voorletter')
        if voorletter=='einde':
            break
        geboortedatum=input('wat is je geboortedatum? ')
        if geboortedatum=='einde':
            break
        email=input('wat is je emailadres? ')
        if email=='einde':
            break

        writer.writerow((name,voorletter,geboortedatum,email))