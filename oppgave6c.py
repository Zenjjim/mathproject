import scipy as sp
import math as m
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt

# Tidligere oppgaver
from oppgave2 import lagA


def solve(A, b):
    y = spsolve(A, b)
    s = y.shape
    f = y[s[0]-1]
    return f


def main():
    E = 1.3*10**10  # N/m^2
    I = (0.3*0.03**3)/12  # I = (wd^3)/12

    # f(x) er konstant når massen er lik egenmassen, f(x) = -480*w*d*g
    fx = -480*0.3*0.03*9.81  # kg*m/s^2*m
    p = 100  # kg/m
    L = 2
    x = L

    # eksakt løsning
    y2halv = ((fx / (24 * E * I)) * (x ** 2) *
              ((x ** 2) - (4 * L * x) + (6 * (L ** 2))))
    y2halv2 = (((9.81 * p * L) / (E * I * m.pi)) * ((L ** 3 / m.pi ** 3)
                                                    * 0 - (x ** 3 / 6) + ((L * x ** 2) / 2) - ((2 * L ** 2) / m.pi**2)))
    bibkj = m.sin(m.pi*x/L)
    y2 = y2halv - y2halv2
    print("y2: ", y2)
    B = [0.0]*12
    ntab = [0.0]*12

    for i in range(1, len(B)+1):
        n = 10*2**i
        h = L / n  # h = L/n, der L = 2.0 meter
        b = [0.0]*n
        for j in range(0, n):
            sx = -100 * 9.81 * m.sin(m.pi / 2 * (h*(j+1)))
            b[j] = (h ** 4 / (E * I)) * (fx + sx)

        A = lagA(n)
        print(n, " : ", solve(A, b))

        #feilen = eksakt - utregnet
        B[i-1] = (abs(abs(y2) - abs(solve(A, b))))
        ntab[i-1] = (n)

    #plt.plot(y2, solve(A, b))
    plt.loglog(ntab, B)
    plt.ylabel("feil")
    plt.xlabel("n")
    plt.show()

main()
