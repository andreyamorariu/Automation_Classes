#'''
# numar natural sau nu
# calculator de impozit in f de cc
# % de benzina ramasa + daca scadem sub 15%, afisam un warning
# nume de baiat sau fata?
# F care sa aplice o reducere de pret. Ex: 100 lei, reducere 10%, return 90
# sa inbunatatim f de add din set
# 2 liste? care sunt elementele lor comune?
# f de replace pe lista
#'''

#def say_hi():
#    print('Hi!')

#say_hi()
#print(say_hi())

# nume este parametru
#def say_hi_user(name, prenume):
#    prenume = prenume.upper()
#    print(f'Hi {name} {prenume}!')

# input 3 numere
# output - ne dorim un set
#def make_set(n1, n2, n3):
#    r = set()
#    r.add(n1)
#    r.add(n2)
#    r.add(n3)
#    return r

#say_hi()
#print(say_hi())

# Andy este argument
#say_hi_user('S', 'Andy')
#say_hi_user('S', 'Ares')

#set1 = make_set(1,2,2)
#set2 = make_set(1,2,3)

#print(set1.intersection(set2))

# cand apelez functia eu deja trebuie sa vizualizez rezultatul
#print(make_set(1,2,3).intersection(make_set(2, 3, 3)))

# f cu return dar fara param
#def pi_value():
#    return 3.14

#x = pi_value() + 4
#print(x)

# cum folosim functii din alte fisiere?
# import doar ce am nevoie
#from folder1.helpers import suma

# import tot din helpers
# from folder1.helpers import *
# print(suma(3,4))
#
# cc = int(input('Alege centimetri cubi  '))
# impozit = None
# def calcul_impozit(cc_input, hibrid_input):
#     if hibrid_input == True:
#         return 10
#     else:
#         if cc_input < 1000:
#             return 70
#         elif cc_input <2000:
#             return 160
#         else:
#             return 900
#
# #apelam functia
# impozit = calcul_impozit(cc, False)
# print(impozit)#cc 49= 70
# impozit= calcul_impozit(2400, False)
# print(impozit)# =900
# impozit = calcul_impozit(2400, True)
# print(impozit)#10

# Room1 - Emi
#def benzina_ramasa(benzina):
#    if benzina<15:
#        return 'warning'
#    else:
#        return benzina

# raspuns=benzina_ramasa(16)
# print(raspuns)
# # Room2 - Denis
# benz = int(input('Benzina ramasa:'))
# benz_ramasa = None
# REZERVOR = 50
# def benzina_ramasa(benzina_input):
#     if benzina_input > REZERVOR:
#         print('Nu poti avea mai multi l decat capacitatea max')
#         return 'N/A'
#     if benzina_input < 0:
#         print('Nu poti avea valori negative')
#         return 'N/A'
#     procentaj_benz = benzina_input/REZERVOR * 100
#     print(procentaj_benz)
#     if procentaj_benz <= 15:
#         print('Warning')
#     return procentaj_benz
#
# benz_ramasa = benzina_ramasa(benz)
# print(f'Mai ai {benz_ramasa}% benzina')

# Room3 - Teodora
# REZERVOR = 50
# cantitate_benzina = float(input('Introdu cantitatea de benzina: '))
# def consum_benzina(cantitate_benzina):
#     if cantitate_benzina == 0:
#         return ('Caut-o sticla')
#     elif cantitate_benzina < 7.5:
#         return ('Atentie, cauta o benzinarie')
#     else:
#         return ('Vrummm, Vruummm')
# print(consum_benzina(cantitate_benzina))

# Room 1 - Isa, Flo, Teo
# nume = input('Introdu nume')
# exceptii_fete = ['Carmen', 'Damaris', 'Beatrice']
# exceptii_baieti = ['Mihnea', 'Mircea', 'Horia', 'Horea']
#
# def gen(nume):
#     if nume[len(nume)-1] != 'a' and
#         print('Este baiat.')


# Room 2 - Denis, Andreea, Miki
# nume = input('Nume: ')
# numele = None
# def gen_nume(nume_input):
#     if nume_input[len(nume_input)-1] == 'a':
#         print('este nume de fata')
#         return 'este nume de fata'
#     else:
#         print('este nume de baiat')
#         return 'este nume de baiat'
#
# numele = gen_nume(nume)
# print(numele)


# Room 3
# nume = input('Introduceti numele:')
#lista_nume_baieti=['Mihnea','Mircea','Luca']
#lista_nume_fete=['']
#def fata_baiat(nume_ales):
#    if nume_ales in lista_nume_baieti:
#        return 'Nume de baiat'
#    elif nume_ales in lista_nume_fete:
#        return 'Nume de fata'
#    elif nume_ales[len(nume_ales)-2:len(nume_ales)-1] == 'a':
#        return 'Nume de fata'
#    else:
#        return 'Nume de baiat'

#print(fata_baiat('Ana'))
#print(fata_baiat('Mihai'))

#cc = int(input('Alege centimetri cubi  '))
#impozit = None
#def calcul_impozit(cc_input, hibrid_input):
#    if hibrid_input == True:
#        return 10
#    else:
#        if cc_input < 1000:
#            return 70
#        elif cc_input <2000:
#            return 160
#        else:
#            return 900



#apelam functia
#impozit = calcul_impozit(cc, False)
#print(impozit)#cc 49= 70
#impozit= calcul_impozit(2400, False)
#print(impozit)# =900
#impozit = calcul_impozit(2400, True)
#print(impozit)#10


