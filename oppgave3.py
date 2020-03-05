from scipy.sparse.linalg import spsolve
from numpy import power
from oppgave2 import lagA

def calc_y_c():
  w = 0.3 #m
  t = 0.03 #m
  g = 9.81 #N
  d = 480 #kg/m^3
  L = 2 #m
  E = 1.3 * power(10, 10) #N/m^2
  n = 10
  I = w*power(d, 3)/12
  f = -d*w*t*g
  h = L/n
  f_x = [f] * n
  A = lagA(n)
  y = spsolve(A, f_x)
  return y
