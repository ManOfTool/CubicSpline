from Cubicspline import *

n = int(input('Value of n = '))

x, fx, h = enterNodes(n)

a = fx
b, c, d = coeBCD(n, a, h)

with open('q1.txt', 'a') as f:
    retDisplay(n, x, a, b, c, d, f)

saveFigure(n, x, a, b, c, d, 'q1_1.png')