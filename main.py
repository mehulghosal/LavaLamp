import sys, pygame
from colors import *
from math import *

pygame.init()


maxwidth, maxheight = 600, 600
done = False
clock = pygame.time.Clock()
screen = pygame.display.set_mode((maxwidth, maxwidth))
screen.fill(white)
pygame.display.flip()
# bgfdnmyd

class Blob(object):
	def __init__(self, width, height, col, x, y, direction):#all measurements are in pixels
		self.width = width
		self.height = height
		self.col = col
		self.x = x
		self.y = y
		self.direction = direction #tuple with two elements, 0 or 1

	def move(self):
		self.x += self.direction[0] * 5
		self.y += self.direction[1] * 5

	 #combines two blobs if overlap, return new blob -- figure out how to tell if they overlap
	def combine(self, another):
		widt = int((self.width + another.width)/2)
		heig = int((self.height + another.height)/2)
		colr = (int((self.col[0] + antother.col[0])/2), int((self.col[1] + antother.col[1])/2), int((self.col[2] + antother.col[2])/2))
		nx = int((self.x + self.x)/2)
		ny = int((self.y + self.y)/2)
		direc = (self.direction[0] * another.direction[0], self.direction[1] * another.direction[1])
		return Blob(widt, heig, colr, nx, ny, direc)

	def divide(self):
		width = self.width/2
		height = self.height/2
		x1, x2 = int(self.x + self.width/2), int(self.x - self.width/2)
		y1, y2 = int(self.y + self.height/2), int(self.y - self.height/2)

		return Blob(width, heigth, self.col, x1, y1, direction), Blob(width, height, self.col, x2, y2)