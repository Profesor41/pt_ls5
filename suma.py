zork = 0
print('Before' , zork)
for thing in [1, 2, 5, 6, 7, 2, 15, 100]:
    zork = thing + zork
    print(thing, zork)
print('Summa is ', zork)