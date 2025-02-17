import scipy.io
import numpy as np
import matplotlib.pyplot as plt
from numpy.typing import NDArray
from scipy.sparse import diags, kron, identity, csr_matrix
from scipy.sparse.linalg import spsolve
from tqdm import tqdm  # Para visualizar el progreso

IntArray = NDArray[np.int16]

def matriz_tridiagonal(N, diagonal=-2, off_diagonal=1):
    """
    Genera una matriz tridiagonal dispersa de tamaño NxN con:
    - `diagonal`: valor en la diagonal principal.
    - `off_diagonal`: valores en las diagonales superiores e inferiores.
    """
    return diags([off_diagonal, diagonal, off_diagonal], [-1, 0, 1], shape=(N, N), format='csr')

def cargar_datos(nombre_archivo: str):
    """
    Carga datos desde un archivo .mat.
    """
    data = scipy.io.loadmat(nombre_archivo)
    return data[list(data.keys())[-1]]

def construir_matriz_A(N, M):
    """
    Construye la matriz dispersa A usando el operador de Laplace 2D.
    """
    Dx = matriz_tridiagonal(N*N, diagonal=-2, off_diagonal=1)
    Dy = diags([1, -2, 1], [-1, 0, 1], shape=(M, M), format='csr')
    return csr_matrix(Dx + kron(Dy, identity(N, format='csr')))

def jacobi(A, b, x0=None, tol=1e-6, max_iter=100):
    """
    Implementación del método de Jacobi con barra de progreso.
    """
    A = csr_matrix(A)  # Asegurar que A sea dispersa
    D = A.diagonal()
    R = A - diags(D, 0, format='csr')
    x = np.zeros_like(b) if x0 is None else x0.copy()

    for i in tqdm(range(max_iter), desc="Iteraciones de Jacobi"):
        x_new = (b - R @ x) / D
        if np.linalg.norm(x_new - x) < tol:
            print(f"Convergencia alcanzada en {i+1} iteraciones.")
            break
        x = x_new

    return x

# Cargar datos
archivo_mat = 'bordes2.mat'  # Se puede cambiar fácilmente
u: IntArray = cargar_datos(archivo_mat)

# Configuración de matrices
N, M = u.shape
A = construir_matriz_A(N, M)
f_vector = u.flatten()

# Resolver usando Jacobi
u_jacobi_vector = jacobi(A, f_vector)
u_jacobi = u_jacobi_vector.reshape((N, M))

# Guardar resultado
plt.imsave("u_jacobi_2.png", u_jacobi, cmap="gray")  # Guarda en escala de grises
