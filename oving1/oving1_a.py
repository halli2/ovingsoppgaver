# Brukeren skriver inn fot og programmet skriver ut i meter.
FOT_I_METER = 0.3048
fot_streng = input('Tast inn fot: ')
fot_tall = float(fot_streng)

meter_tall = fot_tall * FOT_I_METER
print('Det blir %s meter.' %format(meter_tall, '5.3f'))