import numpy as np


with open('./ovingsoppgaver/oving3/tall_filtrert.txt', 'r') as vindmaalinger:

    # individuellmaaling = list()
    # for i in vindmaalinger:
    #     individuellmaaling += i.split()
    maalinger = []
    try:
        for line in vindmaalinger:
            maalinger.append(float(line.strip()))   # Stripper \n og gjør til float og settes på slutten av maalinger.
    except ValueError as e:
        print('Value error: ' + str(e))

# Regner ut antall målinger, max/min og gjennomsnittet av målinger.
antall = len(maalinger)   
maks_maaling = max(maalinger)
min_maaling = min(maalinger)
gjennomsnitt_maaling = np.mean(maalinger)


# Skriver dette inn i en ny tekstfil.
with open('./ovingsoppgaver/oving3/vindmålingerutskrift.txt', 'w') as utskrift:
    utskrift.write('Antall: %s\n' %antall)
    utskrift.write('Gjennomsnitt: %s\n' %format(gjennomsnitt_maaling, '.2f'))
    utskrift.write('Maksimum: %s\n' %format(maks_maaling, '.2f' ))
    utskrift.write('Minimum: %s\n' %format(min_maaling, '.2f'))