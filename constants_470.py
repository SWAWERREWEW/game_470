import pygame
pygame.init()
from random import randrange, choice
# размеры
WIDTH = 800
HEIGHT = 600
SIZE_BLUE_SQUERE = 30
SIZE_YELOW_SQUERE = 15
SIZE_RED_SQUERE = 25

# цвета
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
LIGHT_GREEN = (124, 252, 0)


# другие параметры
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # Задание ширины и высоты экрана
pygame.display.set_caption("game 470") # задание заголовка игры
FPS = 60 # Это необходимо для того, чтобы синий квадратик не перемещался слишком быстро
clock = pygame.time.Clock() # Это необходимо для того, чтобы синий квадратик не перемещался слишком быстро
