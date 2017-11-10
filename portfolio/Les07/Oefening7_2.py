week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag', 'do':'donderdag', 'vr': 'vrijdag'}
week['za']='zaterdag'
for afkortingen in week:
    print(afkortingen)
for langeNaam in week.values():
    print(langeNaam)
for beide in week.items():
    print(beide)
for afkorting in week:
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))

print(afkorting)
print(week[afkorting])
