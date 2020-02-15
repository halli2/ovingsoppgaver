# Tegner rader og kolonner i turtlegraf.
import turtle

# Bruker putter inn antall rader og kolonner
antall_kolonner = input('Antall kolonner: ')
antall_kolonner_tall = int(antall_kolonner)
antall_rader = input('Antall rader: ')
antall_rader_tall = int(antall_rader)

# Uncomment for å få det raskere.
turtle.speed(100) 

start_punkt = 0 # initialverdi

for x in range(antall_rader_tall):          # Rader
    for x in range(antall_kolonner_tall):   # Kolonner
        for x in range(4):                  # Celler
            turtle.forward(50)
            turtle.right(90)
        turtle.forward(50)
        start_punkt += 1
    turtle.right(180)                       # Får "turtle'n" tilbakestilt klar for å tegne ny rad.
    turtle.forward(50*start_punkt)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    start_punkt = 0

# Forhindrer vinduet til å lukkes når scriptet er ferdig
turtle.done()