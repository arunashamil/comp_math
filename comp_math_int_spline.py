import numpy as np

x = np.array([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1])
y = np.array([0.000, 0.033, 0.067, 0.100, 0.133, 0.166, 0.199, 0.231, 0.264, 0.296, 0.327])
xo = 0.95

n = len(x) - 1
a = np.zeros(n + 1)

for i in range(0, n + 1):
    a[i] = y[i]

b = np.zeros(n)
d = np.zeros(n)

h = np.zeros(n)
for i in range(n):
    h[i] = x[i + 1] - x[i]

alpha = np.zeros(n)
for i in range(1,n):
    alpha[i] = (3 / h[i]) * (a[i + 1] - a[i]) - (3 / h[i - 1]) * (a[i] - a[i - 1])

c = l = mu = z = np.zeros(n + 1)
l[0] = 1
mu[0] = z[0] = 0

for i in range(1, n):
    l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * mu[i - 1]

for i in range(1, n):
    mu[i] = h[i] / l[i]

for i in range(1, n):
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

l[n] = 1
z[n] = c[n] = 0

for i in reversed(range(n)):
    c[i] = z[i] - mu[i] * c[i + 1]

for i in reversed(range(n)):
    b[i] = (a[i + 1] - a[i]) / h[i] - h[i] * (c[i + 1] + 2 * c[i]) / 3
    d[i] = (c[i + 1] - c[i]) / (3 * h[i])

a = list(a)
b = list(b)
c = list(c)
d = list(d)
x = list(x)

splines = []
splines.append(a)
splines.append(b)
splines.append(c)
splines.append(d)
splines.append(x)
#print(splines)
num = 0 # индекс точки, за которой располагается наша 0.95
while x[i] <= xo:
    num = i
    i += 1

#print(num)

a_o = splines[0][num]
b_o = splines[1][num]
c_o = splines[2][num]
d_o = splines[3][num]

polynom = a_o + b_o * (xo - x[num]) + c_o * (xo - x[num])**2 + d_o * (xo - x[num]) ** 3
print(polynom)

# Получилось 0.31156202933225874