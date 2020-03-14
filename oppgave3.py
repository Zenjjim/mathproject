from scipy.sparse.linalg import spsolve
from numpy import power
from oppgave2 import lagA


def calc_y_c(n):
    w = 0.3  # m
    t = 0.03  # m
    g = 9.81  # N
    d = 480  # kg/m^3
    L = 2  # m
    E = 1.3 * 10**10  # N/m^2
    I = (w*t**3)/12
    f = -d*w*t*g
    h = L/n
    f_x = [(h ** 4 / (E * I)) * f] * n
    A = lagA(n)
    y = spsolve(A, f_x)
    return y
