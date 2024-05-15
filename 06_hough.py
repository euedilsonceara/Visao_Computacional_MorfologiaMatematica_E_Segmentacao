import cv2
import numpy as np

imagem = cv2.imread('imagens/caderno.jpg')
img = cv2.imread('imagens/caderno.jpg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray,50,120,apertureSize = 3)

lines = cv2.HoughLines(edges,1,np.pi/190,200)
#print lines
#print len(lines[0])
for i in range(len(lines)):
    for rho,theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.waitKey(1)

cv2.imshow('Imagem Original',imagem)
cv2.imshow('Linhas - Hough',img)
cv2.waitKey(0)