import pygame as pg

pg.init()
#amores essa função ajuda a baixar imagens e sons para o gayme
def load(tipo,media,size=False):
    if tipo == 1:
        m = pg.mixer.Sound(media)

    else:
        m = pg.image.load(media)
        m = pg.transform.scale(m,size)

    return m

tamanho = (1000,600)
tela = pg.display.set_mode(tamanho)

#usando aquela função cisss
bg = load(2,'door.png',tamanho)
audio = load(1,'qual_seria.mp3')
audio.set_volume(1.0)

ygona_images = []
for i in range(1,6):
    #isso aqui vai baixar todos os sprites da diva e colocar em uma lista/array
    ygona_images.append(load(2,f'ygona{i}.png',(120,120)))

    #isso remove o fundo preto dos sprites
    ygona_images[i-1].set_colorkey((0,0,0))

chave = load(2,'key.png',(150,200))

class Chave(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = chave
        self.rect = self.image.get_rect()
        self.rect.top = 300
        self.rect.left = 400
        self.subindo = False
        self.descendo = False
    def update(self):

        if self.rect.top == 300:
            self.subindo = True

        elif self.rect.top == 200:
            self.subindo = False

        if self.subindo:
            self.rect.top -= 5
        else:
            self.rect.top += 5


#vou usar essa classe para instanciar a ygonaaa
class Trans(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)

        self.image = ygona_images[0]
        self.rect = self.image.get_rect()
        self.andando = False
        self.rect[0] = 120
        self.rect[1] = 400
        self.cont = 0
        self.direcao = 'direita'

    def andar(self):
        if self.andando:
            self.image = ygona_images[self.cont]
            if self.direcao == 'direita':
                self.rect[0] += 20
                print("Ygona to direita")
            else:
                self.rect[0] -= 20
                self.image = pg.transform.flip(self.image,True,False)
                print("Ygona to esquerda")
            if self.cont<4:
                self.cont += 1
            else:
                self.cont = 0

    def pular(self):
        self.rect[1] -= 200

    def cair(self):
        if self.rect[1] != 400:
            self.rect[1]+=10
        

#Criando o objeto da Ygona
Ygona = Trans()
sprites = pg.sprite.Group()
key = Chave()
sprites.add(Ygona,key)
clock = pg.time.Clock()

while True:
    clock.tick(30)
    for ev in pg.event.get():
        #essa parte verifica se eu soltei o botão do mouse e sai do jogo ;)
        if ev.type == quit or ev.type == pg.MOUSEBUTTONUP:
            pg.quit()

        elif ev.type == pg.KEYDOWN:
            print(ev.key)
            #tecla a = 97
            #tecla d = 100
            if ev.key == 97:
                Ygona.direcao = 'esquerda'
                Ygona.andando = True
            elif ev.key == 100:
                Ygona.direcao = 'direita'
                Ygona.andando = True

            elif ev.key == 1073741911:
                aghata.update()

            
            if ev.key == 13:
                Ygona.pular()


            print(ev.key)

        elif ev.type == pg.KEYUP:
            if ev.key == 113:
                audio.play()
            if ev.key != 13:
                Ygona.andando = False 

    tela.blit(bg,(0,0))
    sprites.draw(tela)
    Ygona.andar()
    key.update()
    Ygona.cair()
    pg.display.update()

