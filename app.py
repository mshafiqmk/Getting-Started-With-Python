secret_number = 9
i = 0
while i<=3:
    number = int(input('Enter Number to guess = '))
    if number == secret_number :
        print('You Win')
        break
    else:
        print('Give anthor try')
        i+=1