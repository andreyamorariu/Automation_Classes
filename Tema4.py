#1.
#Avand lista
#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

#Folositi un for ca sa iterati prin toata lista si sa afisati
#‘Masina mea preferata este x’

#x = 'Volvo'
#for i in range(len(masini)):
#    print(masini[i])
#else:
#    print(f'Masina mea preferata este {x}')

#Faceti acelasi lucru cu un for each

#for masina in masini:
#    print(masina)
#else:
#    print(f'Masina mea preferata este {x}')

#Faceti acelasi lucru cu un while

#i = 0
#while i < len(masini):
#    print(masini[i])
#    i = i + 1
#else:
#    print(f'Masina mea preferata este {x}')

#2.
#Aceeasi lista
#Folositi un for else
#In for
#   Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
#In else
#   Printati lista

#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#for masina in range(1,len(masini)-1):
#    print(masini[masina].upper())
#else:
#    print(masini)

#3.
#Aceeasi lista,
#Vine un cumparator care doreste sa cumpere un Mercedes
#Iterati prin ea prin modalitatea aleasa de voi
#Daca masina e mercedes
#   Printam ‘am gasit masina dorita de dvs’
#   Iesim din ciclu folosind un cuvant cheie care face acest lucru
#Altfel
#   Printam Am gasit masina X. Mai cautam

#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#for masina in masini:
#    if masina == 'Mercedes':
#        print('Am gasit masina dorita de dvs.')
#        break
#    else:
#        print(f'Am gasit masina {masina}. Mai cautam.')

#4.
#Aceasi lista
#Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun
#Iterati prin lista
#Daca masina e Trabant sau Lastun
#   Folositi un cuvant cheie care sa dea skip la ce urmeaza
#(nu trebuie else)
#Printati S-ar putea sa va placa masina x

#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#for masina in masini:
#    if masina == 'Trabant' or masina == 'Lastun':
#        continue
#    print('S-ar putea sa va placa masina', masina)

#5.
#Modernizati parcul de masini
#Creati o lista goala, masini_vechi
#Iterati prin masini
#Cand gasiti Lastun sau Trabant:
#Salvati aceste masini in masini_vechi
#Suprascrieti-le cu ‘Tesla’
#Printati Modele vechi: x
#Modele noi: x

#masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#masini_vechi = []
#for masina in masini:
#    if masina == 'Lastun' or masina == 'Trabant':
#        masini_vechi.append(masina)
#print(masini_vechi)

#masini_vechi = ['Lastun', 'Trabant']
#for i in range (len(masini_vechi)):
#    masini_vechi[i] = 'Tesla'
#print(masini_vechi)

#6.
#Avand dict
#pret_masini = {
#    'Dacia': 6800,
#    'Lastun': 500,
#    'Opel': 1100,
#    'Audi': 19000,
#    'BMW': 23000
#}
#Vine un client cu un buget de 15000 euro
#Prezentati doar masinile care se incadreaza in acest buget
#Iterati prin dict.items() si accesati masina si pretul
#Printati Pentru un buget de sub 15000 euro puteti alege masina x

#buget = 15000
#for masina,pret in pret_masini.items():
#    if pret <= buget:
#        print(f'Pentru un buget de sub 15000 euro puteti alege masina {masina} la pretul {pret}')

#7.
#Avand lista
#numere = numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#Iterati prin ea
#Afisati de cate ori apare 3
#(nu aveti voie sa folositi count)

#x = 0
#for i in numere:
#    if i == 3:
#        x = x + 1
#print(f'Cifra 3 apare de {x} ori')

#8.
#Aceeasi lista
#Iterati prin ea
#Calculati si afisati suma numerelor
#(nu aveti voie sa folositi sum)

#numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#suma = 0
#for i in numere:
#    suma = suma + i
#print('Suma numerelor este', suma)

#9.
#Aceeasi lista
#Iterati prin ea
#Afisati cel mai mare numar
#(nu aveti voie sa folositi max)

#numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#numar_mare = numere[0]
#for i in numere:
#    if i > numar_mare:
#        numar_mare = i
#print('Cel mai mare numar este',numar_mare)

#10.
#Aceeasi lista
#Iterati prin ea
#Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
#Ex: daca e 3, sa devina -3
#Afisati noua lista

#numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
#for i in range(len(numere)):
#    if numere[i] > 0:
#        numere[i] = numere[i] * -1
#print('Noua lista este', numere)

#c. Optionale (may need google)

#11.
#alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#numere_pare = []
#numere_impare = []
#numere_pozitive = []
#numere_negative = []
#Iterati prin lista alte_numere
#Populati corect celelalte liste
#Afisati cele 4 liste la final

#for i in range(len(alte_numere)):
#    if alte_numere[i] % 2 == 0:
#        numere_pare.append(alte_numere[i])
#    else:
#        numere_impare.append(alte_numere[i])
#print('Numerele pare sunt', numere_pare)
#print('Numerele impare sunt', numere_impare)

#for i in range(len(alte_numere)):
#    if alte_numere[i] > 0:
#        numere_pozitive.append(alte_numere[i])
#    else:
#        numere_negative.append(alte_numere[i])
#print('Numerele pozitive sunt', numere_pozitive)
#print('Numerele negative sunt', numere_negative)

#12.
#Aceeasi lista
#Ordonati crescator lista fara sa folositi sort
#Va puteti inspira vizual de aici
#https://www.youtube.com/watch?v=lyZQPjUT5B4

#alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
#for i in range(len(alte_numere)):
#    for j in range(len(alte_numere)-1) :
#        if alte_numere[j] > alte_numere[j+1] :
#            alte_numere[j], alte_numere[j+1] = alte_numere[j+1], alte_numere[j]
#print('Lista ordonata este', alte_numere)

#13.
#Alegeti un numar de la tastatura
#Ex:7
#Scrieti un program care sa genereze in consola urmatoarea piramida
#1
#22
#333
#4444
#55555
#666666
#7777777

#Ex:3
#1
#22
#333

#nr = 6
#for i in range(nr):
#    for j in range(i):
#        print(i, end=' ')
#    print('')

#14.
#tastatura_telefon = [
#  [1, 2, 3],
#  [4, 5, 6],
#  [7, 8, 9],
#  [0]
#]
#Iterati prin lista 2d
#Printati ‘Cifra curenta este x’
#(hint: nested for - adica for in for)

#for i in range(len(tastatura_telefon)):
#    for j in range(len(tastatura_telefon[i])):
#        print(f'Cifra curenta este {tastatura_telefon[i][j]}')



