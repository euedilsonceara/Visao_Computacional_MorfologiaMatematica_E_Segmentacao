import cv2
import numpy as np

def erosao(imagem_binaria, tamanho_kernel=(3, 3)):
    # Define o kernel (elemento estruturante) para erosão
    kernel = np.ones(tamanho_kernel, np.uint8)
    
    # Aplica a erosão na imagem binária
    imagem_erodida = cv2.erode(imagem_binaria, kernel, iterations=1)
    
    return imagem_erodida


def dilatacao(imagem_binaria, tamanho_kernel=(3, 3)):
    # Define o kernel (elemento estruturante) para dilatação
    kernel = np.ones(tamanho_kernel, np.uint8)
    
    # Aplica a dilatação na imagem binária
    imagem_dilatada = cv2.dilate(imagem_binaria, kernel, iterations=1)
    
    return imagem_dilatada


# Função principal
def main():
    # Carrega uma imagem binária (por exemplo, obtida por limiarização)
    imagem_binaria = cv2.imread('imagens/tracos.jpg', cv2.IMREAD_GRAYSCALE)
    
    # Verifica se a imagem foi carregada corretamente
    if imagem_binaria is None:
        print("Não foi possível carregar a imagem.")
        return
    
    # Aplica a erosão
    imagem_erodida = erosao(imagem_binaria, tamanho_kernel=(5, 5))
    
    # Aplica a dilatação
    imagem_dilatada = dilatacao(imagem_binaria, tamanho_kernel=(5, 5))
    
    # Mostra as imagens
    cv2.imshow('Imagem Original', imagem_binaria)
    cv2.imshow('Erosao', imagem_erodida)
    cv2.imshow('Dilatacao', imagem_dilatada)
    
    # Aguarda o fechamento das janelas
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()