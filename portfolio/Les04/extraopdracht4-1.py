temperatuur=eval(input('Hoeveel graden is het: '))
def geefmelding(temperatuur):
    if temperatuur<=0:
        print('Het vriest vandaag')
    elif 0<=temperatuur<15:
        print('Het is koud vandaag')
    else:
        print('Het is lekker weer')
geefmelding(temperatuur)