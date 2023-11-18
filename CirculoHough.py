# cv2 proporciona herramientas para realizar operaciones de procesamiento de imágenes
import cv2
import numpy as np

# Cargar la imagen
imagen = cv2.imread('C:/Users/marit/OneDrive/Documentos/imagenHough/motor2.jpg')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detección de bordes
bordes = cv2.Canny(gris, 50, 150, apertureSize=3)

# Transformada de Hough para círculos
circulos = cv2.HoughCircles(
    bordes,
    cv2.HOUGH_GRADIENT,
    1, 50, param1=50, param2=30, minRadius=60, maxRadius=102 
)

# Dibujar circulos en la imagen
if circulos is not None:
    circulos = np.uint16(np.around(circulos))
    for (x,y,r) in circulos[0, :]:
        # Dibujar el borde del círculo
        cv2.circle(imagen, (x, y), r, (0, 255, 0), 3)
        # Dibujar el centro del círculo
        cv2.circle(imagen, (x, y), 2, (0, 255, 255), 3)

# Mostrar la imagen
cv2.imshow('Círculos detectados', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()