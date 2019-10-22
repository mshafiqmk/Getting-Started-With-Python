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
    def bark(self) : 
        print('bark')

class Cat(Mammal) : 
    def be_annoying(self):
        print('annoying')

dog1 = Dog()
dog1.bark()

cat1 = Cat()
cat1.walk()