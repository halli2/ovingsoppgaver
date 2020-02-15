import turtle
import oving2_cd as a

rader = input('Rader: ')
rader = int(rader)
kolonner = input('Kolonner: ')
kolonner = int(kolonner)

turtle.speed(100)
a.multsekskant(rader=rader, kolonner=kolonner)
turtle.done()