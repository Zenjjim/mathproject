from scipy.sparse.linalg import spsolve, inv, norm
from scipy.sparse import csc_matrix
from numpy.linalg import cond
from math import inf
from oppgave2 import lagA
import math
from matplotlib.pyplot import loglog, plot, show


def calc_y_c(n):
	w = 0.3  # m
	t = 0.03  # m
	g = 9.81  # N
	d = 480  # kg/m^3
	L = 2  # m
	E = 1.3 * 10**10  # N/m^2
	I = (w*t**3)/12
	f = -d*w*t*g
	p = 100 #km/m
	h = L/n
	b = [0.0]*n
	for k in range(n):
		s = -p*g*math.sin(math.pi/L*h*(k+1))
		b[k]=([(h ** 4 / (E * I)) * (f+s)])
	A = csc_matrix(lagA(n))
	y = spsolve(A, b)
	return y


def oppgave6b():
	w = 0.3  # m
	t = 0.03  # m
	g = 9.81  # N
	p = 100 #kg/m
	d = 480  # kg/m^3
	L = 2  # m
	E = 1.3 * 10**10  # N/m^2
	I = (w*t**3)/12
	f_x = -d*w*t*g
	x = L

	y1 = f_x / (24 * E * I) * (x ** 2) * ((x ** 2) - 4 * L * x + 6 * L ** 2)
	y2 = ((g*p*L/(E*I*math.pi))*((L**3)/(math.pi**3)*math.sin(math.pi/L*x)-((x**3)/6)+(L*(x**2)/2)-(x*(L**2)/(math.pi**2))))
	y = y1-y2

	y_list = [0.0]*11
	for i in range(1, 12):
		n = 10 * 2 ** i

		m = calc_y_c(n)
		print(f"Number {i}")
		print(f"Calculated {m[-1]}")
		print(f"Exact {y}")
		print("-----------")
		y_list[i-1] = (m[-1])
	plot(list(range(1, 12)), [y]*11, 'r', list(range(1, 12)), (y_list), 'b')
	show()

oppgave6b()
