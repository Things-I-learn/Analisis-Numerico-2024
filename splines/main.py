import numpy as np
import matplotlib.pyplot as plt

def spline_cubico_natural(x, y):
    x = np.array(x, dtype=float)
    y = np.array(y, dtype=float)
    n = len(x)
    
    a = y.copy()
    h = x[1:] - x[:-1]
    alpha = np.zeros(n-1)
    for i in range(1, n-1):
        alpha[i] = 3.0 * ((a[i+1] - a[i]) / h[i] - (a[i] - a[i-1]) / h[i-1])
    
    l = np.ones(n)
    mu = np.zeros(n)
    z = np.zeros(n)
    l[0] = 1.0
    
    for i in range(1, n-1):
        l[i] = 2.0 * (x[i+1] - x[i-1]) - h[i-1] * mu[i-1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    
    c = np.zeros(n)
    for j in range(n-2, -1, -1):
        c[j] = z[j] - mu[j] * c[j+1]
    
    b = np.zeros(n-1)
    d = np.zeros(n-1)
    for i in range(n-1):
        b[i] = ((a[i+1] - a[i]) / h[i]) - (h[i]/3.0)*(2.0*c[i] + c[i+1])
        d[i] = (c[i+1] - c[i]) / (3.0*h[i])
    
    def spline_func(x_eval):
        x_eval_arr = np.array(x_eval, ndmin=1, dtype=float)
        s_vals = np.zeros_like(x_eval_arr)
        
        for idx, val in enumerate(x_eval_arr):
            if val <= x[0]:
                i = 0
            elif val >= x[-1]:
                i = n-2
            else:
                i = np.searchsorted(x, val) - 1
            
            dx = val - x[i]
            s_vals[idx] = a[i] + b[i]*dx + c[i]*(dx**2) + d[i]*(dx**3)
        
        return s_vals[0] if np.isscalar(x_eval) else s_vals
    
    return spline_func, (a, b, c, d)

# Cargar datos
datos_nombre = "datos_eguar"  # Nombre identificador
data = np.load(f"{datos_nombre}.npy")  # Debe contener [(x0, y0), (x1, y1), ...]
x, y = zip(*data)
x = np.array(x)
y = np.array(y)

# Definir t
n = len(x)
t = np.arange(n)

# Construir los splines paramétricos
splineX, _ = spline_cubico_natural(t, x)
splineY, _ = spline_cubico_natural(t, y)

# Evaluar en varios puntos
puntos = 1000
t_eval = np.linspace(t[0], t[-1], puntos)
X_eval = splineX(t_eval)
Y_eval = splineY(t_eval)

# Graficar
plt.figure()
plt.plot(X_eval, Y_eval, label='Spline mano')
plt.plot(x, y, 'ro', label='Puntos originales')
plt.axis('equal')
plt.legend()
titulo = f"Spline {datos_nombre} - {puntos} puntos evaluados"
plt.title(titulo)

# Guardar imagen
filename = f"spline_{datos_nombre}_{puntos}.png"
plt.savefig(filename, dpi=300)
# plt.show()

# print(f"Gráfico guardado como {filename}")
