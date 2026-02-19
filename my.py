from turtle import *

k = 20
tracer(0)
left(90)

for i in range(7):
    forward(k * 10)
    right(120 * k)

up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "red")

exitonclick()
