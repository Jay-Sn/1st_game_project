import pygame
import math
pygame.init()

win = pygame.display.set_mode((1000,500))

pygame.display.set_caption("Bullet_Travel")

end = False

shooting = False

time = 0

no_b = 0

b_size = 5

pos_x = 30

pos_y = 30



collision = False

while not end:
	win.fill((0,0,0))
	pygame.time.delay(20)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True

	key = pygame.key.get_pressed()

	if key[pygame.K_UP]:
		pos_y -= 4
	if key[pygame.K_DOWN]:
		pos_y += 4

	if key[pygame.K_SPACE] and not shooting :
		if no_b < 1:
			pos_y_b  = pos_y
			b_vel_x = pos_x
			shooting = True
			no_b += 1

	if shooting and no_b == 1 and time < 75 and not collision:
		bullet = pygame.draw.rect(win , (255,200,200) ,(b_vel_x , pos_y_b , b_size , b_size))
		b_vel_x += 6
		time += 0.75

	if time >= 75 or collision:
		shooting = False
		no_b = 0
		time = 0
		b_vel_x = 4

	pygame.display.update()
	
	print (isJumping)