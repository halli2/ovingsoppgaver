
# Konstruktør for klassen spørsmål.
class Sporsmaal:
    identitet = 1

    def __init__(self, spors, svar_alternativ, svar_korrekt=0):
        self._spors = spors
        self._svar_alternativ = svar_alternativ
        self._svar_korrekt = svar_korrekt
        self.identitet = Sporsmaal.identitet
        Sporsmaal.identitet += 1

    @property
    def spors(self):
        return self._spors
    
    @property
    def svar_alternativ(self):
        return self._svar_alternativ

    @property
    def svar_korrekt(self):
        return self._svar_korrekt
    
    # Metode som sjekker om svar er riktig
    def riktig(self, tall):
        if tall in self.svar_korrekt:
            return True
        else:
            return False

    # __str__ metode som gir ut spørsmålet, m/svaralternativer på respektiv index
    def __str__(self):
        ut = "ID: %s \n Spørsmål: \n" %self.identitet + self.spors
        for indx, svar_alt in enumerate(self.svar_alternativ):
            ut += "\n %s: %s" %(indx, svar_alt)
        return ut

def liste_med_sporsmaal():
    a = Sporsmaal(
        'Hvilken løkkestruktur bruker man for å kjøre en blokk et opgitt antall ganger?', 
        ['For', 'While', 'If', 'Try'], 0
        )
    b = Sporsmaal(
        'Hvilken logisk operator gir bare sann hvis begge argumentene er sanne?',
        ['Or', 'Not', 'and', 'xor'], 2
    )
    c = Sporsmaal('Hvilket år er det?', ['2010', '2012', '2018', '2020'], 3)
    d = Sporsmaal('Har Norge regnskog?', ['Nei', 'JA'], 1)
    e = Sporsmaal('A, B, C, ?', ['F', 'G', 'D', 'D'], [2, 3])
    x = [a, b, c, d, e]
    return x



if __name__ == "__main__":
    riktig = 0
    antall = 0
    test = liste_med_sporsmaal()
    for number in range(len(test)):
        print(test[number])
        antall += 1
        svar = int(input('Velg riktig svaralternativ: '))
        if test[number].riktig(svar):
            print('Korrekt!\n')
            riktig += 1
        else:
            print('Feil Svar!\n')
    print('Ut av %s spørsmål har du fått %s riktige!' %(antall, riktig))


# Frivillig: Lag en funksjon som leser inn en serie med spørsmål fra fil og lager ei liste med
# «Sporsmaal» objekter fra fila. Kjøre spillet basert på fila i stedet for på funksjonen fra
# oppgave e). Denne oppgaven krever at du finner et fornuftig format på denne fila og lager ei
# fil som den kal nese inn.
