import numpy as np
import cv2

img = cv2.imread('/home/gatomalo/OpenCV/OpenCV/opencv-2.4.8/build/ejemplo/imagenes/breaking.jpg')
mask = cv2.imread('/home/gatomalo/OpenCV/OpenCV/opencv-2.4.8/build/ejemplo/imagenes/paint.jpg',0)

dst = cv2.inpaint(img,mask,5,cv2.INPAINT_TELEA)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()