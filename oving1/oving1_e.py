# Pris for pakker ut ifra kg 
# Med funksjon for å regne total pris for flere pakker.
# Her er det også en maks pris som bruker setter.

tillat_pris_streng = input('Maks beløp?: ')
pakke_kg_streng = input('Skriv inn vekt på pakke i kg: ')
tillat_pris_flyt = float(tillat_pris_streng)
totalpris = 0   # Setter initialverdi.

# While pakker sin totalpris blir kalkulert innenfor budsjettet.
while pakke_kg_streng != '':
    pakke_kg_flyt = float(pakke_kg_streng)
    if pakke_kg_flyt > 35:
        print('Pakker over 35 kilo er ikke tillat.')
    elif pakke_kg_flyt > 25:
        print('Mellom 25 og 35 kg: 381,-')
        totalpris += 381
    elif pakke_kg_flyt > 10:
        print('Mellom 10 og 25 kg: 268,-')
        totalpris += 268
    elif pakke_kg_flyt > 0:
        print('Opp til 10kg: 149,-')
        totalpris += 149
    else:
        print('Feil: Vekt kan ikke være 0 eller negativ')
        break
    if totalpris > tillat_pris_flyt:
        print('Siste pakke ikke registrert: Tillat pris oversteget.')
        break
    pris_budsjett = totalpris
    pakke_kg_streng = (input('Skriv inn vekt på neste pakke i kg eller trykk enter for totalpris: ')) 

# Skriver ut prisen innenfor budsjettet.
print('Totalprisen blir: ' + str(pris_budsjett))