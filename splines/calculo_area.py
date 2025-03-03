import numpy as np

def area_gauss(x, y):
    """
    Calcula el área de un polígono definido por los puntos (x[i], y[i])
    usando la fórmula de Gauss (shoelace).
    Asume que (x, y) describen el contorno en orden.
    """
    n = len(x)
    area_sum = 0.0
    
    for i in range(n-1):
        area_sum += x[i] * y[i+1] - x[i+1] * y[i]
    
    area_sum += x[n-1] * y[0] - x[0] * y[n-1]
    
    return 0.5 * abs(area_sum)

# ------------------------------------------------------------------------
# USO
# ------------------------------------------------------------------------
if __name__ == "__main__":
 
    points = np.load("datos_julio.npy")  
    
    x, y = zip(*points)  
    x = np.array(x)
    y = np.array(y)
    num_eliminar = 0

    if len(x) > num_eliminar:
        # Eliminar los primeros 10 elementos
        x = x[num_eliminar:]
        y = y[num_eliminar:]
    else:
        print("El array tiene menos de 10 elementos, no se puede eliminar.")


    
    # Calcular el área
    A = area_gauss(y, x) * 22**2
    print("Área estimada de la mano:", A)
