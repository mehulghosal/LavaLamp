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
# bgfdnmyd

class Blob(pygame.sprite.Sprite):
	def __init__(self, width, height, col):#all measurements are in pixels
		self.width = width
		self.height = height
		self.col = col
		if randint(0,1) == 1: self.dirx = 1
		else: self.dirx = -1

		if randint(0,1) == 1: self.diry = 1
		else: self.diry = -1
		#self.direction = direction #tuple with two elements, -1 or 1

		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image.fill(col)
		self.rect = self.image.get_rect()

	def update(self):

		if self.rect.left <= 0: 
			self.dirx *= -1
			print("left")
		elif self.rect.right >= maxwidth: 
			self.dirx *= -1
			print("right")
		if self.rect.top <= 0: 
			self.diry *= -1
			print("top")
		elif self.rect.bottom >= maxheight: 
			self.diry *= -1
			print("bottom")
		print(self.rect.x, self.rect.y)

		self.rect.x += int(self.dirx * 1)
		self.rect.y += int(self.diry * 1)

		for sprite in spriteList:
			colideList = pygame.sprite.spritecollide(sprite, blobs, False)
			for i in colideList:
				combReturn = sprite.combine(i)
				newBlob = combReturn[0]
				newBlob.rect.x = combReturn[1]
				newBlob.rect.y = combReturn[2]
				blobs.remove(sprite, i)
				blobs.add(newBlob)


	'''def move(self):
		self.x += self.direction[0] * 5
		self.y += self.direction[1] * 5'''

	 #combines two blobs if overlap, return new blob -- figure out how to tell if they overlap
	def combine(self, another):
		area1 = self.height*self.width
		area2 = another.height*another.width


		widt = int(sqrt((area1+area2)/(2*((self.width/self.height)+(another.width/another.height)))))
		heig = (area1+area2)/widt

		colr = (int((self.col[0] + another.col[0])/2), int((self.col[1] + another.col[1])/2), int((self.col[2] + another.col[2])/2))
		nx = int((self.rect.x + self.rect.x)/2)
		ny = int((self.rect.y + self.rect.y)/2)
		direc = (self.dirx * another.dirx, self.diry * another.diry)
		b = Blob(widt, heig, colr)
		b.dirx = direc[0]
		b.diry = direc[1]
		return (b, nx, ny)

	'''
	def divide(self):
		for i in range (self.width):
			if x/i == 4:
				width = i
		for i in range (self.height):
				if x/i == 4:
					height = i
		x1, x2 = int(self.x + width*2), int(self.x - width*2)
		y1, y2 = int(self.y + height*2), int(self.y - height*2)

		return Blob(width, heigth, self.col, x1, y1, direction), Blob(width, height, self.col, x2, y2)

	def draw(self): 
		pygame.draw.ellipse(screen, self.col, Rect())'''


blobs = pygame.sprite.Group()

for i in range(1):
	#			#width 			 #height 			red					  green 		 blue
	blob = Blob(randint(50,125), randint(50, 125), (150 + randint(0,100), randint(0,50), randint(0,50)))
	blob.rect.center =(randint(blob.width,maxwidth-blob.width), randint(blob.height, maxheight-blob.height))
	blobs.add(blob)

while not done:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
	


	spriteList = blobs.sprites()


	screen.fill(white)
	blobs.draw(screen)
	blobs.update()

	clock.tick(30)
	pygame.display.flip()

