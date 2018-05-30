import numpy as np
import matplotlib.pyplot as plt

ROUNDING = 6

def enterNodes(n):
    x = []
    fx = []
    h = []

    for i in range(0, n+1):
        xi, fxi = input('n = ' + repr(i).rjust(2) + ' : ').split()
        x.append(float(xi))
        fx.append(float(fxi))

    for j in range(0, n):
        h.append(round(x[j+1] - x[j], ROUNDING))

    return x, fx, h

#########################################

def coeBCD(n, a, h):
    e = []
    s = []
    b = []
    c = []
    d = []

    for i in range(2, n+1):
        e.append(round(3 * ((a[i] - a[i-1]) / h[i-1] - (a[i-1] - a[i-2]) / h[i-2]), ROUNDING))

    for i in range(0, n-1):
        s.append(round(2 * (h[i] + h[i+1]), ROUNDING))

    for i in range(1, n-1):
        s[i] = round(s[i] - (h[i] / s[i-1]) * h[i], ROUNDING)
        e[i] = round(e[i] - (h[i] / s[i-1]) * e[i-1], ROUNDING)

    c.append(round(e[len(e)-1] / s[len(s)-1], ROUNDING))
    for i in range(n - 2, 0, -1):
        c.insert(0, round((e[i-1] - h[i] * c[0]) / s[i-1], ROUNDING))
    c.insert(0, 0.000000000)
    c.append(0.000000000)

    for i in range(0, n):
        b.append(round((a[i+1] - a[i]) / h[i] - (h[i] * (2 * c[i] + c[i+1])) / 3, ROUNDING))
        d.append(round((c[i+1] - c[i]) / (3 * h[i]), ROUNDING))

    return b, c, d

#########################################

def retDisplay(n, x, a, b, c, d):
    print('j'.rjust(3), 'x'.rjust(10), 'a'.rjust(15), 'b'.rjust(15), 'c'.rjust(15), 'd'.rjust(15))
    print('------------------------------------------------------------------------------')
    for i in range(0, n):
            print(repr(i).rjust(3), repr(x[i]).rjust(10), repr(a[i]).rjust(15), repr(b[i]).rjust(15), repr(c[i]).rjust(15), repr(d[i]).rjust(15))

#########################################

def getInterval(xx, n, x):
    for i in range(0, n):
        if xx >= x[i] and xx < x[i+1]:
            print('{} is in interval [{}, {})'.format(xx, x[i], x[i+1]))
            break

        elif xx == x[i+1]:
            print('{} is in interval [{}, {}]'.format(xx, x[i], x[i+1]))

    return i

#########################################

def saveFigure(n, x, a, b, c, d, title):
    for i in range(0, n):
        xx = np.arange(x[i], x[i + 1], 0.0002)
        tmp = xx - x[i]
        y = a[i] + b[i] * tmp + c[i] * pow(tmp, 2) + d[i] * pow(tmp, 3)

        plt.plot(xx, y)
    # plt.show()
    plt.savefig(title)
    print('\nFigure ' + title + ' saved!!\n------------------------------------------------------------------------------')

#########################################

def predictValue(xx, x, a, b, c, d):
    tmp = xx - x

    return a + b * tmp + c * pow(tmp, 2) + d * pow(tmp, 3)

#########################################

def relatErr(pred_v, real_v):
    return abs((pred_v - real_v) / pred_v)
