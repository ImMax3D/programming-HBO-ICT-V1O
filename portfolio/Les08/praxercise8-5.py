import random

somworp=random.randrange(2,13)
print(somworp)
aantalworpen=0
succes=0
while succes<100:
    if random.randrange(2,13)==somworp:
        succes+=1
    aantalworpen+=1
print(aantalworpen)
