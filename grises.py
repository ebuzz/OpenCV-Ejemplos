import numpy as np
import cv2

img = cv2.imread('/home/gatomalo/OpenCV/OpenCV/opencv-2.4.8/build/ejemplo/imagenes/ellen.jpg',0)
cv2.imshow('Imagen gris',img)
cv2.waitKey(0)
cv2.destroyAllWindows()