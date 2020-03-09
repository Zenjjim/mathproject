from oppgave2 import lagA
from numpy import dot

def y_e_vektor():
    w = 0.3 #m
    t = 0.03 #m
    g = 9.81 #N
    d = 480 #kg/m^3
    L = 2 #m
    E = 1.3 * 10**10 #N/m^2
    I = (w*t**3)/12
    f_x = -d*w*t*g

    y_e = []

    for i in range(0, 10):
        x = (i+1)*0.2
        y_e.append(f_x / 24 / E / I * (x**2) * (x**2 - 4*x*L + 6*L**2))

    return y_e

# TODO: Skriv om
def oppgave4c():
    A = lagA(10)
    y_e = y_e_vektor()
    h = 0.2
    return (1 / h**4) * dot(A, y_e)

print(oppgave4c())