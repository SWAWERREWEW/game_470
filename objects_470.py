import pygame
pygame.init()
from random import randrange, choice
from content_470 import *

# Класс для задания характеристик синего квадратика или игрока
class BlueSquere(pygame.sprite.Sprite):
    def __init__(self): # Конструктор класса
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([SIZE_BLUE_SQUERE, SIZE_BLUE_SQUERE]) # задание размером синему квадратику
        self.image.fill(BLUE) # заполняем квадратик синим цветом
        self.rect = self.image.get_rect() # создание возможности фиксировать перемещение
        self.rect.center = (WIDTH // 2, HEIGHT // 2) # В начале игры квадратик появится в центре экрана
        self.speed = 3 # значение скорости
        self.health = 100 # здоровье
    # Функция update позволяет менять координаты синего квадратика для перемещения
    def update(self):
        x = 0 # координаты перемещения, которые меняются после нажатия клавиши
        y = 0 # и прибавляются к координатам местоположения синего квадратика
        keys = pygame.key.get_pressed() # Фиксирует нажатия клавиш. В эту переменную передаётся информация о том, нажата ли в какойто момент клавиша
        if keys[pygame.K_LEFT]:
            x = -self.speed # координата меняется в 
        if keys[pygame.K_RIGHT]:
            x = self.speed
        if keys[pygame.K_UP]:
            y = -self.speed
        if keys[pygame.K_DOWN]:
            y = self.speed
        self.rect.x += x
        self.rect.y += y
        # Дальше условия не позволяют выйти за пределы экрана
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

# Класс жёлтого квадратика
class YellowSquere(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([SIZE_YELOW_SQUERE, SIZE_YELOW_SQUERE])
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, WIDTH - SIZE_YELOW_SQUERE) # Заданиие случайных координат
        self.rect.y = randrange(0, HEIGHT - SIZE_YELOW_SQUERE)


class RedSquere(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([SIZE_RED_SQUERE, SIZE_RED_SQUERE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = randrange(0, WIDTH - SIZE_RED_SQUERE)
        self.rect.y = randrange(0, HEIGHT - SIZE_RED_SQUERE)
        self.x = choice([-2, 2]) # задаётся перемещение в случайную сторону
        self.y = choice([-2, 2])


    def update(self):
        self.rect.x += self.x
        self.rect.y += self.y
        if self.rect.left < 0 or self.rect.right > WIDTH:
            self.x = -self.x
        if self.rect.top < 0 or self.rect.bottom > HEIGHT:
            self.y = -self.y


def draw_text(surface, text, size, x, y, color=WHITE):
    font = pygame.font.SysFont("serif", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)


all_sprites = pygame.sprite.Group()
yellow_squere = pygame.sprite.Group()
red_squeres = pygame.sprite.Group()
blue_squere = BlueSquere()
all_sprites.add(blue_squere)


yellow_count = 5
for i in range(yellow_count):
    yellow_object = YellowSquere()
    all_sprites.add(yellow_object)
    yellow_squere.add(yellow_object)


red_count = 20
for i in range(red_count):
    red_object = RedSquere()
    all_sprites.add(red_object)
    red_squeres.add(red_object)


score = 0
game_loop = True
