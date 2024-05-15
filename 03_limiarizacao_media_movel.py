import cv2

def limiarizacao_media_movel(imagem, tamanho_bloco, constante):
    # Converte a imagem para escala de cinza
    img_gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    
    # Aplica a limiarização por média móvel
    imagem_limiarizada = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                               cv2.THRESH_BINARY, tamanho_bloco, constante)
    
    return imagem_limiarizada

# Carrega a imagem de entrada
imagem = cv2.imread('imagens/placa.png')

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    print("Não foi possível carregar a imagem.")
    exit()

# Define o tamanho do bloco (vizinhança) e a constante de subtração
tamanho_bloco = 11  # Tamanho da vizinhança para calcular a média (deve ser ímpar)
constante = 2       # Constante subtraída da média calculada

# Aplica a limiarização por média móvel
imagem_limiarizada = limiarizacao_media_movel(imagem, tamanho_bloco, constante)

# Mostra a imagem original e a imagem limiarizada
cv2.imshow('Imagem Original', imagem)
cv2.imshow('Imagem Limiarizada por Media Movel', imagem_limiarizada)

# Aguarda o fechamento das janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
