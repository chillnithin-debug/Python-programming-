for row in range(6):
    for col in range(7):
        if (row == 0 and col % 3 != 0) or \
           (row == 1 and col % 3 == 0) or \
           (row - col == 2) or \
           (row + col == 8):
            print("*", end=" ")
        else:
            print(end="  ")
    print()


    import matplotlib.pyplot as plt
import numpy as np

t = np.linspace(0, 2 * np.pi, 100)
x = 16 * np.sin(t)**3
y = 13 * np.cos(t) - 5 * np.cos(2*t) - 2*np.cos(3*t) - np.cos(4*t)

plt.plot(x, y, 'r-', linewidth=2)
plt.show()

import turtle

pen = turtle.Turtle()

# Defining a method to draw a curve
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

# Defining method to draw a full heart
def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

heart()
pen.ht() # Hide the turtle
turtle.done() 
