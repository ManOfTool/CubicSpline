from Cubicspline import *

n = 12
h = []

t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = [7, 4, 3, 0, -3, -4, -7, -4, -3, 0, 3, 4, 7]
y = [0, 2, 5, 8, 5, 2, 0, -2, -5, -8, -5, -2, 0]

for j in range(0, n):
    h.append(t[j+1] - t[j])

a1 = x
b1, c1, d1 = coeBCD(n, a1, h)

a2 = y
b2, c2, d2 = coeBCD(n, a2, h)

print('Coefficient of Sx(t):')
retDisplay(n, t, a1, b1, c1, d1)

print('')
print('Coefficient of Sy(t):')
retDisplay(n, t, a2, b2, c2, d2)

for i in range(0, n):
    tt = np.arange(t[i], t[i+1], 0.0002)

    tmp = tt - t[i]

    xx = a1[i] + b1[i] * tmp + c1[i] * pow(tmp, 2) + d1[i] * pow(tmp, 3)
    yy = a2[i] + b2[i] * tmp + c2[i] * pow(tmp, 2) + d2[i] * pow(tmp, 3)

    plt.plot(xx, yy)

plt.savefig('q7.png')