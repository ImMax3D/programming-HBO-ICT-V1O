tabel=[[4,7,2,5],[5,1,9,2],[8,3,6,6]]
for rij in range(3):
    for kolom in range(4):
        print(tabel[rij][kolom],end=' ')
    print()
print(len(tabel))
print(len(tabel[0]))
aantalrijen = len(tabel)
aantalkolommen = len(tabel[0])
for rij in range(aantalrijen):
    for kolom in range(aantalkolommen):
        print(tabel[rij][kolom], end = ' ')
    print()
