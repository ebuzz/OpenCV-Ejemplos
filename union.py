import numpy as np
import cv2

img1 = cv2.imread('/home/gatomalo/OpenCV/OpenCV/opencv-2.4.8/build/ejemplo/imagenes/nin1.jpg')
img2 = cv2.imread('/home/gatomalo/OpenCV/OpenCV/opencv-2.4.8/build/ejemplo/imagenes/nin2.jpg')

dst = cv2.addWeighted(img1,0.7,img2,0.4,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()