import cv2
import numpy as np

# Carrega a imagem de entrada em escala de cinza
img = cv2.imread("imagens/numeros.jpg", cv2.IMREAD_GRAYSCALE)

# Verifica se a imagem foi carregada corretamente
if img is None:
    print("Não foi possível carregar a imagem.")
    exit()

# Aplica o filtro Gaussiano para suavização (Kernel 3x3 e DP calculado automaticamente)
img_gaussian = cv2.GaussianBlur(img, (3, 3), 0)

# Detecção de bordas usando o operador Sobel
img_sobelx = cv2.Sobel(img, cv2.CV_8U, 1, 0, ksize=5)
img_sobely = cv2.Sobel(img, cv2.CV_8U, 0, 1, ksize=5)
img_sobel = img_sobelx + img_sobely

# Detecção de bordas usando o operador Prewitt
kernelx = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
kernely = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
img_prewittx = cv2.filter2D(img, -1, kernelx)
img_prewitty = cv2.filter2D(img, -1, kernely)

# Mostra as imagens em janelas separadas
cv2.imshow("Imagem Original", img)
cv2.imshow("Sobel X", img_sobelx)
cv2.imshow("Sobel Y", img_sobely)
cv2.imshow("Sobel", img_sobel)
cv2.imshow("Gaussiano", img_gaussian)
cv2.imshow("Prewitt X", img_prewittx)
cv2.imshow("Prewitt Y", img_prewitty)
cv2.imshow("Prewitt", img_prewittx + img_prewitty)

# Aguarda pressionamento da tecla 'q' para fechar as janelas
while True:
    if cv2.waitKey(0) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()