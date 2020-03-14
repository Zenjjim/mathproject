from scipy.sparse.linalg import spsolve, inv, norm
from math import inf
from oppgave2 import lagA

def oppgave5():
  w = 0.3 #m
  t = 0.03 #m
  g = 9.81 #N
  d = 480 #kg/m^3
  L = 2 #m
  x = L
  E = 1.3 * 10**10 #N/m^2
  I = (w*t**3)/12
  f_x = -d*w*t*g
  for i in range (1, 12):
    n = 10 * 2 ** i
    h = L/n

    m = [(h ** 4) / (E * I) * f_x] * n

    y = f_x / (24 * E * I) * x ** 2 * (x ** 2 - 4 * L * x + 6 * L ** 2)
    
    A = lagA(n)
    invA = inv(A)

    print("Eksponent: ", i, ", n = ", n)
    print("Kondisjonstall: ", norm(A, ord=inf) * norm(invA, ord=inf))

oppgave5()