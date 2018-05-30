from Cubicspline import *

n = 4
h = []

t = [0, 0.25, 0.5, 0.75, 1]
x = [-1, 0, 1, 0, 1]
y = [0, 1, 0.5, 0, -1]

for j in range(0, n):
    h.append(round(t[j+1] - t[j], 6))

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

plt.savefig('q6.png')