from scipy.sparse import diags, kron, identity
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from scipy.sparse.linalg import spsolve

IntArray = NDArray[np.int16]

data = scipy.io.loadmat('bordes2.mat')
u: IntArray = data["bordes2"]


N, M = u.shape
Dx = diags([1, -2, 1], [-1, 0, 1], shape=(N, N))
Dy = diags([1, -2, 1], [-1, 0, 1], shape=(M, M))

A = kron(identity(M), Dx) + kron(Dy, identity(N))


f_vector = u.flatten()
N, M = u.shape  


def gauss_seidel(A, b, x0=None, tol=1e-6, max_iter=100):
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(len(b)):
            x[i] = (b[i] - A[i, :i].dot(x[:i]) - A[i, i+1:].dot(x[i+1:])) / A[i, i]
        if np.linalg.norm(x - x_old) < tol:
            break

    return x

u_gauss_seidel_vector = gauss_seidel(A, f_vector)
u_gauss_seidel = u_gauss_seidel_vector.reshape((N, M))


plt.imsave("u_gauss_seidel_2.png", u_gauss_seidel, cmap="gray")  
