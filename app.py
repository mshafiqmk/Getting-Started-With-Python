numbers = [ 3,5,70,2,1,9,10,50,60]
max = numbers[0]
for x in numbers:
    if x > max:
        max = x

print(f'Max Number in the list of {numbers} is {max}')