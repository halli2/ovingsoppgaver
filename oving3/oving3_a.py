# Pris for pakker ut ifra kg 
# Med funksjon for å regne total pris for flere pakker.

pakke_kg_streng = input('Skriv inn vekt på pakke i kg: ')
totalpris = 0   # Setter initialverdi.



while pakke_kg_streng != '':
    try:
        pakke_kg_flyt = float(pakke_kg_streng)
    except ValueError:
        print('Ulovlig flyttal.')
        break
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
    pakke_kg_streng = (input('Skriv inn vekt på neste pakke i kg eller trykk enter for totalpris: ')) 
print('Totalprisen blir: ' + str(totalpris))