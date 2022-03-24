'''
Ne imaginam o echipa de fotbal pt teren sintetic.
3 Schimbari maxime admise

Declara o Lista cu 5 jucatori
Schimbari_efectuate = va jucati voi cu valori diferite
schimbari_max = 3

Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
Efectuam schimbarea
Stergem jucatorul scos din lista
Adaugam jucatorul intrat
Afisam a intra x, a iesit y, mai aveti z schimbari
Daca jucatorul nu e in teren:
Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
Afisati ‘mai aveti z schimbari’
'''
#SCHIMBARI_MAXIME = 3
#schimbari_efectuate = 2
# calculam si initializam schimbari ramase
#schimbari_ramase = SCHIMBARI_MAXIME - schimbari_efectuate
#echipa = {'j1', 'j2', 'j3', 'j4', 'j5'}
#jucator_in = 'j6'
#jucator_out = 'j1'

# daca jucatorul e in tere SI daca mai am schimbari
#if jucator_out in echipa and schimbari_ramase > 0:
#    if jucator_in in echipa: # eliminam cazul cand jucatorul este deja in teren
#        print('Nu putem face schimbarea deoarece jucatorul introdus este deja in teren')
#    else: # cazul valid, facem tot ce trebuie facut
#        echipa.remove(jucator_out)  # scoatem jucatorul
#        echipa.add(jucator_in)  # adaugam jucatorul nou
#        schimbari_ramase = schimbari_ramase - 1  # contorizam schimbarea
#        print(f'Schimbare efectuata cu succes!')
#        print(f'A intrat {jucator_in}, a iesit {jucator_out}, mai aveti {schimbari_ramase} schimbari')
#else:
#    if schimbari_ramase <= 0:
#        print('Nu mai ai schimbari')
#    else:
#        print(f'Nu se poate efectua schimbarea deoarece jucatorul {jucator_out} nu e in teren')
#print(f'Actuala echipa este {echipa}')

# caz1 jucator adaugat deja in teren => nu se face sch {'j1', 'j5', 'j3', 'j4', 'j2'}
# caz2 jucator scos nu este in teren => nu se face sch {'j1', 'j5', 'j3', 'j4', 'j2'}
# caz3 happy flow, cand putem face sch, jucator in nu e in teren, jucator out e in teren {'j4', 'j6', 'j2', 'j5', 'j3'}
# caz4 nu mai am schimbari => nu mai am schimbari {'j1', 'j5', 'j3', 'j4', 'j2'}

# while /while else
# i = 0
# while i <= 3:
#     print(i)
#     i = i + 1
#     print(i)
# else: #optional, se executa o singura data la final indiferent daca conditia e true sau false
#     print('done')

# debug = depanare, punem pauza in cod ca sa vedem cum arata un anumit prezent

# for / for else
# range
# de unde incepem, daca nu punem default e 0
# pana unde? dar va fi penultima
# pasul, optional
# putem sa parcurgem invers, descrescator
#for i in range(101, 0, -2):
#    print(i)
#else:
#    print(f'la iesire din for i are valoarea {i}')

# crescator
#for i in range(101, 0, -2):
#    print(i)
#else:
#    print(f'la iesire din for i are valoarea {i}')

# hai sa folosim for ca sa parcurgem lista
# facem noi replace, inlocuim alb cu fuxia
#culori = ['albastru', 'alb', 'verde', 'rosu', 'alb', 'galben']
#for i in range(len(culori)):
#    print(f'culoarea mea preferata este {culori[i]}')
    # daca culoarea e alb, vreau sa fac ceva
#    if culori[i] == 'alb':
        # suprasciu culori de i cu noua valoare
#        culori[i] = 'fuxia'

#print(f'Culori actualizate v1 {culori}')

# for each, trecem prin toate elementele
#for culoare in culori: # pentru fiecare culoare din culori
#    if culoare == 'fuxia':
#        index = culori.index('fuxia') # aflam indexul unde este fuxia
#        culori[index] = 'magenta' # suprascriem lista in acel index

#print(f'Culori actualizate v2 {culori}')

# un alt caz in care folosim for each
#note = [3, 5, 8, 10]
#s = 0
# aflu media artimetica a clasei
#for nota in note:
#    s = s + nota
#else:
#    media = s / len(note)

#print(f'media clasei este {media}')

# break - intrerupe iteratia, iese automat din for
#for i in range(100):
#    if i == 7:
#        break # iesim din for
#    print(i)

#print('se continua cu codul din fisier')
# cand se foloseste break?
# cand cautam acul in carul cu fan
# cand cautam o valoare intr-o lista si dupa ce am gasit, am satisfacut cerinta

# continue
# continue da skip la iteratia curenta, trimite codul inapoi la inceput de for/while
#for i in range(0, 20):
#    if i == 7:
#        continue
#    print(f'i este {i}')

# accesam valori cu for each din dict
#note_elevi = {
#    'marius': 10,
#    'ana s': 7,
#    'andy': 5,
#    'ana d': 7
#}
# care sunt elevii care au luat peste 7?
#for elev, nota in note_elevi.items():
#    if nota>7:
#        print(f'{elev} a luat nota {nota}')
# cati elevi au luat 7?
#counter = 0
#for elev, nota in note_elevi.items():
#    if nota == 7:
#        counter+=1
#print(counter)



