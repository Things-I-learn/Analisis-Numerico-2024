## 🖥️ Reconstrucción de imágenes a partir de sus bordes

El operador Laplaciano en 2D se define como:

$$
\nabla^2 u(x,y) = \frac{\partial^2 u}{\partial x^2} + \frac{\partial^2 u}{\partial y^2}
$$

donde \( u(x, y) \) es una función que representa la intensidad de los píxeles de la imagen en el dominio espacial.  
El operador Laplaciano se utiliza para detectar bordes porque responde a las variaciones de la intensidad de los píxeles en la vecindad de cada punto. En áreas de la imagen donde la intensidad varía rápidamente (bordes), el Laplaciano tiene un valor alto, mientras que en áreas homogéneas (sin bordes) el Laplaciano es cercano a cero.  
El proceso de detección de bordes implica calcular el Laplaciano de la imagen \( u(x, y) \), lo que da como resultado un mapa de bordes.

En este ejercicio estamos interesados en reconstruir la imagen original \( u(x, y) \) a partir de los bordes detectados.  
Para esto debemos resolver la ecuación de Poisson en 2D:

$$
\nabla^2 u(x,y) = f(x,y) \tag{1}
$$

donde \( f(x, y) \) es el mapa de bordes.

El problema (1) puede ser discretizado en un sistema de ecuaciones lineales de la forma:

$$
A u = f
$$

donde \( A \) es una matriz que representa el operador Laplaciano discreto, \( u \) es el vector que contiene los valores de la imagen original en cada píxel (a reconstruir), y \( f \) es el vector que contiene los valores de los bordes detectados.

---

### 📌 Instrucciones:

Su tarea consiste en reconstruir las imágenes originales. En la página web del curso encuentran los archivos `bordes1.mat` y `bordes2.mat` que contienen los datos de cada fotografía.  
Siga los pasos descritos a continuación:

1. **Plantee el sistema lineal** \( A u = f \) a partir de la discretización del operador Laplaciano, empleando diferencias finitas centradas para aproximar las derivadas.  
   - La matriz \( A \) será una matriz dispersa que representa las conexiones entre los píxeles vecinos en una cuadrícula 2D.

2. **Utilice los métodos iterativos**: Jacobi, Gauss-Seidel y SOR, para solucionar el sistema lineal \( A u = f \), donde \( f \) son los datos `bordes1.mat` y `bordes2.mat`.

3. **Visualice la solución**. Para ello los siguientes comandos de Matlab son útiles:

   ```matlab
   surf, shading flat, axis ij, axis equal, view(2), colormap bone, colormap gray.
