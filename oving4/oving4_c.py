import os

# Funksjon som lager en mengde ut av en tekstfil.
def mengdetekst(tekstfil):
    mengde = set()
    with open(tekstfil, "r", encoding="UTF-8") as ov3:
        for linje in ov3:
            word = linje.strip('.:;,-_()')
            word = word.split()
            for i in range(0, len(word)):    # Gjør ordene til lowercase og stripper de for div chars for å ikke få duplikater
                word[i] = word[i].lower()
                word[i] = word[i].strip(',.:;()')
            for i in word:
                mengde.add(i)
        return mengde

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    oving3 = dir_path + '\oving3.txt'
    oving4 = dir_path + '\oving4.txt'

    # Kaller funksjonen på begge filene
    mengde1 = mengdetekst(oving3)
    mengde2 = mengdetekst(oving4)

    # Finner snittet og ser hvilket ord som er i begge mengdene.
    duplikat_ord = mengde1.intersection(mengde2)
    print(duplikat_ord)