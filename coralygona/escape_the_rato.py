import pygame as pg
#Serve para carregar as imagens do jogo
from pygame.image import load
#Redefine o tamanho da imagem e inverte a imagem
from pygame.transform import scale, flip
from PIL import Image, ImageOps
from random import choice,randint

pg.init()

#Define uma janela para o jogo
TAMANHO = (1000,600)
TELA = pg.display.set_mode(TAMANHO)

#Carrega a imagem dentro da função scale(Imagem, Tamanho)
BACKGROUND = scale(load("assets/background.png"),TAMANHO)
RATO_IMAGE = scale(load("assets/rato.png"),(350,150))
RATO_GRITO = pg.mixer.Sound("assets/rat.mp3")
RATO_RAIVA = scale(load("assets/angry-rato.png"),(350,150))
VIDA_YGONA =  scale(load("assets/Ygone.png"),(50,50))
VIDA_RATO =scale(load("assets/rato.png"),(100,50))
RATO_NORMAL = RATO_IMAGE
TA_DOENDO = pg.mixer.Sound("assets/ta_doendo.mp3")
SOUNDTRACK = pg.mixer.Sound("assets/b.mp3")
RATO_GRITO.set_volume(1.2)
YGONA_IMAGES = []

def escapeTheRato():
    IMAGE1 = scale(load("assets/ygona1.png"),(150,150))
    IMAGE1.set_colorkey((0,0,0))

    TOPRECT = pg.Rect(0,0,TAMANHO[0],400)
    VULNERABILIDADE = pg.USEREVENT + 1
    YGONEVULNERAVEL_IMAGES = [IMAGE1,scale(load("assets/ygona-vul.png"),(150,150))]

    #Armazena as imagens da ygona dentro da lista YGONA_IMAGES[]
    for i in range(1,6):
        imagem = scale(load(f"assets/ygona{i}.png"),(150,150))
        imagem.set_colorkey((0,0,0))
        YGONA_IMAGES.append(imagem)
    #Classe que irá dá vida a ygona
    class Trans(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.image = YGONA_IMAGES[1]
            self.rect = self.image.get_rect()
            self.rect.left = 500
            self.rect.top = 400
            self.andandoParaFrente = False
            self.andandoParaTras = False
            self.peso = 20
            self.velocidade = 20
            self.pulando = True 
            self.folha = 0
            self.folha_vul = 0
            self.vidas = 3
            self.vulneravel = True
        def update(self):
            print(self.vulneravel)
            self.folha += 1
            self.folha_vul += 1
            if self.folha_vul > 1:
                self.folha_vul = 0

            if not self.vulneravel:
                self.image = YGONEVULNERAVEL_IMAGES[self.folha_vul]

            if self.folha > 3:
                self.folha = 0
            if self.andandoParaFrente:
                self.image = YGONA_IMAGES[self.folha]
                if self.rect.left < 900:
                    self.rect.left += self.velocidade
            elif self.andandoParaTras:
                self.image = YGONA_IMAGES[self.folha]
                self.image = flip(self.image, True, False)
                if self.rect.left > 0:
                    self.rect.left -= self.velocidade
            if self.rect.top < 400:
                self.rect.top += self.peso

                #print(ygona.vulneravel)

        def testarColisoes(self,enemie):
            if self.vulneravel:
                """if self.rect.colliderect(enemie.rectColuna):
                    self.rect.top -= 150
                    RATO_GRITO.play()"""
                if self.rect.colliderect(enemie.rectNariz):
                    self.vidas -= 1
                    self.vulneravel = False
                    #print("Ygona foi atingida")
                    TA_DOENDO.play()
                    YGONA_IMAGES[0] = YGONEVULNERAVEL_IMAGES[1]
                    pg.time.set_timer(VULNERABILIDADE,3000)


    class Rato(pg.sprite.Sprite):
        def __init__(self):
            pg.sprite.Sprite.__init__(self)
            self.image = RATO_IMAGE
            self.rect = self.image.get_rect()
            self.rectColuna = self.image.get_rect()
            self.rectNariz = self.image.get_rect()
            self.rect.left = -599
            self.rect.top = 400
            self.rect.width = 350
            self.rect.height = 150
            self.ratoIndo = False
            self.ratoVoltando = True
            self.vulneravel = True
            self.velocidade = 40
            self.vida = 10
            self.folha = 0

        def update(self):
            self.rectNariz.height = 50
            self.rectNariz.width = 50
            self.rectColuna.height = 20
            self.rectColuna.width = 150

            self.folha += 1

            if self.folha > 3:
                self.folha = 0

            self.rectColuna.top = self.rect.top + 30
            self.rectNariz.top = self.rect.top  + 50
            #print(self.rect.left)
            if self.rect.left in list(range(1200,1300,1)):
                self.image = flip(self.image,True,False)
                self.ratoVoltando = True
                self.ratoIndo = False
            elif self.rect.left in list(range(-400,-600,-1)):
                self.image = RATO_IMAGE
                if not self.vulneravel:
                    self.image = RATO_RAIVA
                self.ratoIndo = True
                self.ratoVoltando = False
            if self.ratoVoltando:
                self.rect.left -= self.velocidade
                self.rectColuna.left = self.rect.left + 100
                self.rectNariz.left = self.rect.left + 50
            else:
                self.rect.left += self.velocidade
                self.rectColuna.left = self.rect.left + 100
                self.rectNariz.left = self.rect.left + 230


        def testarColisao(self,y):
            if y.vulneravel and self.vulneravel:
                if self.rectColuna.colliderect(y.rect):
                    pg.time.set_timer(VULNERABILIDADE,5000)
                    self.image = RATO_RAIVA
                    self.vida -= 1
                    y.rect.top -= 150
                    self.velocidade = 70
                    RATO_GRITO.play()
                    self.vulneravel = False
    ygona = Trans()
    ratinhocis = Rato()
    grupo = pg.sprite.Group()
    relogio = pg.time.Clock()

    grupo.add(ygona,ratinhocis)

    SOUNDTRACK.play()
    resultado = "Viveu"
    #Loop principal
    while True:
        relogio.tick(30)
        #Verifica os eventos do jogo
        for evento in pg.event.get():

            teclas = pg.key.get_pressed()

            if teclas[pg.K_d]:
                ygona.andandoParaFrente = True
            else:
                ygona.andandoParaFrente = False

            if teclas[pg.K_a]:
                ygona.andandoParaTras = True
            else:
                ygona.andandoParaTras = False

            if teclas[pg.K_SPACE]:
                if not TOPRECT.colliderect(ygona.rect):
                    ygona.rect.top -= 300

            if evento.type == pg.QUIT:
                pg.quit()
                break

            """elif evento.type == pg.KEYDOWN:

                #Ao clicar na tecla D a Ygona anda para frente
                if evento.key == 100:
                    ygona.andandoParaFrente = True

                #Ao clicar na tecla A a Ygona anda para trás
                elif evento.key == 97:
                    ygona.andandoParaTras = True

                #Ao clicar na tecla ESPAÇO a Ygona dá um pulo cis
                elif evento.key == 32:
                    if not TOPRECT.colliderect(ygona.rect):
                        ygona.rect.top -= 300

            elif evento.type == pg.KEYUP:
                ygona.andandoParaFrente = False
                ygona.andandoParaTras = False
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if not TOPRECT.colliderect(ygona.rect):
                    ygona.rect.top -= 300"""
            
            if evento.type == VULNERABILIDADE:

                if not ygona.vulneravel:
                    ygona.vulneravel = True
                    YGONA_IMAGES[0] = IMAGE1
                if not ratinhocis.vulneravel:
                    ratinhocis.vulneravel = True
                    ratinhocis.velocidade = 40
                    ratinhocis.image = RATO_IMAGE


        pg.draw.rect(TELA,(0,0,0),TOPRECT)
        TELA.blit(BACKGROUND,(0,0))
        for i in range(0,ygona.vidas):
            TELA.blit(VIDA_YGONA,(70 * i,0))

        for i in range(0,ratinhocis.vida):
            TELA.blit(VIDA_RATO,(i* 70, 100))
        grupo.draw(TELA)
        #pg.draw.rect(TELA,(0,0,0),ratinhocis.rectNariz)
        ygona.update()
        ygona.testarColisoes(ratinhocis)
        ratinhocis.update()
        ratinhocis.testarColisao(ygona)
        pg.display.update()

        if ygona.vidas == 0:
            resultado = "Morreu"
            break
        elif ratinhocis.vida == 0:
            resultado = "Viveu"
            break

    SOUNDTRACK.stop()
    TA_DOENDO.stop()
    RATO_GRITO.stop()
    return resultado
