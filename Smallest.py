smalest_so_far = None
print('Before' , smalest_so_far)
for value in [9, 41, 12, 3, 74, 15]:
    if smalest_so_far is None :
        smalest_so_far = value
    elif value < smalest_so_far:
        smalest_so_far = value
    print(smalest_so_far, value)
print('Smallest is ', smalest_so_far)
    


    while True:
    if num == "done":
        break
    if smallest is None:
        smallest = num
    elif smallest > num:
        smallest = num