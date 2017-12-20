import sys, pygame
from colors import *
from random import *
from math import *
pygame.init()


maxwidth, maxheight = 400, 650
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((maxwidth, maxheight))
screen.fill(white)
pygame.display.flip()

class Blob(pygame.sprite.Sprite):
	def __init__(self, width, height, col):#all measurements are in pixels
		self.width = width
		self.height = height
		self.col = col
		if randint(0,1) == 1: self.dirx = randint(1, 3)
		else: self.dirx = -1*randint(1,3)

		if randint(0,1) == 1: self.diry = randint(1,3)
		else: self.diry = -1*randint(1,3)
		#self.direction = direction #tuple with two elements, -1 or 1

		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(white)
		self.rect = self.image.get_rect()

	def update(self, *args):

		if self.rect.left <= 0: 
			self.dirx *= -1
			#print("left")
		elif self.rect.right >= maxwidth: 
			self.dirx *= -1
			#print("right")
		if self.rect.top <= 0: 
			self.diry *= -1
			#print("top")
		elif self.rect.bottom >= maxheight: 
			self.diry *= -1
			#print("bottom")
		#print(self.rect.x, self.rect.y)

		if self.dirx > 3 or self.dirx<-3: self.dirx = randint(1,3)
		if self.diry > 3 or self.diry<-3: self.diry = randint(1,3)

		self.rect = self.rect.move(self.dirx, self.diry)
		#self.rect.move_ip(int(self.dirx), int(self.diry))
		#self.rect.y += int(self.diry * 1)
		'''
		letterPressed = args[0]
		if letterPressed:
			pointlist = args[1]
			blobList = args[2]

			for i in range(7):
				cenx = blobList[i].rect.center[0]
				ceny = blobList[i].rect.center[1]
				point = pointlist[i]
				if (point[0] -10 <= cenx <= point[0]+10) and (point[1] - 10 <= ceny <= point[1]+10):
					blobList[i].dirx = 0
					blobList[i].diry = 0
					#print("finished", cenx, ceny)'''
				

		colideList = pygame.sprite.spritecollide(self, blobs, False)
		for i in colideList:
			if not i is self:
				self.combine(i)

		if self.width*self.height >= 200*200:
			#print(self.width, self.height)
			self.divide()


	 #combines two blobs if overlap, return new blob -- figure out how to tell if they overlap
	def combine(self, another):
		#print(self.alive(), another.alive())
		area1 = self.height*self.width
		area2 = another.height*another.width
		#USE PYGAME RECT.INFLATE

		widt = int(sqrt((area1+area2)/(2*((self.width/another.height)+(another.width/self.height)))))
		heig = (area1+area2)/widt

		# widt = (self.width+another.width)/2
		# heig = (self.height+another.height)/2
		

		colr = (int((self.col[0] + another.col[0])/2), int((self.col[1] + another.col[1])/2), int((self.col[2] + another.col[2])/2))
		nx = int((self.rect.x + another.rect.x)/2)
		ny = int((self.rect.y + another.rect.y)/2)
		direc = (self.dirx * another.dirx, self.diry * another.diry)

		b = Blob(widt, heig, colr)
		b.dirx = direc[0]
		b.diry = direc[1]
		blobs.add(b)
		blobs.remove(self, another)
		b.rect.x = nx
		b.rect.y = ny

		'''
		if self.alive(): 
			print(self.width, self.height)
			another.kill()
			self.dirx = direc[0]
			self.diry = direc[1]
			self.rect = self.rect.inflate((self.width/another.width)+0.5, (self.height/another.height)+0.5)
			self.col = colr
			another = None
			print(self.width, self.height)

			#print(self.width, another.width, widt, self.width)
						
		else:
			print(another.width, another.height)
			self.kill()
			another.dirx = direc[0]
			another.diry = direc[1]
			another.rect = another.rect.inflate((self.width/another.width)+0.5, (self.height/another.height)+0.5)
			another.col = colr
			#print(self.width, another.width, widt, another.width)
			self = None
			print(another.width, another.height)'''


	
	def divide(self):
		self.kill()
		'''c1 = Blob(self.width/2, self.height, self.col)
								c1.rect.x = self.rect.x + self.width
								c1.rect.y = self.rect.y
								c1.dirx = 1
								c2 = Blob(self.width/2, self.height, self.col)
								c1.rect.x = self.rect.x - self.width
								c1.rect.y = self.rect.y
								c2.dirx = -1'''
		blobs.add(Blob(self.width/2, self.height, self.col))#rect = (self.rect.x+self.width, self.rect.y, self.width/2, self.height)
		blobs.add(Blob(self.width/2, self.height, self.col))#rect = (self.rect.x-self.width, self.rect.y, self.width/2,self.height)
		

def A(blobList):
	points = [(170,160),(230,160),(100,325),(200,325),(300,325),(50,500), (340,500)]
	for i in range(len(blobList)):
		blobList[i].dirx = copysign(1, points[i][0] - blobList[i].rect.center[0]) *randint(1,3)
		blobList[i].diry = copysign(1, points[i][1] - blobList[i].rect.center[1]) *randint(1,3)
	return points

def B(blobList):
	points = [(200,70),(100,170),(300,170),(175,240),(75,310),(300,310),(200,400)]
	for i in range(len(blobList)):
		blobList[i].dirx = copysign(1, points[i][0] - blobList[i].rect.center[0]) *randint(1,3)
		blobList[i].diry = copysign(1, points[i][1] - blobList[i].rect.center[1]) *randint(1,3)
	return points

def C(blobList):
	points = [(340,116), (270,80),(130,180),(60,325),(130, 470), (270,580), (340, 530)]
	for i in range(len(blobList)):
		blobList[i].dirx = copysign(1, points[i][0] - blobList[i].rect.center[0]) *randint(1,3)
		blobList[i].diry = copysign(1, points[i][1] - blobList[i].rect.center[1]) *randint(1,3)
	return points

blobs = pygame.sprite.Group()

for i in range(5):
	#			#width 			 #height 			red					  green 		 blue
	blob = Blob(randint(80,130), randint(125, 175), (150 + randint(0,100), randint(0,50), randint(0,50)))
	print(blob)
	blob.rect.center = (randint(blob.width,maxwidth-blob.width), randint(blob.height, maxheight-blob.height))
	blobs.add(blob)

spriteList = blobs.sprites()

#while not done:
for i in range(30):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			#done = True
			break

	
	letter = False
	pointlist = [None for i in range(7)]
	'''
	pressed = pygame.key.get_pressed()
	if pressed[pygame.K_a]: 
		char = "A"
		letter = True
		pointlist = A(spriteList)
	elif pressed[pygame.K_b]: 
		char = "B"
		letter = True
		pointlist = B(spriteList)
	elif pressed[pygame.K_c]: 
		char = "C"
		letter = True
		pointlist = C(spriteList)
	elif pressed[pygame.K_SPACE]:
		for i in spriteList:
			if randint(0,1) == 1: i.dirx = randint(1, 3)
			else: i.dirx = -1*randint(1,3)

			if randint(0,1) == 1: i.diry = randint(1,3)
			else: i.diry = -1*randint(1,3)
	'''
	screen.fill(white)
	blobs.update(letter, pointlist, spriteList)
	blobs.draw(screen)
	spriteList = blobs.sprites()

	for sprite in spriteList:
		pygame.draw.ellipse(screen, sprite.col, sprite.rect, 0)
	pygame.display.flip()

	clock.tick(10)

