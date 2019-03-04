import pygame
import math
pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Testing with gravity")

size = 20
x = 20
X = 0
k = 0.1
y = 20
weight = 20
obj_vert = 2
run = True

falling =True

while run:
	distBetween = 470 - y
	pygame.time.delay(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	window.fill ((0,0,0))
	Object = pygame.draw.rect(window , (255, 0 ,0) , (x , y , size , size))
	floor = pygame.draw.rect(window , (255,250 ,250) , (0, 480 , 500 , 20)) # x , y , length , height
	pygame.display.update()

	#if not on ground
	if y < (470 - size):
		falling = True
		print (y)

	else:
		falling = False

	if falling and y < (470 - size) :
		if obj_vert < 20:
			
			obj_vert = 20 - 20*(math.exp(-k*X))
			X += 1


		y += obj_vert
	print (obj_vert)


