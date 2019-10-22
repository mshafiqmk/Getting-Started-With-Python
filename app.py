class Person : 
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'Hi , I am {self.name} ... ')


shafiq = Person('Shafiq')
shafiq.talk()

adnan = Person('Adnan')
adnan.talk()