import pygame as pg
#Serve para carregar as imagens do jogo
from pygame.image import load
#Redefine o tamanho da imagem e inverte a imagem
from pygame.transform import scale, flip

pg.init()

TAMANHO = (1000,600)
#Define uma janela para o jogo
TELA = pg.display.set_mode(TAMANHO)
#Carrega a imagem dentro da função scale(Imagem, Tamanho)
BACKGROUND = scale(load("assets/background.png"),TAMANHO)

ygona_images = []
rato_image = scale(load("assets/rato.png"),(100,100))

#Armazena as imagens da ygona dentro da lista ygona_images[]
for i in range(1,6):
    imagem = scale(load(f"assets/ygona{i}.png"),(200,200))
    imagem.set_colorkey((0,0,0))
    ygona_images.append(imagem)

#Classe que irá dá vida a ygona
class Trans(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = ygona_images[0]
        self.rect = self.image.get_rect()
        self.rect.left = 0
        self.rect.top = 400
        self.folha = 0

    """def update(self):
        self.image = ygona_images[self.folha]
        self.folha += 1
        print(self.folha)
        if self.folha > 3:
            self.folha = 0"""


ygona = Trans()
grupo = pg.sprite.Group()
grupo.add(ygona)

#Loop principal
while True:

    #Verifica os eventos do jogo
    for evento in pg.event.get():
        if evento.type == pg.QUIT:
            pg.quit()
            break

    TELA.blit(BACKGROUND,(0,0))
    grupo.draw(TELA)
    """ygona.update()"""
    pg.display.update()