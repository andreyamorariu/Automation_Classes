#a. Usor (recomandat)
#1. Revizualizeaza intalnirea 2 si ia notite in caz ca ti-a scapat ceva
#2. Vizualizeaza video despre Operatori si Flow Control din 'Primii pasi in Programare'
#(Daca nu ai facut-o deja)
#3. Vizualizeaza video 3 despre Structuri de date din 'Primii pasi in Programare'
#Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
#si sigur ti se vor intipari in minte mai bine.
#https://www.itfactory.ro/8174437-intro-in-programare/

#b. Usor spre Mediu (obligatoriu)
#Pentru toate exercitiile se va folosi notiunea de if in rezolvare.
#Indirect veti exersa si operatorii in cadrul conditiilor ramurilor din if
#X poate fi initializat direct in cod sau citit de la tastatura, dupa preferinte.
#X este un int

#1.
#Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else
#Un if else evalueaza daca o propozitie/expresie este True sau False.
#2.
#Verifica si afiseaza daca x este numar natural sau nu

#x = int(input('x= '))
#if x >= 0:
#    print('x este numar natural')
#else:
#    print('x nu este un numar natural')

#3.
#Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru

#if x < 0:
#    print('x este numar negativ')
#elif x > 0:
#    print('x este numar pozitiv')
#else:
#    print('x este numar neutru')

#4.
#Verifica si afiseaza daca x este intre -2 si 13

#if x >= -2 and x <= 13:
#    print('x este intre -2 si 13',x)
#else:
#    print('x nu este intre -2 si 13')

#5.
#Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5

#x = int(input('un numar: '))
#y = int(input('un numar: '))
#if x - y < 5:
#    print('diferenta este mai mica decat 5')

#6.
#Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)

#x = int(input('un numar: '))
#if not (x >= 5 and x <= 27):
#    print('x nu este intre 5 si 27')

#7.
#x si y (int)
#Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare

#x = int(input('un numar: '))
#y = int(input('un numar: '))
#if x == y:
#    print('x si y sunt numere egale')
#elif x > y:
#    print('x este mai mare decat y')
#else:
#    print('x este mai mic decat y')

#8.
#X, y, z - laturile unui triunghi
#Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.

#x = int(input('un numar: '))
#y = int(input('un numar: '))
#z = int(input('un numar: '))
#if (x == y and x != z) or (x == z and x != y) or (y == z and y != x):
#    print('triunghiul este isoscel')
#elif x == y and x == z and y == z:
#    print('triunghiul este echilateral')
#else:
#    print('triunghiul este oarecare')

#9.
#Citeste o litera de la tastatura
#Verifica si afiseaza daca este vocala sau nu

#a = input('o litera: ')
#if a == 'a' or a == 'A' or a == 'e' or a == 'E' or a == 'i' or a == 'I' or a == 'o' or a == 'O' or a == 'u' or a == 'U':
#    print('a este o vocala')
#else:
#    print('a este o consoana')

#10.
#Transforma si printeaza notele din sistem romanesc in sistem american dupa cum urmeaza
#Peste 9 => A
#Peste 8 => B
#Peste 7 => C
#Peste 6 => D
#Peste 4 => E
#4 sau sub => F

#nota = int(input('Alege o nota: '))
#if nota >= 9 and  nota <= 10:
#    nota_usa = 'A'
#    print(f'ai luat nota: {nota_usa}')
#elif nota >= 8 and nota <9:
#    nota_usa = 'B'
#    print(f'ai luat nota: {nota_usa}')
#elif nota >= 7 and nota < 8:
#    nota_usa = 'C'
#    print(f'ai luat nota: {nota_usa}')
#elif nota == 6 and nota < 7:
#    nota_usa = 'D'
#    print(f'ai luat nota: {nota_usa}')
#elif nota >= 4 and nota < 6:
#    nota_usa = 'E'
#    print(f'ai luat nota: {nota_usa}')
#elif nota <= 4 and nota >=1:
#    nota_usa = 'F'
#    print(f'ai luat nota: {nota_usa}')

#c. Optionale (may need google)

#11.
#Verifica daca x are minim 4 cifre
#(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

#x = int(input('un numar: ')
#if x / 1000 > 1 :
#    print('numarul are minim 4 cifre')
#else:
#    print('numarul nu are 4 cifre')

#12.
#Verifica daca x are exact 6 cifre

#x = int(input('un numar: '))
#if x / 100000 > 1 and x / 100000 < 10:
#    print('x are exact 6 cifre')
#else:
#    print('x nu are exact 6 cifre')

#13.
#Verifica daca x este numar par sau impar

#x = int(input('un numar: '))
#if x % 2 == 0:
#    print('x este numar par')
#else:
#    print('x este numar impar')

#14.
#x, y, z (int)
#Afiseaza care este cel mai mare dintre ele?

#x = int(input('un numar'))
#y = int(input('un numar'))
#z = int(input('un numar'))
#if x > y and x > z:
#    print('x este cel mai mare numar')
#elif y > x and y > z:
#    print('y este cel mai mare numar')
#elif z > y and z > x:
#    print('z este ce mai mare numar')
#else:
#    print('x,y,z sunt egale')

#15.
#X, y, z - reprezinta unghiurile unui triunghi
#Verifica si afiseaza daca triunghiul este valid sau nu

#print('Introduceti numerele x,y,z')
#x = int(input('x: '))
#y = int(input('y: '))
#z = int(input('z: '))
#if x + y + z == 180 and x > 0 and y > 0 and z > 0:
#    print('Triunghiul este valabil')
#else:
#    print('Triunghiul nu este valabil')



