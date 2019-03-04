import pygame
import math
pygame.init()

window = pygame.display.set_mode((500,500))

pygame.display.set_caption("Testing with gravity 2")

pos_x =20
pos_y = 20
size = 20
k = 0.1
x = 0
vel_fall = 0
vel = 5

run = True

while run:
	pygame.time.delay(20)
	for event in pygame.event.get():#for quiting program
		if event.type == pygame.QUIT:
			run = False
	key = pygame.key.get_pressed()
	window.fill ((0,0,0))#avoid dublicates
	Object = pygame.draw.rect(window , (255, 0 ,0) , (pos_x , pos_y , size , size))# red object
	floor = pygame.draw.rect(window , (255,250 ,250) , (0, 480 , 500 , 20)) # x , y , length , height
	pygame.display.update()

	if pos_y < 470 - size:
		falling = True

	else:

		falling = False
		vel_fall = 0
		x = 0

	if falling:
		if vel_fall < 20:
			x += 1
			vel_fall = 30- 30 * math.exp(-k*x) #Used a exponential curve to simulate gravity

		pos_y += vel_fall
		print (pos_y)
	if key[pygame.K_LEFT] and pos_x > vel:
		pos_x -= vel
	if key[pygame.K_RIGHT] and pos_x < 500 - size - vel:
		pos_x += vel
	if key[pygame.K_UP] and not falling: #jump
		pos_y -= 20

   