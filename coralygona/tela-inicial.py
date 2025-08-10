import pygame as pg
from sys import exit
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
bg = load(2,'assets/start-bg.png',tamanho)
aghat = load(2,'assets/mais-mais.png',(300,300))
ygona = load(2,'assets/Ygone.png',(300,300))

playrr = load(2,'assets/playr.png',(300,150))
class Aghata(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = aghat
        self.rect = self.image.get_rect()
        self.rect.top = 250
        self.subindo = False
        self.descendo = False
    def update(self):

        if self.rect.top == 250:
            self.subindo = True

        elif self.rect.top == 200:
            self.subindo = False

        if self.subindo:
            self.rect.top -= 5
            print("MAIS MAIS<UP>")
        else:
            self.rect.top += 5
            print("MAIS MAIS<DOWN>")

aghata = Aghata()
ygone = Aghata()
ygone.image = ygona
ygone.rect.left = 700
grupo = pg.sprite.Group()
grupo.add(aghata,ygone)
Clock = pg.time.Clock()
audio = pg.mixer.Sound("assets/rato_da_phonst.mp3")
while True:
    Clock.tick(10)
    for ev in pg.event.get():
        if ev.type == pg.QUIT:
            pg.quit()
            exit()

        elif ev.type == pg.MOUSEBUTTONDOWN:
            audio.play()

    tela.blit(bg,(0,0))
    tela.blit(playrr,(350,300))

    grupo.draw(tela)
    aghata.update()

    pg.display.update()

