# from file import Klass
from animal import Animal 


# instance / object 
dog = Animal(name='Jezza', age=4)
cat = Animal(name='Zorka', age=7)
bird = Animal(name='Fufu', age=10)
print(dog.speak())
print(cat.speak())
print(bird.speak())

print(cat.intro())