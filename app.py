# Inheritance is using for reusing code 
# example where we can use inheritance
# class Dog : 
#     def walk(self):
#         print('walk')

# class Cat :
#     def walk(slef)
#         print('walk')

# solution
# base class 
class Mammal :
    def walk(self) :
        print('walk')

# inherit Dog from Mamal
class Dog(Mammal) :
    pass 

class Cat(Mammal) : 
    pass

dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()