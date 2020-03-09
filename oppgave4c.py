from oppgave2 import lagA

def y_e_vektor():
    # E = N/m^2
    E = 1.3*10**10 # 10^10
    # I = (wd^3)/12
    I = (0.3 * 0.03 ** 3) / 12
    L = 2
    f_x = -480 * 0.3 * 0.03 * 9.81
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
    return (1 / h**4) * A * y_e



print(y_e_vektor())
print(oppgave4c())