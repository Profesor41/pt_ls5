count = 0
sum = 0 
print('Before', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum)
print('Midd sum is = sum/count and it*s  ', sum / count)
