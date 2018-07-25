from sense_hat import SenseHat
from pygame.locals import *
import pygame
import time
# this script demonstrates how to create a class structure for gaming mode
sense = SenseHat()
sense.clear()


class stack():
	def __init__(self):
		pygame.init()
		pygame.display.set_mode((640, 480)) #640, 480 is the size of the window
		self.gaming = True

	def startGame(self):
		pygame.time.set_timer(USEREVENT +1, 800)
		x = 0	
		y = 7
		speed = 0.3
		#resets position of the light
		while self.gaming: # self.gaming is essentially a boolean, set it to false if you want to break the loop
			for event in pygame.event.get():
				if event.type == KEYDOWN:
					sense.set_pixel(x - 1, y, (0, 0, 255))
				else:
					sense.set_pixel(x, y, (0, 0, 255))
					time.sleep(speed)
					sense.set_pixel(x, y, (0, 0, 0))
					x += 1
					time.sleep(speed)
					if y == 0 and x == 8:
						y = 7
						x = 0
					elif x == 8:
						x = 0
						y -= 1

if __name__ == '__main__':
	try:
		game = stack()
		game.startGame()
	except KeyboardInterrupt:
		sense.clear()
		print "\n"
