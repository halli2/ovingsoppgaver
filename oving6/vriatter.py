import kort as k

class Spillere:

    def __init__(self):
        self.spillere = {}

    def nyspiller(self, navn, hand):
        self.spillere[str(navn)] = hand



    def __str__(self, spiller=False):
        resultat = ''
        if spiller == False:
            for key in self.spillere:
                resultat += 'Spiller ' + str(key) + ' har kortene:\n'
                for kort in self.spillere[key]:
                    resultat += str(kort) + '\n'
                resultat += '\n'
        else:
            for kort in self.spillere[spiller]:
                resultat += str(kort) + '\n'
        return resultat 




class Vri:

    identitet = 0
    turn = 0
    runde_spiller = ''
    def __init__(self):
        self.spillere = {}
        self.stokk = k.Kortstokk()
        self.stokk.lag_standard_kort()
        self.stokk.stokk()
        self.bunke = k.Kortstokk()
        self.bunke.legg(self.stokk.trekk())
        self.tur = {}
        self.game_over = False

    def legg_til_spillere(self):
        antall = input('Hvor mange spillere: ')
        self.spillere = Spillere()
        for n in range(int(antall)):
            navn = input('Navn: ')
            self.tur[str(Vri.identitet)] = navn
            Vri.identitet += 1
            hand = []
            for i in range(5):
                hand.append(self.stokk.trekk())
            self.spillere.nyspiller(navn, hand)

    # Viser øverste kortet i bunken på 'bordet'
    def overst_bunke(self):
        try:
            return 'Øverst i bunken - ' + str(self.bunke.overste_kort())
        except IndexError:
            return 'Feil, bunken er tom.'

    # Ny runde, setter runde_spiller lik den sin tur det er for å kalle i dict.
    def runde(self):
        Vri.runde_spiller = self.tur[str(Vri.turn)]
        if Vri.turn < (Vri.identitet - 1):
            Vri.turn += 1
        else:
            Vri.turn = 0
        
    # Trekker kort og legger til i listen i dict'n til spilleren.
    def trekk_kort(self):
        if not self.stokk.kortene:
            behold_kort = self.bunke.trekk() # Beholder øverste kortet!
            for x in self.bunke.kortene:
                self.stokk.legg(self.bunke.trekk())                         # SJEKK HVA SOM SKJER HER!! stokk? duplikat kort?
            self.bunke.legg(behold_kort)
        try:
            kort = self.stokk.trekk()
            self.spillere.spillere[Vri.runde_spiller].append(kort)
            print('Trakk kortet %s \n' %kort)
        except IndexError:
            print('Tom for kort.')
        #self.runde()    # Trukket gir ny runde.

    # Viser kortene til den spilleren som har runden nå.
    def kort_pa_hand(self):
        print('Spiller %s har følgende kort på hånd:\n' %Vri.runde_spiller)
        for n in self.spillere.spillere[Vri.runde_spiller]:
            print(n)
        print('\n')

    def atter_kort(self):
        if self.spillere.spillere[Vri.runde_spiller]:
            test = True
            while test:
                kort = input('"vis" for å vise kort på hånd \nLegg et kort til: ')              # Gjør at hvis 8'er blir lagt igjen får legge enda ett kort!
                if kort == 'vis':
                    self.kort_pa_hand()
                    continue
                for n in self.spillere.spillere[Vri.runde_spiller]:
                    if str(n) == kort:
                        self.bunke.legg(n)
                        test = False
        else:
            self.winner()

    # Forteller hvem sin tur det er
    def spiller_tur(self):
        return Vri.runde_spiller

    def winner(self):
        print('Vinneren er! %s' %Vri.runde_spiller)
        self.game_over = True

                



    def legg_kort(self):
        # print('Velg ')
        # for n in self.spillere.spillere[Vri.runde_spiller]:
        #     print(n)
        # print(self.spillere.spillere[Vri.runde_spiller])
        x = True # lager en while løkke i tilfelle skrivefeil eller ulovlig trekk.
        valg = ''
        
        while x == True:
            kort = input('"vis kort" for å vise kort på hånd. \n"bunke" for å vise kort på bunken. \n "trekk" for å trekke kort \n\nVelg kort: \n')
            if kort == 'vis kort':  # Alternativer hvis 'usikker' på hvilket kort han skal ta
                self.kort_pa_hand()
                continue
            elif kort == 'bunke':
                self.overst_bunke()
                continue
            elif kort == 'trekk':
                self.trekk_kort()
                break
            # print(kort + '\n')
            ny_liste_hand = []
            for n in self.spillere.spillere[Vri.runde_spiller]:
                ja = n
                if str(n) == kort:
                    # trekk kortet legg på bunken.
                    x = False
                    overst_i_bunke = self.bunke.overste_kort()
                    if ja.verdi == 8:                         # FÅ TIL AT ÅTTEN BLIR TATT VEKK SÅ DEN IKKE KAN LEGGES 2 GANGER.
                        print("8'er")
                        self.bunke.legg(n)
                        self.atter_kort()
                    elif ja.korttype == overst_i_bunke.korttype:
                        self.bunke.legg(n)
                    elif ja.verdi == overst_i_bunke.verdi:
                        print('Like verdi.')
                        self.bunke.legg(n)
                    else:
                        x = True
                    #print('Øverste kort i bunken er nå: ' + str(self.bunke.overste_kort()))

                elif str(n) != kort:
                    ny_liste_hand.append(n)

            self.spillere.spillere[Vri.runde_spiller] = ny_liste_hand
            test = True
            # Kan ikke legge kortet
            if x == True:
                while test == True:
                    valg = input('Kan ikke legge det kortet, prøv på nytt eller trekk kort: \n For nytt forsøk skriv: 0 \n For å trekke kort skriv: 1 \n')
                    if valg == '0':
                        print('Prøver på nytt.')
                        test = False
                    elif valg == '1':
                        print('Trekker kort.')
                        x = False
                        test = False
                        self.trekk_kort()





if __name__ == "__main__":
    vrimeg = Vri()
    vrimeg.legg_til_spillere()
    vrimeg.runde()
    # vrimeg.kort_pa_hand()
    # vrimeg.legg_kort()
    while vrimeg.game_over == False:
        print('%s sin tur' %vrimeg.spiller_tur())
        print(vrimeg.overst_bunke())
        vrimeg.kort_pa_hand()
        move = input(
            '0: Legg kort \n1: Trekk kort \nAvslutt: for å avslutte spillet.\n'
        )
        if move == '0':
            vrimeg.legg_kort()
        elif move == '1':
            vrimeg.trekk_kort()
        elif move == 'Avslutt':
            break
        else:
            print('Ingen gyldig input, prøver på ny. \n \n')
        vrimeg.runde()