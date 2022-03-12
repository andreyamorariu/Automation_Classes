#a. Usor (recomandat)
#1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
#2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
#(Daca nu ai facut-o deja)
#3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
#Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
#si sigur ti se vor intipari in minte mai bine.
#https://www.itfactory.ro/8174437-intro-in-programare/

#Pentru toate exercitiile
#Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
#Daca functia are return, printati raspunsul

#b. Dificultate: usor spre mediu

#1. Functie care sa calculeze si sa returneze suma a 2 numere

#def add_numere(a,b):
#    sum = a + b
#    return sum

#numar1=20
#numar2=50
#print(add_numere(20, 50)')

#2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

#numere = int(input("Alege un numar: "))
#def numar_par(numere):
#    if numere % 2 == 0:
#        return True
#    else:
#        return False

#print(numar_par(2))

#3. Functie care returneaza numarul total de caractere din numele tau complet.
#(nume, prenume, nume_mijlociu)

#def total_caractere(nume, prenume, nume_mijlociu):
#    return len(nume) + len(prenume) + len(nume_mijlociu)

#print(total_caractere('Morariu', 'Andreea', 'Maria'))

#4. Functie care returneaza aria dreptunghiului

#def aria_dreptunghiului(L, l):
#    return L * l

#L = float(input('Introduceti lungimea dreptunghiului: '))
#l = float(input('Introduceti latimea dreptumghiului: '))

#print("Aria dreptunghiului este:",aria_dreptunghiului(L, l))

#5. Functie care returneaza aria cercului

#PI = 3.14
#def aria_cercului(r):
#    aria_cercului = r * r * PI
#    return aria_cercului

#print ("Aria cercului este", aria_cercului(6))

#6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

#def caracter(my_string):
#    x = input('Alegeti un caracter: ')
#    if x in my_string:
#        return True
#    else:
#        return False

#print(caracter('abc'))

#7. Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case exte y

#def char_counter(my_string):
#    counter_lower = 0
#    counter_upper = 0
#    for i in range(len(my_string)):
#        if (my_string[i] >= 'a' and my_string[i] <= 'z'):
#            counter_lower += 1
#        elif (my_string[i] >= 'A' and my_string[i] <= 'Z'):
#            counter_upper += 1
#    print('Lower case letter', counter_lower)
#    print('Upper case letter', counter_upper)
#print(char_counter('Andreea-Maria'))

#8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

#lista1 = [1,-2, 3,-4, 5,-6, 7, -8]
#def numere_pozitive(lista1):
#    lista2 = []
#    for numar in lista1:
#        if numar > 0:
#            lista2.append(numar)
#    print('Lista cu numere pozitive este: ', lista2)
#print(numere_pozitive(lista1))

#9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.

#def doua_numere(x, y):
#    if x > y:
#        print(f'Numarul {x} este mai mare decat {y}')
#    elif y > x:
#        print(f'Numarul {y} este mai mare decat {x}')
#    else:
#        print('Numerele sunt egale')
#doua_numere(1, 4)

#10. Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False

#set_numere = {1, 2, 3 ,4 ,5 ,6, 7, 8}
#def functie_numare(nr1,numere):
#    if nr1 in numere:
#        print('Nu am adaugat numarul in set. Acesta exista deja')
#        return False
#    else:
#        numere.add(nr1)
#        print('Am adaugat numarul nou in set.')
#        return True

#functie_numare(9, set_numere)
#print(set_numere)


#c. Optionale (may need google)

#11. Functie care primeste o luna din an si returneaza cate zile are acea luna

#calendar = {
#     'January' : 31,
#     'February' : 28,
#     'March' : 31,
#     'April' : 30,
#     'May' : 31,
#     'June' : 30,
#     'July' : 31,
#     'August' : 31,
#     'September' : 30,
#     'October' : 31,
#     'November' : 30,
#     'Dcember' : 31
# }
#def days(month):
#     return calendar.get(month)
#print(days('February'))

#12. Functie calculator care sa returneze 4 valori
#Suma, diferenta, inmultirea, impartirea a 2 numere

#In final vei putea face:
#a, b, c, d = calculator(10, 2)
#print("Suma: ", a)
#print("Diferenta: ", b)
#print("Inmultirea: ", c)
#print("Impartirea: ", d)

#def calculator(nr1, nr2):
#    a = nr1 + nr2
#    b = nr1 - nr2
#    c = nr1 * nr2
#    d = nr1 / nr2
#    return a, b, c, d

#a, b , c, d = calculator(100, 10)
#print(f'Suma : {a}')
#print(f'Diferenta : {b}')
#print(f'Inmultirea : {c}')
#print(f'Impartirea : {d}')

#13. Functie care primeste o lista de cifre (adica doar 0-9)
#Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
#Returneaza un DICT care ne spune de cate ori apare fiecare litera
#=> dict {
#0: 0
#1 :2
#2: 0
#3: 1
#4: 0
#5: 3
#6: 0
#7: 2
#8: 0
#9: 1
#}

#def lista_numere(numere):
#        my_dict= {}
#        for i in range(0, 10):
#            my_dict[i] = numere.count(i)
#            return my_dict
#lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
#print(lista_numere(lista))


#14. Functie care primeste 3 numere
#Returneaza valoarea maxima dintre ele

#def valoarea_maxima(nr1, nr2, nr3):
#    if nr1>nr2 and nr1>nr3:
#        return nr1
#    if nr2>nr1 and nr2>nr3:
#        return nr2
#    if nr3>nr1 and nr3>nr2:
#        return nr3

#numere = valoarea_maxima(123, 45678, 9101112)
#print(f'Valoarea maxima dintre ele este: {numere}')


#15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
#Ex: daca dam nr 3
#Suma va fi 6 (0+1+2+3)

#def suma_nr(nr):
#    sum=0
#    for i in range(0, nr+1):
#        sum += 1
#    return sum
#x = suma_nr(3)
#print(f'Suma tuturor numerelor este : {x}')

#BONUS:

#16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
#‘Numele este de baiat’ sau ‘Numele este de fata’




#17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
#Returnati numerele comune

#Ex:
#list1 = [1, 1, 2, 3]
#list2 = [2, 2, 3, 4]
#Raspuns: {2, 3}

#18. Functie care sa aplice o reducere de pret
#Daca produsul costa 100 lei si aplicam reducere de 10%
#Pretul va fi 90
#Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida

#19. Functie care sa afiseze data si ora curenta

#def data_ora():
#    return datetime.today()

#print(data_ora())

#20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)

