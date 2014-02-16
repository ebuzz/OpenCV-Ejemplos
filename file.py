from cv2.cv import *

img = LoadImage("/home/gatomalo/OpenCV/OpenCV/opencv-2.4.8/build/ejemplo/imagenes/ellen.jpg")
NamedWindow("opencv")
ShowImage("Cargando imagen",img)
WaitKey(0)
