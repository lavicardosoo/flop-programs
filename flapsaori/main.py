import pygame 
from sys import exit
from random import choice

pygame.init()

saori_imgs = []

for i in range(0,3):
	imagem = pygame.image.load(f"saori-{i+1}")
	imagem = pygame.transform.scale(imagem,(100,100))
	saori_imgs.append(imagem)

scat_img = pygame.image.load("scat.png")
scat_img = pygame.transform.scale(scat_img,(80,80))
jp_img = pygame.image.load("jp.png")
jp_img = pygame.transform.scale(jp_img,(100,100))
doll_img = pygame.image.load("doll.png")
doll_img = pygame.transform.scale(doll_img,(100,100))
life_img = pygame.image.load("life.png")
life_img = pygame.transform.scale(life_img,(30,30))

class Saori(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = saori_imgs[0]
		self.rect = self.image.get_rect()
		self.rect.left = 20
		self.folha = 0
		self.voando = False
	def update(self):
		if self.folha < 3:
			self.image = saori_imgs[self.folha]
			if not self.voando:
				self.rect.top += 7
			else:
				self.rect.top -= 50
				self.folha = 0
				self.voando = False
		else:
			self.folha  = 0
		self.folha += 1

class Scat(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = scat_img
		self.rect = self.image.get_rect()
		self.cont = 0
	def update(self,mocinha):
		self.rect.left -= 8
		if pygame.sprite.collide_mask(self, mocinha) and self.cont == 0 :
			self.rect.left = 780
			if self.image == scat_img:
				shake = pygame.mixer.Sound("chocotony.mp3")
				shake.play()
				
			else:
				moral = pygame.mixer.Sound("doll.mp3")
				moral.play()
				self.cont += 1
				return "viveu"
			self.cont += 1

	def colidir(self):
		self.cont = 0

class Jp(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image  = jp_img
		self.rect = self.image.get_rect()
		self.cont = 0 
	def update(self, mocinha):
		self.rect.left -= 8

		if pygame.sprite.collide_mask(self,mocinha) and self.cont == 0:
			monange = pygame.mixer.Sound("monange.mp3")
			monange.play()
			
			self.cont += 1

			return "Morreu"
		
	def colidir(self):
		self.cont = 0
		
cor = (253,223,238,0.8)
tela = pygame.display.set_mode((700,400))

grupo = pygame.sprite.Group()
saori = Saori()
scat = [Scat(),Scat(),Scat(),Scat(),Scat(),Scat()]
jp = [Jp(),Jp(),Jp(),Jp()]
grupo.add(saori)

pos_x = [600,1200,1600,2180,2780,2890]
pos_y = [300,80,150,220,390,120]

pos1_x = [890,1390,1790,2000]
pos2_y = [150,180,420,220]

for element in scat:
	element.rect.left = pos_x[scat.index(element)]
	element.rect.top = pos_y[scat.index(element)]
	grupo.add(element)

scat[5].image = doll_img

for element in jp:
	element.rect.left = pos1_x[jp.index(element)]
	element.rect.top = pos2_y[jp.index(element)]
	grupo.add(element)
	
fps = pygame.time.Clock()

vida = 3
vidas = [10,40,70]
while True:
	fps.tick(30)
	for ev in pygame.event.get():
		if ev.type == pygame.QUIT:
			pygame.quit()
			exit()
		elif ev.type == pygame.KEYUP:
			if ev.key == 13:
				saori.voando = True


	tela.fill(cor)
	grupo.draw(tela)
	for element in scat:
		if element.update(saori) == "viveu":
			vida += 1

		elif element.rect.left < -100:
			element.rect.left = pos_x[scat.index(element)]
			element.rect.top = pos_y[scat.index(element)]

			element.colidir()

	for element in jp:
		if element.update(saori) == "Morreu":
			vida -= 1
		elif element.rect.left < -100:
			element.rect.left = pos_x[jp.index(element)]
			element.rect.top = pos_y[jp.index(element)]

			element.colidir()


	for i in range(0,vida):
		tela.blit(life_img,(vidas[i], 0))
	saori.update()
	pygame.display.update()
	print(vida)
