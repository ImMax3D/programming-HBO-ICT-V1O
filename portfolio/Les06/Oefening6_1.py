gewicht=eval(input('wat is je gewicht: '))
lengte=eval(input('wat is je lengte in meters: '))
bmi=gewicht/(lengte**2)
if bmi<=18.5:
    print('ondergewicht')
elif bmi>18.5 or 25:
    print('normaal')
else:
    print('overgewicht')
print('je bmi is',bmi)
