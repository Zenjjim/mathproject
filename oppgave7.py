from numpy import ones
from scipy.sparse import spdiags, csr_matrix, lil_matrix
from scipy.sparse.linalg import spsolve
from matplotlib import pyplot

def lagA(n):
    e = ones(n)
    A = lil_matrix(spdiags(
        [e, -4.0 * e, 6.0 * e, -4.0 * e, e], 
        [-2, -1, 0, 1, 2],
        n, n)
    )
    B = csr_matrix([
        [16.0, -9.0, (8 / 3), (-1 / 4)],
        [(16 / 17), (-60 / 17), (72 / 17), (-28 / 17)],
        [(-12 / 17), (96 / 17), (-156 / 17), (72 / 17)]
    ])

    A[0, 0: 4] = B[0, :]
    A[n-2, n-4: n] = B[1, :]
    A[n-1, n-4: n] = B[2, :]
    return csr_matrix(A)

if __name__ == "__main__":
    B = [0.0]*12
    n_tabell = [0.0]*12
    f_x = -480*0.3*0.03*9.81
    s_x = -9.81*50/0.3
    E = 1.3*10**10
    I = (0.3*0.03**3)/12

    for i in range(0, len(B)):
        n = 10*2**(i+1)
        n_tabell[i] = i+1
        h = 2/n
        b = [(h ** 4 / (E * I)) * f_x] * n
        end = round(n*(1-0.15))

        for j in range(end, n):
            b[j] += ((h ** 4 / (E * I))*s_x)

        A = lagA(n)
        y = spsolve(A, b)
        s = y.shape
        B[i] = abs(y[s[0]-1])

    pyplot.plot(n_tabell, B)
    pyplot.ylabel("Forbøyning")
    pyplot.xlabel("n")
    pyplot.show()