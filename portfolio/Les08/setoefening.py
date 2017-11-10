set1=set()
for i in range(0,1000):
    if i % 3 ==0:
        set1.add(i)
set2=set()
for i in range(0,1000):
    if i % 7==0:
        set2.add(i)

set3=set()
for i in range(0,1000):
    set3.add(i)
print(set3-set1-set2)