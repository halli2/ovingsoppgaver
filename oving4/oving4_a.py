import numpy as np
import matplotlib.pyplot as plt

# Definerer funksjon som regner ut renter.
def renter(startverdi, renter, aar):
    okningstall = 1.0 + renter/100
    verdi = startverdi * (okningstall ** aar)
    return verdi

# Lager liste fra 0-41 (brukes som år i funksjonen)
# aar_liste = range(40) 
aar_liste = []
for i in range(41):
    aar_liste.append(i)

# Får ut verdien etter renter for hvert år.
rente_liste = []
for x in aar_liste:
    rente_liste.append(renter(150000, 2.89, aar_liste[x]))

# Plotter.
plt.plot(aar_liste, rente_liste)
plt.xlabel('År')
plt.ylabel('Kroner')
plt.show()