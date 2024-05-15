import sys
import cv2
import math
import numpy as np
import matplotlib.pyplot as plt
import time

# Função para segmentação de região por crescimento em escala de cinza
def growingRegionGray(x, y, differential):
    global image
    global image2
    global pixelsGrowing

    threshold = image[x][y]  # Limiar de intensidade inicial
    for u in pixelsGrowing:
        line = u[0]
        col = u[1]
        # Percorre uma janela ao redor do pixel (line, col)
        for a in range(-1, 2):  # Variação em linha
            for b in range(-1, 2):  # Variação em coluna
                try:
                    # Verifica se o pixel vizinho está dentro da faixa de diferença do limiar
                    if (threshold - differential <= image[line + a][col + b] <= threshold + differential):
                        if [line + a, col + b] in pixelsGrowing:
                            continue
                        else:
                            # Atualiza o pixel na imagem segmentada e na imagem visualizada
                            image2[line + a][col + b] = image[line + a][col + b]
                            image[line + a][col + b] = 1
                            pixelsGrowing.append([line + a, col + b])
                except:
                    continue
        # Atualiza a visualização da imagem em cada iteração
        cv2.imshow('Result', image2)
        cv2.waitKey(1)

# Função para segmentação de região por crescimento binário
def growingRegionBin(x, y):
    global image
    global image2
    global pixelsGrowing

    for u in pixelsGrowing:
        line = u[0]
        col = u[1]
        # Percorre uma janela ao redor do pixel (line, col)
        for a in range(-1, 2):  # Variação em linha
            for b in range(-1, 2):  # Variação em coluna
                try:
                    # Verifica se o pixel vizinho é branco (255)
                    if (image[line + a][col + b] == 255):
                        if [line + a, col + b] in pixelsGrowing:
                            continue
                        else:
                            # Atualiza o pixel na imagem segmentada e na imagem visualizada
                            image[line + a][col + b] = 1
                            pixelsGrowing.append([line + a, col + b])
                            image2[line + a][col + b] = 255

                except:
                    continue
        # Atualiza a visualização da imagem em cada iteração
        cv2.imshow('Result', image2)
        cv2.waitKey(1)

# Leitura da imagem
imgName = 'imagens/placa.png'
image = cv2.imread(imgName, 0)
image2 = image
plt.imshow(image)
plt.show()

startTime = time.time()
kernel = 3
kernelSize = kernel * kernel
kernelA = int(math.sqrt(kernelSize))
kernelB = int(kernelA)
kernelStep = -1 * int(kernelA / 2)
pixelsGrowing = []

imageSizeX, imageSizeY = image.shape

# Definição dos pontos semente (seed) para crescimento em escala de cinza
seeds = [
    [100, 150],
    [200, 150],
    [300, 150],
    [415, 150],
    [465, 150],
    [580, 150],
    [620, 150]
]

# Preenchimento das sementes na lista de pixels para crescimento
for seed in seeds:
    pixelsGrowing.append(seed)

# Criação de uma imagem em branco para a visualização do crescimento da região
image2 = np.zeros((imageSizeX, imageSizeY, 1), np.uint8)
image = cv2.imread(imgName, 0)  # Leitura da imagem original em escala de cinza

# Chamada da função de crescimento da região em escala de cinza com limiar de 25
growingRegionGray(100, 150, 25)

lapseTime = time.time() - startTime
print('Tempo decorrido: ' + str(lapseTime) + 's')

cv2.waitKey(0)
