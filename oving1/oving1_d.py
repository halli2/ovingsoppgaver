# Turtle graffik og for loops
import turtle
turtle.penup()
turtle.forward(100)
turtle.pendown()

# Ble tegnet en stjerne med 9 hjørner.
for tall in range(9):
    turtle.right(160)
    turtle.forward(200)

# En stjerne med sirkel i midten og 24 hjørner.
# for tall in range(24):
#     turtle.right(165)
#     turtle.forward(200)

# Trekant
# for tall in range(3):
#     turtle.speed(22)
#     turtle.right(120)
#     turtle.forward(200)

# Kvadrat
# for tall in range(4):
#     turtle.speed(22)
#     turtle.right(90)
#     turtle.forward(200)

# Sirkel (lagger litt?)
# for tall in range(360):
#     turtle.speed(360)
#     turtle.right(1)
#     turtle.forward(3)

# "firkanta stjerne" med sirkel i midten.
# for tall in range(18):
#     turtle.speed(22)
#     turtle.right(100)
#     turtle.forward(200)

turtle.done()