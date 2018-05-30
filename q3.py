from Cubicspline import *

ROUNDING = 6
x = []
fx = []
h = []

n = int(input('Value of n = '))

for i in range(0, n+1):
    xi, fxi = input('n = ' + repr(i).rjust(2) + ' : ').split()
    x.append(int(xi))
    fx.append(int(fxi))

for j in range(0, n):
    h.append(round(x[j+1] - x[j], ROUNDING))

a = fx
b, c, d = coeBCD(n, a, h)

with open('q3.txt', 'a') as f:
    retDisplay(n, x, a, b, c, d, f)

saveFigure(n, x, a, b, c, d, 'q1_3.png')

xx = int(input('Predict the populations in: '))
l_most = getInterval(xx, n, x)
value = predictValue(xx, x[l_most], a[l_most], b[l_most], c[l_most], d[l_most])
print('When x = {}, S(x) = {}\n'.format(xx, round(value)))

print('The real populations in 1960 was 179,323,175.\nCalculate the relative error: {}'.format(round(relatErr(value, 179323175), ROUNDING)))