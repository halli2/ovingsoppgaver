import gallon_to_litre as gtr

gallon = input('Gallon: ')
# kaller funksjonen fra gtr filen.
litre = gtr.gallon_to_litre(gallon)
# 2 desimaler.
# print(
#     format(litre, '.2f')
#      + ' liter.'
# )
print(f"Antall liter: {litre:.2f}")
