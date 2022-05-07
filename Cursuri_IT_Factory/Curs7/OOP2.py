'''
Abstraction from Google
Abstraction is used to hide the internal functionality of the function from the users.
The users only interact with the basic implementation of the function, but inner working is hidden.
User is familiar with that "what function does" but they don't know "how it does."
VS
An Abstract class can contain the both method normal and abstract method.
Abstract methods have no budy, they have just the name and

An Interface contains only abstract methods
'''

from abc import ABC, abstractmethod # avem nevoie de importul acesta pentru abstractizare in python

class Car(ABC): #abstract class contains abstract methods

    @abstractmethod # am folosit un decorator ca sa evidentiem mai bine faptul ca metoda este abstracta
    def accelerate(self): #abstract method = metode fara corp (logica interna)
        pass
        # raise NotImplementedError

    @classmethod
    def stop(self): #poate sa contina si metode normale (care au logica interna)
        print("STOP!")



class Ferrari(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 5 seconds")
    def stop(self): # poly
        print("I'm a F, I can't stop")


class Lastun(Car):
    def accelerate(self):
        print("I'm accelerating from 0 to 100 in 15 seconds")


f = Ferrari()
f.accelerate()
f.stop()

l = Lastun()
l.accelerate()
l.stop()


# Interface - toate metodele sunt abstracte (An interface is a completely "abstract class")
# Obliga clasele mostenitoare sa implementeze functiile, e ca o reteta pentru subclase

class Animal(ABC):

    @abstractmethod
    def sound(self):
        raise NotImplementedError

    @abstractmethod
    def sleep(self):
        raise NotImplementedError

# a class implements an interface

class Dog(Animal):
    def sound(self):
        print('Ham Ham!')

    def describe(self):
        print('I have an owner')

    def sleep(self):
        print('ZZZZZZZ')


class Cat(Animal):
    def sound(self):
        print('Miau Miau!')

    def sleep(self):
        print('prrrrr')

    def describe(self):
        print('I own a human')

azorel = Dog()
tom = Cat()
azorel.sleep()
azorel.sound()
azorel.describe()

tom.sleep()
tom.sound()
tom.describe()

#________________________________________

# encapsulation = cand ascundem atributele si folosim getter si setter sa ajungem la ele
# si metodele pot fi private, nu doar atributele
# ele se ascund daca punem __ inainte
import random


class Car:
    __color = 'gray'

    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare
        self.__color = culoarea_dorita

    def delete_color(self):
        self.__color = None

    def __hidden(self):
        pass


volvo = Car()
print(volvo.get_color()) # getter
volvo.set_color('red') # setter
print(volvo.get_color()) # getter
volvo.delete_color() # deleter
print(volvo.get_color()) # getter



class CarPy:

    def __init__(self, color):
        self.__color = color

    @property
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        if color == 'black':
            self.__color = 'gray'
        else:
            self.__color = color
        print(f'Setter: Noua culoare este {color}')


    @color.deleter
    def color(self):
        print(f'Deleter: Am sters culoarea')
        self.__color = None


car2 = CarPy('gray')
car2.color = 'red' # set color
car2.color # get color
del car2.color # del color
car2.color # get color
print('--------------------------------')
car3 = CarPy('white')
print(car3.color) # get color
car3.color = 'black'
print(car3.color)
del car3.color
print(car3.color)

#________________________________________________

#inheritance = cand o clasa copil mosteneste o clasa parinte si are acces la toate atributele si metodele ei

class Chef: # clasa parinte
    cutite = 1
    def make_salad(self):
        print("salad")
    def make_fries(self):
        print("fries")

class Chef2: # clasa parinte
    short = 2

#clasa copil care mosteneste clasa Chef (se trece intre paranteze numele clasei parinte)
class JapaneseChef(Chef):
    def make_sushi(self):
        print("sushi")

class ItalianChef(Chef, Chef2):
    tava = 1
    def make_pizza(self):
        print("pizza")

newbe = Chef() # pot exista obiecte si de tipul clasei parinte
newbe.make_fries()
print("-------------------------------")
nakamoto = JapaneseChef() # initializam un obiect de tip JapaneseChef
nakamoto.make_sushi()
nakamoto.make_salad()
nakamoto.make_fries()

print("-------------------------------")

mario = ItalianChef()
mario.make_pizza()

#------------------------------------------------

#polymorphism - cand exista 2 metode cu acelasi nume dar python stie sa o foloseasca pe cea corecta


# ex de built in polymorphic function
print(len("abc"))
print(len([1, 2, 3, 4]))


# user polymorphic function
def add(x, y, z=0):
    return x + y + z

print(add(2, 3))
print(add(2, 3, 4))


# Polymorphism with class methods
class Romania():
    def language(self):
        print("Romanian")

class USA():
    def language(self):
        print("English")

obj_ro = Romania()
obj_usa = USA()
for country in (obj_ro, obj_usa):
    country.language()

# Polymorphism with Inheritance
class Bird:
    def describe(self):
        print("I'm a bird")

    def fly(self):
        print("Flu Flu! I'm flying")


class Parrot(Bird):
    def talk(self):
        print("I also can talk")


class Penguin(Bird):
    def fly(self): # polymorphism - 2 functii cu acelasi nume - se foloseste cea adecvata - cea din clasa copil
        print("I actually can't fly. But that's ok, I'm dressed stylish.")


random_bird = Bird()
random_bird.describe()
random_bird.fly()
print('------------------------')

polly = Parrot()
polly.describe()
polly.talk()
polly.fly()
print('------------------------')

pingu = Penguin()
pingu.describe()
pingu.fly()

#------------------------------------------------------------------

# exceptie = o eroare in Python, ceva ce nu poate sa faca codul si opreste executia
# se trateaza prin try except

# try: #in try punem codul despre care presupunem ca ar putea genera o execptie
#     number = 0
#     number2 = 10/number
# except Exception as e: #in except tratam orice exceptie (salvam mesajul ei in variabila e)
#     print(f'Error: {e}')
#
# print('ajung aici')

# try: # in try punem codul 'periculos'
#     lista = [1, 2, 3]
#     lista[6]
# except IndexError as e: #tratam IndexError exception
#     print(e)
#
# print('am ajuns aici') # fiindca am prins exceptia, codul merge mai departe

# fortezi o exceptie
raise IndexError('Limita elevilor din clasa este 30')