
# Konstruktør for klassen spørsmål.
class Sporsmaal:
    def __init__(self, sporsmaal, svar_alternativ, svar_korrekt=0):
        self.sporsmaal = sporsmaal
        self.svar_alternativ = svar_alternativ
        self.svar_korrekt = svar_korrekt
    
    # Metode som sjekker om svar er riktig
    def riktig(self, tall):
        if tall == self.svar_korrekt:
            return True
        else:
            return False
    
    # __str__ metode som gir ut spørsmålet, m/svaralternativer på respektiv index
    def __str__(self):
        ut = "Spørsmål: \n" + self.sporsmaal
        for indx, svar_alt in enumerate(self.svar_alternativ):
            ut += "\n %s: %s" %(indx, svar_alt)
        return ut


def liste_med_sporsmaal(spors, svaralt, korsvar):
        liste = []
        for n, x in enumerate(spors):
            liste.append(Sporsmaal(x, svaralt[n], korsvar[n]))
        return liste



if __name__ == "__main__":
    riktig = 0
    antall = 0
    spors = ['Hvilken løkkestruktur bruker man for å kjøre en blokk et opgitt antall ganger?',
        'Hvilken logisk operator gir bare sann hvis begge argumentene er sanne?',
        'Hvilket år er det?',
        'Har Norge regnskog?',
        "A, B, C, ?"
    ]
    svaralt = [
        ['For', 'While', 'If', 'Try'],
        ['Or', 'Not', 'and', 'xor'],
        ['2010', '2012', '2018', '2020'],
        ['Nei', 'JA'],
        ['F', 'G', 'D', 'E']
    ]
    riktig_alt = [0, 2, 3, 1, 2]
    test = liste_med_sporsmaal(spors, svaralt, riktig_alt)
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
