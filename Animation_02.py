import turtle
colors = ["red", "blue", "green", "purple", "orange"]
turtle.speed(0)
for i in range(360):

    turtle.pencolor(colors[i % 5])
    turtle.forward(i)
    turtle.left(89)