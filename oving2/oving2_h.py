import turtle
import oving2_cd as a




def rart(size):
    for x in range(5):
        if (x % 2 ) == 1:
            white = 1
        else:
            white = 0
        for i in range(5):
            if (i % 2) == 1 and white == 1:
                color = 'red'
            else:
                color = 'blue'
            a.sekskant(size, color)
            turtle.penup()
            if (i % 2) == 0:
                turtle.forward(size)
                turtle.right(60)
                turtle.forward(size)
                turtle.left(60)
            else:
                turtle.forward(size)
                turtle.left(60)
                turtle.forward(size)
                turtle.right(60)
            turtle.pendown()
        turtle.penup()
        turtle.right(180)
        turtle.forward(size*7.5)
        turtle.left(90)
        turtle.forward(size*0.8)
        turtle.left(90)
        turtle.pendown()
                    



    

if __name__ == '__main__':
    turtle.penup()
    turtle.goto(-200, 200)
    turtle.pendown()
    turtle.speed(20)

    rart(25)
    turtle.done()
