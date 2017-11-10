breuk=3/8
print('{:8.3f}'.format(breuk))

karakter='a'
asc=ord('a')
print(asc)
print('de ascii waarde is {:x}'.format(asc))

string=input('gib string:')
for letter in string:
    asc=ord(letter)
    print('{},{},{:x},{:b}'.format(letter,asc,asc,asc))