from math import inf
from numpy import ones
from numpy.linalg import norm
from scipy.sparse.linalg import inv, norm as sp_norm
from scipy.sparse import csc_matrix
from oppgave2 import lagA
from oppgave4c import oppgave4c

y4_c = oppgave4c()  # Numerisk fjerdederivert y''''_c

E = 1.3 * 10 ** 10  # N/m^2
I = (0.3 * 0.03 ** 3) / 12  # I = (wd^3)/12
f = -480 * 0.3 * 0.03 * 9.81  # kg*m/s^2*m
y4_e = (f / (E * I)) * ones((10, 1))  # Eksakt fjerdederivert y''''_e

foroverfeil = norm(y4_e - y4_c, ord=inf)
rel_foroverfeil = foroverfeil / norm(y4_e, ord=inf)
rel_bakoverfeil = 2**(-52)
feilforstorring = rel_foroverfeil / rel_bakoverfeil

A = lagA(10)
A = csc_matrix(A)
AI = inv(A)
cond_A = sp_norm(A, ord=inf) * sp_norm(AI, ord=inf)

print("foroverfeil: ", foroverfeil)
print("relativ foroverfeil:", rel_foroverfeil)
print("feilforstørring:", feilforstorring)
print("kondisjonstall cond(A):", cond_A)
