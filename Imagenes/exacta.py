import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import spsolve
from scipy.sparse import diags, kron, identity
import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from scipy.sparse.linalg import spsolve
from scipy.sparse import csc_matrix

IntArray = NDArray[np.int16]

data = scipy.io.loadmat('bordes2.mat')
u: IntArray = data["bordes2"]


N, M = u.shape
Dx = diags([1, -2, 1], [-1, 0, 1], shape=(N, N))
Dy = diags([1, -2, 1], [-1, 0, 1], shape=(M, M))


A = kron(identity(M), Dx) + kron(Dy, identity(N))

f_vector = u.flatten()

assert f_vector.shape == (A.shape[0],), "Dimensión incorrecta de f_vector"

u_exacta_vector = spsolve(A, f_vector)
u_exacta = u_exacta_vector.reshape((N, M))




plt.imsave("u_exacta_1.png", u_exacta, cmap="gray") 