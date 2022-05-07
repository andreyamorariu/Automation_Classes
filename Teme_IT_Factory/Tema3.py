#1.
#Declara o lista note_muzicale in care sa pui do re mi etc pana la do
#Afiseaz-o

#note_muzicale = ['do','re','mi','fa','sol','la','si','do']
#print(note_muzicale)

#Inverseaza ordinea folosind slicing si suprascrie aceasta lista
#Printeaza varianta actuala (inversata)

#note_muzicale = ['do','re','mi','fa','sol','la','si','do']
#note_muzicale = note_muzicale[::-1]
#print(note_muzicale)

#Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea. (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
#Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala

#note_muzicale.reverse()
#print('Lista inversata:', note_muzicale)

#Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari. Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.

#2.
#De cate ori apare ‘do’?

#note_muzicale = ['do','re','mi','fa','sol','la','si','do']
#print(f'Do apare de {note_muzicale.count("do")} ori.')

#3.
#Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
#Gasiti 2 variante sa le uniti intr-o singura lista.

#list1 = [3, 1, 0, 2]
#list2 = [6, 5, 4]
#newlist = list1 + list2
#print(newlist)

#newlist = [*list1, *list2]
#print(newlist)

#Afisati lista ordonata astfel [0,1,2,3,4,5,6]

#newlist_ordonata = sorted(newlist)
#print(newlist_ordonata)

#4.
#Sortati si afisati lista generata la ex anterior

#sorted(newlist)
#print(newlist)

#Stergeti numarul 0 folosind o functie
#Afisati iar lista

#newlist.remove(0)
#print(newlist)

#5.
#Folosind un if verificati lista generata la ex3 si afisati
#Lista este goala
#Lista nu este goala

#newlist = [3, 1, 0, 2, 6, 5, 4]
#newlist2 = []
#if len(newlist2):
#    print('Lista nu este goala')
#else:
#    print('Lista este goala')

#6.
#Folositi o functie care sa stearga lista de la ex3

#newlist = [3, 1, 0, 2, 6, 5, 4]
#newlist.clear()
#print(newlist)

#7.
#Copy paste la ex 5. Verificati inca o data.
#Acum ar trebui sa se afiseze ca lista e goala

#newlist = [3, 1, 0, 2, 6, 5, 4]
#newlist2 = []
#if len(newlist2):
#    print('Lista nu este goala')
#else:
#    print('Lista este goala')

#8.
#Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#Folositi o functie ca sa afisati Elevii (cheile)

#dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
#print(dict1.keys())

#9.
#Printati cei 3 elevi si notele lor
#Ex: ‘Ana a luat nota x’
#X il veti lua folosind dictul si cheia

#dict1 = {'Ana' : 8,'Gigel' : 10,'Dorel' : 5}
#print(f'Ana a luat nota {dict1.get("Ana")}.Gigel a luat nota {dict1.get("Gigel")}. Dorel a luat nota {dict1.get("Dorel")}.')

#10.
#Dorel a facut contestatie si a primit 6
#Modificati nota lui Dorel in 6
#Printati nota dupa modificare

#dict1 = {'Ana' : 8,'Gigel' : 10,'Dorel' : 5}
#dict1['Dorel'] = '6'
#print(dict1)

#11.
#Gigel se transfera din clasa
#Cautati o functie care sa il stearga

#dict1 = {'Ana' : 8,'Gigel' : 10,'Dorel' : 5}
#dict1.pop('Gigel')
#print(dict1)

#Vine un coleg nou. Adaugati Ionica, cu nota 9
#Printati noii elevi

#dict1 = {'Ana': 8, 'Dorel': 5}
#dict1['Ionica'] = '9'
#print(dict1)

#12.
#Set
#zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
#weekend = {'sambata', 'duminica'}
#Adaugati in zilele_sapt ‘luni’
#Afisati zile_sapt

#zile_sapt.add('luni')
#print(zile_sapt)

#13.
#Folositi un if si verificati daca
#Weekend este un subset al zilelor din sapt
#Weekend nu este un subset al zilelor din sapt

#if weekend.issubset(zile_sapt):
#    print('Weekend este un subset al zilelor sapt.')
#else:
#    print('Weekend nu este un subset al zilelor din sapt.')

#14.
#Afisati diferentele dintre aceste 2 seturi

#print(zile_sapt.difference(weekend))

#15.
#Afisati intersectia elementelor din aceste 2 seturi

#print(zile_sapt.intersection(weekend))