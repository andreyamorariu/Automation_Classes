#1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
#o variabila este un container din memorie care stocheaza valori
#2. Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
#string, int, float, bool
#Valorile le alegeti voi dupa preferinte

#tara = 'thailanda'
#nr_persoane = 4
#temperatura = 33.5
#prima_vizita = True

#3. Utilizat functia type pentru a verifica ca ele au tipul de date asteptat

#print(type(tara))
#print(type(nr_persoane))
#print(type(temperatura))
#print(type(prima_vizita))

#4. Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
#Verificati tipul acesteia

#temperatura_rotunjita = round(temperatura)
#temperatura = temperatura_rotunjita
#print(f'temperatura rotunjita este: {temperatura_rotunjita}')


#5. folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
#$(rezolvati nepotrivirile de tip prin ce modalitate doriti)

#print(f'Noi o sa mergem in vacanta in {tara}')
#print(f'In vacanta din {tara} o sa fim {nr_persoane} persoane')
#print(f'In {tara} sunt acum {temperatura} grade')
#print(f'Aceasta este prima noastra vacanta in {tara}. {prima_vizita}')

#6. citeste de la tastatura numele
#citeste de la tastatura prenumele
#afiseaza 'Numele complet are x caractere'

#nume = 'Morariu'
#prenume = 'Andreea'
#nume_prenume = len(nume+prenume)
#print(f'Numele complet are {nume_prenume} caractere')

#7. citeste de la tastatura lungimea
#citeste de la tastatura latimea
#afiseaza 'Aria dreptunghiului este x'

#lungimea = 9
#latimea = 5
#aria = lungimea*latimea
#print(f'Aria dreptunghiului este {aria}')

#8. Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
#cititi de la tastatura un int x
#afiseaza stringul fara ultimele x caractere
#ex: daca ati ales 7 => 'Coral is either the stupidest animal or the smarte'

#string = 'Coral is either the stupidest animal or the smartest rock'
#x = int(input('3: '))
#y = len(string)-x
#print(string[0:y])

#9.acelasi string
#declara un string nou care sa fie format din primele 5 caractere + ultimele 5

#string1 = (string[0:5])
#lungime_string = len(string)
#string2 = (string[-5:])
#string_nou = print(f'{string1} {string2}')

#10.acelasi string
#afisati de cate ori apare cuvantul 'the'

#print (string.count('the'))

#11.acelasi string
#inlocuieste the cu THE peste tot
#printeaza rezultatul

#print(string.replace('the', 'THE'))

#12.acelasi string
#salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
#(hint: este o functie care te ajuta sa faci asta)
#folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
#output: 'Coral is either the stupidest animal or the smartest '

#index_rock = (string.index('rock'))
#print(f'index_rock:{index_rock}')
#print(string[0:index_rock])

#13. citeste de la tastatura un string
#verifica daca primul si ultimul caracter sunt la fel
#se va folosi un assert
#atentie: se doreste ca programul sa fie case insensitive
#'apA' e acceptat

#my_string = str.casefold(input('un cuvant: '))
#size = len(my_string)
#assert my_string [:1] == my_string [size-1:size]


#14. avand stringul '0123456789'
#afisati doar numerele pare
#acum afisati doar numerele impare
#(hint: folositi slicing, controlati din pas)

#string = '0123456789'
#numar_par = string[::2]
#print(numar_par)
#numar_impar = string[1::2]
#print(numar_impar)