#b. Obligatorii (mediu)

#Pentru toate clasele, creati cel putin 2 obiecte cu valori diferite si apelati toate metodele clasei

#1.
#Clasa Cerc

#Atribute: raza, culoare

#Constructor pt ambele atribute

#Metode:
#descrie_cerc() - va PRINTA culoarea si raza
#aria() - va RETURNA aria
#diametru()
#circumferinta()

#class Cerc:
#    raza = None
#    culoare = None

#    def __init__(self, raza, culoare):
#        self.raza = raza
#        self.culoare = culoare

#    def descrie_cerc(self):
#        print(f'raza este: {self.raza}')
#        print(f'culoarea este: {self.culoare}')


#    def aria(self):
#        return self.raza * self.raza * 3.14

#    def diametru(self):
#        return self.raza * 2

#    def circumferinta(self):
#        return self.raza * 2 * 3.14

#cerc1 = Cerc(8, 'roz')
#cer2 = Cerc(12, 'mov')

#cerc1.descrie_cerc()
#cer2.descrie_cerc()
#print(cerc1.aria())
#print(cer2.aria())
#print(cerc1.diametru())
#print(cer2.diametru())
#print(cerc1.circumferinta())
#print(cer2.circumferinta())


#2.
#Clasa Dreptunghi

#Atribute: lungime, latime, culoare

#Constructor pt toate atributele

#Metode:
#descrie()
#aria()
#perimetrul()
#schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

#class Dreptunghi:
#    lungime = None
#    latime = None
#    culoare = None

#    def __init__(self, lungime, latime, culoare):
#        self.lungime = lungime
#        self.latime = latime
#        self.culoare = culoare

#    def descrie(self):
#        print(f'Lungimea este: {self.lungime}')
#        print(f'Latimea este: {self.latime}')
#        print(f'Culoarea este: {self.culoare}')

#    def aria(self):
#        return self.lungime * self.latime

#    def perimetrul(self):
#        return (self.lungime + self.latime) * 2

#    def noua_culoare(self, culoare):
#        self.culoare = culoare
#        print(f'Culoarea este: {self.culoare}')

#drept1 = Dreptunghi(10, 6, 'albastru')
#drept2 = Dreptunghi(22, 14, 'maro')

#drept1.descrie()
#drept2.descrie()
#print(drept1.aria())
#print(drept2.aria())
#print(drept1.perimetrul())
#print(drept2.perimetrul())
#drept1.noua_culoare('turcoaz')
#drept2.noua_culoare('visiniu')

#3.
#Clasa Angajat

#Atribute: nume, prenume, salariu

#Constructor pt toate atributele

#Metode:
#descrie()
#nume_complet()
#salariu_lunar()
#salariu_anual()
#marire_salariu(procent)

#class Angajat:

#    def __init__(self, nume, prenume, salariu):
#        self.nume = nume
#        self.prenume = prenume
#        self.salariu = salariu

#    def descrie(self):
#        print(f'Nume: {self.nume}')
#        print(f'Prenume: {self.prenume}')
#        print(f'Salariu: {self.salariu}')

#    def nume_complet(self):
#        print(f'Numele complet este: {self.nume} {self.prenume}')

#    def salariu_lunar(self):
#        print(f'Salariul lunar este: {self.salariu}')

#    def salariu_anual(self):
#        print(f'Salariul anual este: {self.salariu * 12}')

#    def marire_salariu(self, procent_marire):
#         self.salariu = self.salariu + (self.salariu * procent_marire/100)
#         print(f'Marirea de salariu este {procent_marire}% iar salariul a devenit: {self.salariu}')




#angj1 = Angajat('Avram', 'Ana', 4500)
#angj2 = Angajat('Avram', 'Marius', 4000)

#angj1.descrie()
#angj2.descrie()
#angj1.nume_complet()
#angj2.nume_complet()
#angj1.salariu_lunar()
#angj2.salariu_lunar()
#angj1.salariu_anual()
#angj2.salariu_anual()
#angj1.marire_salariu(10)
#angj2.marire_salariu(10)



#4.
#Clasa Factura

#Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie),
# numar, nume_produs, cantitate, pret_buc

#Constructor: toate atributele, fara serie

#Metode:
#schimba_cantitatea(cantitate)
#schimba_pretul(pret)
#schimba_nume_produs(nume)
#genereaza_factura() - va printa tabelar daca reusiti

#Factura seria x numar y
#Data: generati automat data de azi
#Produs | cantitate | pret bucata | Total
#Telefon |      7       |       700       | 49000

#Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

#class Factura:
#    seria = 100
#    numar = None
#    nume_produs = None
#    cantitate = None
#    pret_buc = None

#    def __init__(self, numar, nume_produs, cantiate, pret_buc):
#        self.numar = numar
#        self.nume_produs = nume_produs
#        self.cantitate = cantiate
#        self.pret_buc = pret_buc

#    def schimba_cantitate(self, cantitate_noua):
#        self.cantitate = cantitate_noua
#        print(f'Noua cantitate este : {self.cantitate}')

#    def schimba_pretul(self, pret_nou):
#        self.pret_buc = pret_nou
#        print(f'Noul pret este : {self.pret_buc}')

#    def schimba_nume_produs(self, nume_nou):
#        self.nume_produs = nume_nou
#        print(f'Noul nume este : {self.nume_produs}')

