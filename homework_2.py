import turtle
import math


def draw_square(t, size):
    for _ in range(4):
        t.forward(size)
        t.left(90)


def pythagoras_tree(t, size, depth):
    if depth == 0:
        return

    draw_square(t, size)

    x, y = t.position()
    angle = t.heading()

    t.forward(size)
    t.left(45)
    pythagoras_tree(t, size / math.sqrt(2), depth - 1)

    t.setposition(x, y)
    t.setheading(angle)

    t.forward(size)
    t.right(45)
    pythagoras_tree(t, size / math.sqrt(2), depth - 1)

    t.setposition(x, y)
    t.setheading(angle)


def main():
    depth = int(input("Введіть рівень рекурсії: "))

    screen = turtle.Screen()
    screen.title("Фрактал: Дерево Піфагора (квадрати)")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-40, -250)
    t.setheading(90)
    t.pendown()

    pythagoras_tree(t, 100, depth)

    turtle.done()


if __name__ == "__main__":
    main()
