import turtle as t
import random


tim = t.Turtle()
t.colormode(255)
tim.shape("arrow")
tim.color("blue")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


tim.speed("fastest")

def draw_spirograph(size_of_gap):

    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() +  size_of_gap)


draw_spirograph(5)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#
# def draw_shape(no_of_sides):
#
#    for _ in range(no_of_sides):
#        tim.forward(100)
#        tim.left(360/no_of_sides)
#
#
# for _ in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(_)


screen = t.Screen()
screen.exitonclick()
