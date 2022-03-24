ABSTRACTION
Clasa abstracta FormaGeometrica
Contine un field PI=3.14
Contine o metoda abstracta aria
Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’

from abc import ABC, abstractmethod

class FormaGeometrica:
    PI = 3.14

    @abstractmethod
    def aria(self):
        raise NotImplementedError

    def descrie(self):
        print(f'Cel mai probabil am colturi')

class Patrat(FormaGeometrica):
    __latura = 0

    # are un costructor
    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura are dimensiunea: {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura):
        print(f'Noua dimesiune a laturii este: {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print(f'Am sters valoarea laturii')
        self.__latura = 0

    def aria(self):
        self.aria = self.__latura * self.__latura
        return self.aria

class Cerc(FormaGeometrica):
    __raza = 0

    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza cercului este: {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        print(f'Noua valoarea a razei este: {raza}')
        self.__raza = raza

    @raza.deleter
    def raza(self):
        print(f'Am sters valoarea razei')
        self.__raza = 0

    def aria(self):
        aria_cercului = self.PI * self.__raza * self.__raza
        return aria_cercului.__round__(2)

    def descrie(self):
        print(f'Eu nu am colturi')

patrat1 = Patrat(10)
patrat1.descrie()
print(patrat1.aria())
patrat1.latura
patrat1.latura = 15
del patrat1.latura
patrat1.latura


cerc1 = Cerc(3)
cerc1.descrie()
print(cerc1.aria())
cerc1.raza
cerc1.raza = 9
print(cerc1.aria())
del cerc1.raza
cerc1.raza
print(cerc1.aria())