#    def genereaza_factura(self):
#        print(f'Factura seria {self.seria} numar {self.numar}')
#        from datetime import date
#        today = date.today()
#        print(f'Data este: {today}')
#        total = self.cantitate * self.pret_buc
#        print(f'Produs  | cantitatea| pret bucata| totalul ')
#        print(f'{self.nume_produs} |     {self.cantitate}     |   {self.pret_buc}      | {total}')

#fact1 = Factura(28, 'Gaz', 1, 480)
#fact2 = Factura(18, 'Electricitate', 1, 180)

#fact1.schimba_cantitate(2)
#fact2.schimba_cantitate(4)
#fact1.schimba_pretul(650)
#fact2.schimba_pretul(500)
#fact1.schimba_nume_produs('Eon Gaz')
#fact2.schimba_nume_produs('Electrica Furnizare')
#fact1.genereaza_factura()
#fact2.genereaza_factura()


#5.
#Clasa Cont

#Atribute: iban, titular_cont, sold

#Constructor pentru toate

#Metode:
#afisare_sold() - Titularul x are in contul y suma de n lei
#debitare_cont(suma)
#creditare_cont(suma)

#class Cont:
#    iban = None
#    titular_cont = None
#    sold = 0.00

#    def __init__(self, iban, titular_cont, sold):
#        self.iban = iban
#        self.titular_cont = titular_cont
#        self.sold = sold

#    def afisare_sold(self):
#        print(f'Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei.')

#    def debitare_cont(self, suma_debitata):
#        if self.sold > 0 and self.sold > suma_debitata :
#            self.sold = self.sold - suma_debitata
#            print(f'In cont mai aveti {self.sold} lei.')
#        else:
#            print('Fonduri insuficiente.')

#    def creditare_cont(self, suma_creditata):
#        self.sold = self.sold + suma_creditata
#        print(f'Contul dvs a fost creditat cu suma de {suma_creditata} lei.')

#cont1 = Cont('RZBR20RO1234', 'Rus Ovidiu', 7000 )
#cont2 = Cont('RZBR40RO5678', 'Pop Alex', 10000)

#cont1.afisare_sold()
#cont2.afisare_sold()
#cont1.debitare_cont(500)
#cont2.debitare_cont(900)
#cont1.creditare_cont(300)
#cont2.creditare_cont(150)


#BONUS: (daca aveti timp si doriti sa lucrati suplimentar)

#6.
#Clasa Masina

#Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
#Culoare = gri - toate masinile cand ies din fabrica sunt gri
#Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
#Culori disponibile = alegeti voi 5-7 culori
#Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
#Inmatriculata = False

#Constructor: model, viteza_maxima

#Metode:
#descrie() (se vor printa toate atributele, inafara de culori_disponibile)
#inmatriculare() - va schimba atributul inmatriculata in True
#vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
#accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
#franeaza() - masina se va opri si va avea viteza 0

#class Masina:
#    marca = 'Tesla'
#    model = None
#    viteza_maxima = 0
#    viteza_actuala = 0
#    culoare = 'gri'
#    culori_disponibile = {'alb', 'negru', 'rosu', 'albastru', 'bej'}
#    inmatriculata = False

#    def __init__(self, model, viteza_maxima):
#        self.model = model
#        self.viteza_maxima = viteza_maxima

#    def descrie(self):
#        print(f'Marca masinii este : {self.marca}')
#        print(f'Modelul masinii este : {self.model}')
#        print(f'Viteza maxima a masinii este : {self.viteza_maxima}')
#        print(f'Viteza actuala a masinii este : {self.viteza_actuala}')
#        print(f'Culoarea masinii este : {self.culoare}')
#        print(f'Masina este inmatriculata : {self.inmatriculata}')

#    def inmatriculare(self):
#        self.inmatriculata = True
#        print(f'Masina este acum inmatriculata : {self.inmatriculata}')

#    def vopseste(self, noua_culoare):
#        if noua_culoare in self.culori_disponibile:
#            self.culoare = noua_culoare
#            print(f'Noua culoare a masinii este : {self.culoare}')
#        else:
#            print('Culoarea aleasa nu este disponibila.')

#    def accelereaza(self, viteza):
#        if viteza < self.viteza_actuala:
#            print('Atentie, valoarea este invalida.')
#        elif viteza <= self.viteza_maxima:
#            self.viteza_actuala = viteza
#            print(f'Ati atins viteza de : {self.viteza_actuala} km/h.')
#        else:
#            self.viteza_actuala = self.viteza_maxima
#            print(f'Ati atins viteza maxima de : {self.viteza_actuala} km/h.')

#    def franeaza(self):
#        if self.viteza_actuala == self.accelereaza(90):
#            self.viteza_actuala = 0
#            print('Ati franat, masina s-a oprit.')

#masina1 = Masina('Model 3', 220)
#masina2 = Masina('Model S', 240)

#masina1.descrie()
#masina2.descrie()
#masina1.inmatriculare()
#masina2.inmatriculare()
#masina1.vopseste('bej')
#masina1.vopseste('verde')
#masina2.vopseste('negru')
#masina2.vopseste('maro')
#masina1.accelereaza(60)
#masina2.accelereaza(250)
#masina1.franeaza()
#masina2.franeaza()


#7.
#Clasa TodoList

#Atribute: todo(dict, cheia e numele taskului, valoarea e descrierea)
#La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor

#Metode: adauga_task() - se va adauga in dict
#finalizeaza_task() - se va sterge din dict
#afiseaza_todo_list() - doar cheile
#afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
#daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
#Daca acesta raspunde nu - la revedere
#daca raspunde da - il cerem detalii task si salvam nume + detalii in dict


