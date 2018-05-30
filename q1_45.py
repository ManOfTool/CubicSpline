from Cubicspline import *

n = int(input('Value of n: '))

x = []
fx = []
h = []

for i in range(0, n+1):
    xx = round(-2 + (4 / n) * i, 6)
    fxx = round(1 / (1 + 25 * pow(xx, 2)), 6)

    x.append(xx)
    fx.append(fxx)

for j in range(0, n):
    h.append(round(x[j+1] - x[j], 6))

a = fx

b, c, d = coeBCD(n, a, h)

retDisplay(n, x, a, b, c, d)

title = input('Enter graph name: ') + '.png'
saveFigure(n, x, a, b, c, d, title)
