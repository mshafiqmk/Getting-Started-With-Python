
try:
    age = int(input('Age : '))
    income = 1000
    risk = income / age 
    print(age)
except ValueError as error:
    print(f'invalid value ErrorMessage => {error} ')
except ZeroDivisionError :
    print(f'Age cannot be zero ErrorMessage =>{ZeroDivisionError}')