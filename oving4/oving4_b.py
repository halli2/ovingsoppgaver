import os
# For å slippe å skrive lengre path enn bare i mappen filen kjøres fra.
dir_path = os.path.dirname(os.path.realpath(__file__))

textfil = (input('Skriv inn navn på tekstfil: '))

# dir path er mappen vi er i nå.
textfil = dir_path + textfil
ord_fil = ''
ord_dict = {}

try:
    with open(textfil, "r", encoding="UTF-8") as fil_dict:
        for linje in fil_dict:
            ord_fil += linje
        ord_fil = ord_fil.split()
        for i in range(0, len(ord_fil)):    # Gjør ordene til lowercase og stripper de for div chars for å ikke få duplikater
            ord_fil[i] = ord_fil[i].lower()
            ord_fil[i] = ord_fil[i].strip(',.:;()')
        for word in ord_fil:                # Sjekker om ordene er i dict og legger til.
            if word in ord_dict:
                ord_dict[word] += 1
            else:
                ord_dict[word] = 1
    print(ord_dict)


except IOError as e:
    print("Feil i håndtering av fil: " + str(e))
except UnicodeDecodeError as e:
    print("Feil i koding av tekstfil: " + str(e))
except ValueError as e:
    print("Fila inneholder noe i tall-posisjonen som ikke er et tall! " + str(e))