import numpy as np
import cv2

# Ejemplo de herramientas graficas para crear figuras en Python :D
# Realizado por Erick Aguayo - Codigo de  http://docs.opencv.org/

img = np.zeros((512,512,3), np.uint8)

print "Que quiere dibujar 1)Lineas 2)Cuadrados 3)Circulos 4)Poligonos:"
opcion = input("Ingrese opcion:")

if opcion == 1:
	cv2.line(img,(0,0),(511,200),(255,255,0),5)
elif opcion == 2:
	cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
	cv2.rectangle(img,(384,384),(510,256),(0,255,255),3)
	cv2.rectangle(img,(192,576),(384,128),(255,255,0),10)
elif opcion == 3:
	cv2.circle(img,(447,63), 63, (0,0,255), 10)
	cv2.circle(img,(200,200), 80, (255,0,255), -1)
elif opcion == 4:
	pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
	pts = pts.reshape((-1,1,2))
	cv2.polylines(img,[pts],True,(0,255,255))

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Erick',(10,500), font, 4,(255,255,255),2)

cv2.imshow('Linea',img)
print "Presione 0 para salir"
cv2.waitKey(0)
cv2.destroyAllWindows()