from Cubicspline import *
import math

n = int(input('Value of n: '))

t = []
x = []
y = []
h = []

for i in range(0, n+1):
    t.append(round(0 + (2 * np.pi / n) * i, 6))

x = np.cos(t)
y = np.sin(t)

for i in range(0, n+1):
    x[i] = round(x[i], 6)
    y[i] = round(y[i], 6)

for j in range(0, n):
    h.append(t[j+1] - t[j])

a1 = x
b1, c1, d1 = coeBCD(n, a1, h)

a2 = y
b2, c2, d2 = coeBCD(n, a2, h)

f_name = input('Enter file name: ')
with open(f_name + '.txt', 'a') as f:
    # print('Coefficient of Sx(t):')
    retDisplay(n, t, a1, b1, c1, d1, f)

    # print('')
    # print('Coefficient of Sy(t):')
    retDisplay(n, t, a2, b2, c2, d2, f)

for i in range(0, n):
    tt = np.arange(t[i], t[i+1], 0.0002)

    tmp = tt - t[i]
    xx = a1[i] + b1[i] * tmp + c1[i] * pow(tmp, 2) + d1[i] * pow(tmp, 3)
    yy = a2[i] + b2[i] * tmp + c2[i] * pow(tmp, 2) + d2[i] * pow(tmp, 3)

    plt.plot(xx, yy)

# title = input('Enter graph name: ') + '.png'
plt.savefig(f_name + '.png')
print('\nFigure ' + f_name + '.png' + ' saved!!\n------------------------------------------------------------------------------')
