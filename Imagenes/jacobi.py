from scipy.sparse import diags, kron, identity
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from scipy.sparse.linalg import spsolve

IntArray = NDArray[np.int16]

data = scipy.io.loadmat('bordes1.mat')
u: IntArray = data["bordes1"]


N, M = u.shape
Dx = diags([-1, 2, -1], [-1, 0, 1], shape=(N, N))
Dy = diags([-1, 2, -1], [-1, 0, 1], shape=(M, M))

A = kron(identity(M), Dx) + kron(Dy, identity(N))


f_vector = u.flatten()
N, M = u.shape  


def jacobi(A, b, x0=None, tol=1e-6, max_iter=10):
    D = A.diagonal()
    R = A - np.diagflat(D)
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for _ in range(max_iter):
        x_new = (b - R.dot(x)) / D
        if np.linalg.norm(x_new - x) < tol:
            break
        x = x_new.A1

    return x

u_jacobi_vector = jacobi(A, f_vector)
u_jacobi = u_jacobi_vector.reshape((N, M))

import matplotlib.pyplot as plt

plt.imsave("u_jacobi.png", u_jacobi, cmap="gray")  # Guarda en escala de grises
