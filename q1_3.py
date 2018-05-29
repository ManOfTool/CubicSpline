from Cubicspline import *

n = int(input('Value of n = '))

x, fx, h = enterNodes(n)

a = fx
b, c, d = coeBCD(n, a, h)

retDisplay(n, x, a, b, c, d)