import pygame
import math
pygame.init()

win = pygame.display.set_mode((1000,500))

pygame.display.set_caption("Controls")

end = False
pos_x = 30
pos_y= 30
floor_x = 0
floor_y = 470
velocity_x = 4
velocity_y = -7
size = 33
#for gravity
k = 0.1
x = 0
vel_fall = 0

isJumping = False
isFalling = True

while not end:
	overlapped = pos_y - (floor_y -size)
	pygame.time.delay(30)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			end = True

	key = pygame.key.get_pressed()
	#gravity calculation
	if isFalling and not isJumping:
		if vel_fall < 20:
			x += 1
			vel_fall = 30- 30 * math.exp(-k*x) #Used a exponential curve to simulate gravity

		pos_y += vel_fall

	#Controls
	if key[pygame.K_LEFT]:
		pos_x -= velocity_x
	if key[pygame.K_RIGHT]:
		pos_x += velocity_x

	#Jumping controls
	if key[pygame.K_SPACE] and velocity_y != 0:
		isJumping = True	
	elif key[pygame.K_SPACE] and velocity_y == 0:
		isJumping = False
		isFalling = True
	if isJumping:
		pos_y -= velocity_y**2
	if pos_y == 437 and velocity_y == 0 :
		velocity_y = -7
	if isJumping and velocity_y < 0: 
		velocity_y += 1

	#Collision
	if pos_y > floor_y - size:
		pos_y  -= overlapped
		isFalling = False
		isJumping = False

	

	if pos_y < floor_y - size and velocity_y == 0:
		isJumping = False
		isFalling = True



	win.fill((0,0,0))

	pygame.draw.rect(win , (255,0,0) , (pos_x , pos_y , size, size))
	pygame.draw.rect(win , (255,255,255), (floor_x , floor_y, 1000, 20))
	pygame.display.update()
