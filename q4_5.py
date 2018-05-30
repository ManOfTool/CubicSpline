from Cubicspline import *

nn = int(input('Value of n: '))
n = 10

x = []
fx = []
h = []

for i in range(0, n+1):
    xx = round(-2 + (4 / nn) * i, 6)
    fxx = round(1 / (1 + 25 * pow(xx, 2)), 6)

    x.append(xx)
    fx.append(fxx)

for j in range(0, n):
    h.append(round(x[j+1] - x[j], 6))

a = fx

b, c, d = coeBCD(n, a, h)

f_name = input('Enter file name: ')
with open(f_name + '.txt', 'a') as f:
    retDisplay(n, x, a, b, c, d, f)

saveFigure(n, x, a, b, c, d, f_name + '.png')
