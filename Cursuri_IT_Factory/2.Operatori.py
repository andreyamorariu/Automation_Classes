# operatori de atribuire
#x = 3
#x+=7 # la fel ca si x = x + 10
#print(x)

# if
#NOTA_DE_TRECERE_EXAMEN = 4.5 # constanta, semnalam cu litere mari, sa avem grija sa nu se schimbe
#NOTA_DE_TRECERE_PURTARE = 7
#if 7 >= NOTA_DE_TRECERE_EXAMEN and 9 >= NOTA_DE_TRECERE_PURTARE:
#    print('Am trecut')

# if else
#nota_examen = 10
#nota_purate = 10
#if nota_examen >= NOTA_DE_TRECERE_EXAMEN and nota_purate >= NOTA_DE_TRECERE_PURTARE:
#    print('Am trecut clase')
#    if nota_examen == 10 and nota_purate == 10:
#        print('premiul intai')
#else: # nu are conditie, pentru ca e ce a mai ramas
#    print('Nu am trecut clasa')

# if else if ... else
#optiune = int(input('alegeti limba, pt 1 e ro, pt 2 e eng'))
#if optiune == 1:
#    print('ati ales ro')
#    op2 = int(input('pers fiz 1, pers jur 2'))
#    if op2 == 1:
#        print('ati ales fiz')
#    elif op2 == 2:
#        print('ati ales jur')
#    else:
#        print('nu ati ales bine')
#elif optiune == 2:
#    print('ati ales ro')
#elif optiune == 3:
#    print('meniul anterior')
#else:
#    print('nu ati ales corect')

#mama = True
#tata = True
#acord_mama = False
#acord_tata = False
#varsta = 17
#pasaport = True

#if pasaport == False: # nu avem pasaport
#    print('Nu te poti imbarca, indiferent de varsta')
#else: # avem pasaport
#    print('OK, ai pasaport')
#    if varsta >= 18: #major, avem pasaport
#        print('Te poti imbarca')
#    else: # pe aici intru doar daca am pasaport si sunt minor
#        print('sunt minor, am pasaport')
#        if mama == True and tata == True:
#            print('te poti imbarca. si mama si tata')
#        elif mama == True and tata == False and acord_tata == True:
#            print('te poti imbarca, esti cu mama, exista acord tata')
#        elif mama == False and tata == True and acord_mama == True:
#            print('te poti imbarca, esti cu mama, exista acord tata')
#        else:
#            print('nu mai pot, probabil lipsesc ambii parintii, fie lipseste acordul')


#Joc ghicit zarul
# Cauta pe net si vezi cum se genereaza un numar random
# Ne imaginam ca dam cu zarul si salvam acest numar in dice_roll
# import random
# dice_roll = random.randint(1,6)
#
# Luati un nr ghicit de la utilizator
# x = int(input('Alegeti un numar dat cu zarul, de la 1 la 6: '))
#
# Verificati si afisati daca utilizatorul a ghicit
# 3 optiuni
# Ai pierdut. Ai ales un numar mai mic. Ai ales x dar a fost y
# if x < dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mic. Ai ales {x}, dar a fost {dice_roll}.')
#
# Ai pierdut. Ai ales un numar mai mare. Ai ales x dar a fost y
# elif x > dice_roll:
#     print(f'Ai pierdut. Ai ales un numar mai mare. Ai ales {x}, dar a fost {dice_roll}.')
#
# Ai ghicit. Felicitari? Ai ales x si zarul a fost y
# else:
#     print(f'Ai ghicit. Felicitari? Ai ales {x} si zarul a fost {dice_roll}.')