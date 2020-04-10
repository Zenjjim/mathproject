from scipy.sparse.linalg import spsolve, inv, norm
from scipy.sparse import csc_matrix
from numpy.linalg import cond
from math import inf
from oppgave2 import lagA
from oppgave3 import calc_y_c


def oppgave5():
    w = 0.3  # m
    t = 0.03  # m
    g = 9.81  # N
    d = 480  # kg/m^3
    L = 2  # m
    x = L
    E = 1.3 * 10**10  # N/m^2
    I = (w*t**3)/12
    f_x = -d*w*t*g
    y = f_x / (24 * E * I) * (x ** 2) * (x ** 2 - 4 * L * x + 6 * L ** 2)

    for i in range(1, 12):
        n = 10 * 2 ** i
        m = calc_y_c(n)
        print(i, "&", n, "&", cond(lagA(n), p=inf), "&", y-m[-1], "\\\\\n\hline")

oppgave5()
