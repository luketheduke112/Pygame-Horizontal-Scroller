######
#TODO: 
#	- Make sprites and characters. Maybe even a character selector or something?
#	- Implement more or less tiles falling depending on screen size.
#	- add powerups
#	- Add score counter | including a high score tracker 
#	- package up and deliever
#	-change obstacle generation, use a loop instead of just copy pasting.
#
import pygame
import random
pygame.init()
running = True
clock = pygame.time.Clock()
screenWidth = 1920
screenHeight = 1080
screen = pygame.display.set_mode([screenWidth,screenHeight])
obstaclesAreFalling = True

class Player:
	"""docstring for Player"""
	def __init__(self, rect, isAlive, level):
		self.rect = rect
		self.isAlive = isAlive
		self.level = level

	def drawPlayer(self):
		pygame.draw.rect(screen, (255,0,0),self.rect, 0, 10)
		pygame.display.update()

	def movePlayer(self):
		if pygame.key.get_pressed()[pygame.K_w] and self.rect.y > 0:
			self.rect.move_ip(0,-5)
			print("[" + str(self.rect.x) + ", " + str(self.rect.y) + "]")#just to make sure coordinates are updating.
		if pygame.key.get_pressed()[pygame.K_s] and self.rect.y < screenHeight - 50:
			self.rect.move_ip(0,5)
			print("[" + str(self.rect.x) + ", " + str(self.rect.y) + "]")
		if pygame.key.get_pressed()[pygame.K_a] and self.rect.x > 0:
			self.rect.move_ip(-5,0)
			print("[" + str(self.rect.x) + ", " + str(self.rect.y) + "]")
		if pygame.key.get_pressed()[pygame.K_d] and self.rect.x < screenWidth - 50:
			self.rect.move_ip(5,0)
			print("[" + str(self.rect.x) + ", " + str(self.rect.y) + "]")

MainCharacter = Player(pygame.Rect((screenWidth / 2) - 25, (screenHeight / 2) - 25, 50,50), True, 50)

#thinking about redesigning the structure here. Maybe it'd be better as something other than a class? Not sure, maybe I'll color code and add different properties to each different obstacle.
class Obstacle():
	"""
	obstacle class to test collisions in pygame.
	"""
	def __init__(self, rect, color,speed):
		self.rect = rect
		self.color = color
		self.speed = speed
	def draw(self):
		pygame.draw.rect(screen,self.color,self.rect)

#repetitive as hek. Need to just make this a loop. Was testing so just kinda got carried away with ctrl + c and ctrl + v
obstaclesArray = [
	Obstacle(pygame.Rect(230,screenHeight,50,50), pygame.Color(234,34,64), random.randint(4,15)),
	Obstacle(pygame.Rect(430,screenHeight,50,20), pygame.Color(23,52,47), random.randint(4,15)),
	Obstacle(pygame.Rect(20,screenHeight,80,50), pygame.Color(143,64,120), random.randint(4,15)),
	Obstacle(pygame.Rect(130,screenHeight,50,50), pygame.Color(234,34,64), random.randint(4,15)),
	Obstacle(pygame.Rect(630,screenHeight,35,40), pygame.Color(23,52,47), random.randint(4,15)),
	Obstacle(pygame.Rect(500,screenHeight,20,60), pygame.Color(143,64,120), random.randint(4,15)),
	Obstacle(pygame.Rect(230,screenHeight,50,50), pygame.Color(234,34,64), random.randint(4,15)),
	Obstacle(pygame.Rect(430,screenHeight,50,20), pygame.Color(23,52,47), random.randint(4,15)),
	Obstacle(pygame.Rect(20,screenHeight,80,50), pygame.Color(143,64,120), random.randint(4,15)),
	Obstacle(pygame.Rect(130,screenHeight,50,50), pygame.Color(234,34,64), random.randint(4,15)),
	Obstacle(pygame.Rect(630,screenHeight,35,40), pygame.Color(23,52,47), random.randint(4,15)),
	Obstacle(pygame.Rect(500,screenHeight,20,60), pygame.Color(143,64,120), random.randint(4,15)),
]
def controlObstacles(isFalling = True):
	for obstacle in obstaclesArray:
		obstacle.draw()
		if isFalling:
			obstacle.rect.move_ip(0,obstacle.speed)
		else:
			obstacle.rect.move_ip(0,0)
		if(obstacle.rect.y > screenHeight):
			obstacle.rect.y = 0-(random.randint(obstacle.rect.height,1000))
			obstacle.rect.x = random.randint(0 + obstacle.rect.width,screenWidth)
		if(MainCharacter.rect.colliderect(obstacle.rect)):
			print("collision")
			MainCharacter.isAlive = False
score = 0
font = pygame.font.Font("freesansbold.ttf", 32)


while running:
	clock.tick(60)#this is essential for smooth animation, without it the frame rate is variable, thus making your animation randomly speed up or slow down.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
	screen.fill((255,255,255))

	controlObstacles(obstaclesAreFalling)
			
	if MainCharacter.isAlive:
		score+=0.2
		scoreTextValue = "Score:" + str(round(score))
		scoreText = font.render(scoreTextValue,True, (0,0,0))
		textRect = scoreText.get_rect()
		screen.blit(scoreText,textRect)
	else:
		obstaclesAreFalling = False
		score+=0
		scoreTextValue = "GAME OVER! Your score was: " + str(round(score))
		scoreText = font.render(scoreTextValue,True, (0,0,0))
		textRect = scoreText.get_rect()
		screen.blit(scoreText,textRect)
	MainCharacter.movePlayer()
	MainCharacter.drawPlayer()
pygame.quit()
print("You died! Sorry!") #yeesh, so harsh.
