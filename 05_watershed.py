import cv2
import numpy as np
from matplotlib import pyplot as plt

# Leitura da imagem de entrada
img = cv2.imread('imagens/tracos.jpg')
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Converte para RGB para exibição posterior

# Aplicação de desfoque para reduzir o ruído
img_blur = cv2.medianBlur(img, 5)

# Conversão para escala de cinza
img_gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# Binarização da imagem para criar marcadores
ret, thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Identificação dos marcadores utilizando transformação morfológica de abertura
kernel = np.ones((3,3),np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

# Encontrar marcadores de fundo
sure_bg = cv2.dilate(opening, kernel, iterations=10)

# Encontrar marcadores de frente (objetos de interesse)
dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
ret, sure_fg = cv2.threshold(dist_transform, 0.1*dist_transform.max(), 255, 0)

# Encontrar região desconhecida (área onde não temos certeza)
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)

# Criação dos marcadores
ret, markers = cv2.connectedComponents(sure_fg)
markers = markers + 1
markers[unknown == 255] = 0

# Aplicação do algoritmo Watershed
markers = cv2.watershed(img_rgb, markers)
img_rgb[markers == -1] = [255,0,0]  # Marca as bordas com a cor vermelha

# Exibição dos resultados
plt.figure(figsize=(12, 8))
plt.subplot(221), plt.imshow(img_rgb)
plt.title('Imagem Original'), plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(thresh, cmap='gray')
plt.title('Imagem Binária'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(markers, cmap='viridis')
plt.title('Segmentação por Watershed'), plt.xticks([]), plt.yticks([])
plt.show()
