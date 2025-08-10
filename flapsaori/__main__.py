import pygame 
from sys import exit
from random import choice,randint
from PIL import Image, ImageFilter

pygame.init()

saori_imgs = []
fogo_imgs = []

for i in range(0,3):
	imagem = pygame.image.load(f"assets/images/saori-{i+1}.png")
	imagem = pygame.transform.scale(imagem,(100,100))

	saori_imgs.append(imagem)

	imagem = pygame.image.load(f"assets/images/fogo{i+1}.png")
	imagem = pygame.transform.scale(imagem,(200,200))

	imagem.set_colorkey((55, 255, 0, 255))
	print(imagem.get_at((0,0)))

	fogo_imgs.append(imagem)



scat_img = pygame.image.load("assets/images/scat.png")
scat_img = pygame.transform.scale(scat_img,(80,80))
jp_img = pygame.image.load("assets/images/jp.png")
jp_img = pygame.transform.scale(jp_img,(100,100))
doll_img = pygame.image.load("assets/images/doll.png")
doll_img = pygame.transform.scale(doll_img,(100,100))
life_img = pygame.image.load("assets/images/life.png")
shake = pygame.mixer.Sound("assets/chocotony.mp3")
life_img = pygame.transform.scale(life_img,(30,30))
#cor = (253,223,238,0.8)
bg = Image.open("assets/images/bg.png").filter(ImageFilter.GaussianBlur(radius=10))
bg = pygame.image.fromstring(bg.tobytes(),bg.size,bg.mode)
bg = pygame.transform.scale(bg,(700,400))
tela = pygame.display.set_mode((700,400))

class Saori(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = saori_imgs[0]
		self.rect = self.image.get_rect()
		self.vidas = 3
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
		self.rect.left = randint(700,1500)
		self.rect.top = randint(50,300)

	def update(self,mocinha):
		self.rect.left -= 8
		if self.rect.left < -100 or pygame.sprite.collide_mask(self, mocinha):
			
			self.rect.left = 1000
			#shake.play()



	def colidir(self):
		self.cont = 0

class Doll(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = doll_img

class Jp(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image  = jp_img.convert_alpha()
		self.rect = self.image.get_rect()
		self.rect.left = randint(700,1500)
		self.rect.top = randint(50,300)

		

	def update(self, mocinha):
		self.rect.left -= 8

		if self.rect.left < -100:
			self.rect.left = randint(800,1800)

		elif pygame.sprite.collide_mask(self,mocinha) :
			monange = pygame.mixer.Sound("assets/monange.mp3")
			monange.play()
			self.rect.left = randint(800,1800)
			mocinha.vidas -= 1

			print(mocinha.vidas)
			return "Morreu"

	def brothersCollide(self,brothers):
		for element in brothers:
			if pygame.sprite.collide_mask(self,element):
				print("afastado")
				self.rect.left += 100
			
class Fogo(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = fogo_imgs[0]
		self.rect = self.image.get_rect()
		self.rect.left = 0
		self.rect.top = 300
		self.folha = 0

	def update(self):
		if self.folha < 3:
			self.image = fogo_imgs[self.folha]

		else:
			self.folha = 0
		self.folha += 1

grupo = pygame.sprite.Group()
saori = Saori()
fogo1 = Fogo()
fogo1.rect.left = 0
fogo2 = Fogo()
fogo2.rect.left = 200
fogo3 = Fogo()
fogo3.rect.left = 400

scat = [Scat(),Scat(),Scat(),Scat(),Scat(),Scat()]
jp = [Jp(),Jp(),Jp(),Jp()]

grupo.add(saori,fogo1,fogo2,fogo3)

#pos_x = [600,1200,1600,2180,2780,2890]
#pos_y = [300,80,150,220,390,120]
#pos1_x = [890,1390,1790,2000]
#pos2_y = [150,180,420,220]

def main():
	scat_cooldown = 1500
	jp_cooldown = 2000

	scat_lastspawn = pygame.time.get_ticks()
	jp_lastspawn = pygame.time.get_ticks()

	for element in scat:
		#element.rect.left = pos_x[scat.index(element)]
		#element.rect.top = pos_y[scat.index(element)]
		grupo.add(element)

	for element in jp:
		#element.rect.left = pos1_x[jp.index(element)]
		#element.rect.top = pos2_y[jp.index(element)]]
		element.brothersCollide(jp)
		grupo.add(element)
		
	fps = pygame.time.Clock()
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

		agora = pygame.time.get_ticks()

		for element in scat:
			element.update(saori)



			if element.rect.left < -100 and agora - scat_lastspawn > scat_cooldown:
				element.rect.left = randint(700,1500)
				element.rect.top = randint(50,300)

				scat_lastspawn = agora

		for element in jp:
			element.update(saori)
			if element.rect.left < -100 and agora - jp_lastspawn > jp_cooldown:
				element.rect.left = randint(700,1400)
				element.rect.top = randint(50,350)
				jp_lastspawn = agora

				element.brothersCollide(jp)

		
		#tela.fill(cor)
		tela.blit(bg,(0,0))
		grupo.draw(tela)

		for i in range(0,saori.vidas):
			tela.blit(life_img,(vidas[i], 0))

		if saori.vidas == -1:
			pygame.quit()
			exit()

		saori.update()
		fogo1.update()
		fogo2.update()
		fogo3.update()
		pygame.display.update()
		

if __name__ == "__main__":
	main()
