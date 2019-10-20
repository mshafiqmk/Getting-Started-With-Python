is_hot = False

if is_hot:
    print('its hot "day" today')
else: 
    print("Today is normal day")

first = input('Enter your first Name ')
last  = input('Enter your last Name ')

if len(first) <=3 or len(last) <=3:
    print("Name should be greater than three character")
else: 
    print(f"Hello {first} , {last} ")