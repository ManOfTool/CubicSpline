from Cubicspline import *
import numpy as np
import matplotlib.pyplot as plt

n = int(input('Value of n = '))

x, fx, h = enterNodes(n)

a = fx
b, c, d = coeBCD(n, a, h)

retDisplay(n, x, a, b, c, d)

xx = float(input('Enter value to predict: '))

l_most = getInterval(xx, n, x)
value = predictValue(xx, x[l_most], a[l_most], b[l_most], c[l_most], d[l_most])

print('When x = {}, S(x) = {}'.format(xx, value))
