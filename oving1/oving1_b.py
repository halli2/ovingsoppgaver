# Pris for pakker ut ifra kg
pakke_kg = float(input('Skriv inn vekt på pakke i kg: ')) 
if pakke_kg > 35:
    print('Pakker over 35 kilo er ikke tillat.')
elif pakke_kg > 25:
    print('Mellom 25 og 35 kg: 381,-')
elif pakke_kg > 10:
    print('Mellom 10 og 25 kg: 268,-')
elif pakke_kg >= 0:
    print('Opp til 10kg: 149,-')
else:
    print('Feil: Vekt kan ikke være negativ')