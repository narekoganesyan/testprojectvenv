# Инкапсуляция
class Cat:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

cat = Cat('whiski')
print(cat.get_name())


# Наследование
class Animal:
    def speak(self):
        print('Animal speak')

class Dog(Animal):
    def speak(self):
        print('Dog speak')

dog = Dog()
dog.speak()


# Полиморфизм
class Bird:
    def sound(self):
        print("Bird sings")

class Crow(Bird):
    def sound(self):
        print("Crow caws")

def make_sound(bird: Bird):
    bird.sound()

bird = Bird()
crow = Crow()

make_sound(bird)  # Bird sings
make_sound(crow)  # Crow caws
