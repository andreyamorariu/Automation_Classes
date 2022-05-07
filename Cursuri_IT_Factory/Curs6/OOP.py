#nerfgun

#model
#gloante
#piedica pusa

#constructor - model

#descrie()
#incarca()
#trage()
#pune_piedica()
#scoate_piedica()

#------------------

#freestyle - sugestie din clasa
#exemplu simplu de concept din viata de zi cu zi
#cateva atribute
#constructor - required fields
#cateva metode

#2 obiecte

#------------------------------------

#clasa Elev
#atribute: nume, prenume, cod matricol, note (tinem aici toate notele de la mate, romana, info)
#constructor: nume, prenume, cod matricol
#metode:
#descrie elev
#adauga nota per materie
#afiseaza note per materie
#afiseaza media per materie
#afiseaza media generala anuala

#---------------

#clasa Caine
#atribute - rasa, nume, culoare, nume_stapan, varsta
#metode:
#descrie() - afisam nume, nume_stapan, rasa si culoarea intr-un mesaj coerent)
#calculator_varsta() - afisam varsta in ani cainesti (x7)
#la_multi_ani() - cainele creste 1 an
#latra() - afisam '{nume}: Ham Ham' (cand apelam latra(), vom afisa random ham, ham ham sau ham ham ham) hint 'ham ' * n

#creati 2 obiecte de tip Caine cu atribute diferite
#apelati descrie pt fiecare
#apelati latra pt fiecare
#afisati varsta in ani cainesti
#trece un an
#afisati varsta iar


#class Car:

    #fields/atribute
#    culoare = None
#    marca = 'Dacie'
#    model = None

    # constructor
#    def __init__(self, model, culoare):
#        self.model = model
#        self.culoare = culoare

    # metode
#    def accelerate(self):
#        print('Vruum!')

#    def paint(self, culoare):
#        self.culoare = culoare


#car1 = Car('Logan', 'alb')
#car2 = Car('Duster', 'orange')
#print(car2.culoare)
#car1.accelerate()
#car2.accelerate()
#car1.paint('rosuuuuu')
#print(car1.culoare)
#print(car2.culoare)

#import random

#class Caine:
    # atribute - rasa, nume, culoare, varsta
    # constructor
#    def __init__(self, rasa, nume, culoare):
#        self.rasa = rasa
#        self.nume = nume
#        self.culoare = culoare
#        self.varsta = 1

    #metode

#    apelati descrie pt fiecare
#    apelati latra pt fiecare
#    afisati varsta in ani cainesti
#    trece un an


#    def ani_cainesti(self):
#        return self.varsta * 7

#    def descrie(self):
#        print(f'nume: {self.nume}')
#        print(f'culoare: {self.culoare}')
#        print(f'ani cainesti: {self.ani_cainesti()}')

#    def la_multi_ani(self):
#        self.varsta += 1

#    def latra(self):
#        n = random.randint(1,3)
#        print(self.nume + ':')
#        print(f'Ham! ' * n)



#grivei = Caine('golden', 'Grivei', 'alb')
#azorel = Caine('doberman', 'Azorel', 'negru')

#grivei.descrie()
#azorel.descrie()
#azorel.la_multi_ani()
#azorel.descrie()
#azorel.nume = 'Zdreanta'
#azorel.descrie()

# ambele variabile din acest moment se vor referi la acelasi caine
#zdreanta = azorel

#zdreanta.la_multi_ani()
#zdreanta.latra()
#zdreanta.latra()
#zdreanta.latra()

#zdreanta.descrie()
#azorel.descrie()


# ambele variabile din acest moment se vor referi la acelasi caine
#zdreanta = azorel

#azorel.nume = 'Lucy'
#zdreanta.nume = 'Piky'

#azorel.descrie()
#zdreanta.descrie()


#-------------------------

#class Nerfgun:
    #atribute/fields
#    model= None
#    nrgloante= 0
#    piedica_pusa=True
#    culoare= None
#    culoriposibile = {'alb', 'negru', 'rosu'}

    #constructor

#    def __init__(self,model,culoare):
#        self.model=model
#        if culoare in self.culoriposibile:
#            self.culoare=culoare
#        else:
#            print(f'La initializarea obiectului {model} culoarea este invalida! ')
    #metode

#    def descrie(self):
#        print(f'modelul este {self.model}')
#        print(f'nr ul de gloante este {self.nrgloante}')
#        print(f'culoarea este {self.culoare}')
#        print(f'piedica pusa este {self.piedica_pusa}')

#    def scoate_piedica(self):
#        self.piedica_pusa=False
#        print('Ai scos piedica cu succes!')

#    def trage(self):
#        if self.nrgloante>0 and self.piedica_pusa ==False:
#            self.nrgloante-=1
#            print('pac pac')
#        else:
#            print('nu poti trage,verifica piedica scoasa si sa mai ai gloante')

#    def incarca(self,nrgloante):
#        if nrgloante>10:
#            self.nrgloante=10
#        elif nrgloante<=0:
#            print('Gloante invalide!')
#        else:
#            self.nrgloante=nrgloante


#    def pune_piedica(self):
#        self.piedica_pusa=True
#        print('Ai pus piedica cu succes!')







#obiecte/initializam obiecte
#nerf1=Nerfgun('glock','alb')
#nerf2=Nerfgun('deagle','roz')
#nerf1.descrie()
#nerf2.descrie()
#nerf2.culoare='verde'
#nerf2.descrie()
#nerf1.scoate_piedica()
#nerf1.trage()
#nerf1.incarca(11)
#nerf1.descrie()
#nerf1.trage()
#nerf1.trage()
#nerf1.descrie()
#nerf1.pune_piedica()
#nerf1.trage()
#nerf1.descrie()
#nerf2.scoate_piedica()
#nerf2.incarca(1)
#nerf2.trage()
#nerf2.trage()
#nerf2.descrie()