import turtle


def sekskant(lengde=50, farge='blue'):
    turtle.fillcolor(farge)
    turtle.begin_fill()
    for i in range(6):
        turtle.forward(lengde)
        turtle.right(60)
    turtle.end_fill()
    # turtle.done()


def multsekskant(lengde=50, rader=1, kolonner=1, avstand=100):
    start_punkt = 0
    color = 0
    for x in range(rader):          # Rader
        for x in range(kolonner):   # Kolonner
            turtle.pendown()
            if (color % 2) == 0:
                sekskant(lengde, 'red')
            else:
                sekskant(lengde, 'blue')
            turtle.penup()
            turtle.forward(avstand)
            start_punkt += 1
            color += 1
        turtle.right(180)                       # Får "turtle'n" tilbakestilt klar for å tegne ny rad.
        turtle.forward(avstand*start_punkt)
        turtle.left(90)
        turtle.forward(avstand)
        turtle.left(90)
        start_punkt = 0


if __name__ == '__main__':
    # lengde_str = input('Lengde: ')
    # lengde = float(lengde_str)
    # farge = input('Farge: ')

    # utålmodig.
    turtle.speed(100)
    # setter startpunk oppe til venstre
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    multsekskant(40, 5, 3, 100)
    turtle.done()