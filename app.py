
try:
    age = int(input('Age : '))
except ValueError as error:
    print(f'invalid value message => {error} ')