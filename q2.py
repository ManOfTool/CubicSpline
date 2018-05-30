from Cubicspline import *
import numpy as np
import matplotlib.pyplot as plt


n = int(input('Value of n = '))

x, fx, h = enterNodes(n)

a = fx
b, c, d = coeBCD(n, a, h)

with open('q2.txt', 'a') as f:
    retDisplay(n, x, a, b, c, d, f)

saveFigure(n, x, a, b, c, d, 'q1_2.png')

xx = float(input('Predict the position of the car when x = '))
l_most = getInterval(xx, n, x)
value = predictValue(xx, x[l_most], a[l_most], b[l_most], c[l_most], d[l_most])
print('When x = {}, S(x) = {}'.format(xx, value))