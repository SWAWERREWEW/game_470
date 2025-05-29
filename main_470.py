import pygame
pygame.init()
from random import randrange, choice
from object_470 import *
from content_470 import *


while game_loop:
    clock.tick(FPS) # Это необходимо для того, чтобы синий квадратик не перемещался слишком быстро
    for event in pygame.event.get(): # Здесь обрабатываются события и единственное событие пока что
        if event.type == pygame.QUIT: # Это выход из игры
            game_loop = False
    all_sprites.update() # Загрузка всех игровых объектов в игру
    yellow_collisions = pygame.sprite.spritecollide(blue_squere, yellow_squere, True) # Проверка на то, произолшло ли столкновение
    for collision in yellow_collisions:
        score += 10 # При столкновении увеличиваются очки
        blue_squere.health = min(100, blue_squere.health + 0) # Происходит регенерация здоровья на ноль
        yellow_object = YellowSquere() # Жёлтый квадратик пересоздаётся. Обновляются координаты.
        all_sprites.add(yellow_object) # Перезагружается в игру. Жёлтый квадратик появляется, но его нельзя снова подобрать
        yellow_squere.add(yellow_object) # и обновляется сам объект, потому что иначе его нельзя будет собрать второй раз
    red_collisions = pygame.sprite.spritecollide(blue_squere, red_squeres, False) # Проверка на столкновение
    for collision in red_collisions:
        blue_squere.health -= 5 # Уходит здоровье
        if collision.rect.centerx > blue_squere.rect.centerx:
            blue_squere.rect.x -= 20 # Синего квадратика отталкивают по оси OX
        else:
            blue_squere.rect.x += 20

        if collision.rect.centery > blue_squere.rect.centery:
            blue_squere.rect.y -= 20 # отталкивают по оси OY
        else:
            blue_squere.rect.y += 20

        if blue_squere.health <= 0: # после столкновения, отнятия здоровья и отталкивания происходит
            # проверка на то, осталось ли здоровье вообще
            game_loop = False
    if score >= 470: # Победа
        print("You win! You collected 470 points!")
        game_loop = False
    screen.fill(BLACK) # Заполнение экрана чёрным цветом
    all_sprites.draw(screen) # Рисует все спрайты на экране
    pygame.draw.rect(screen, RED, (5, 5, 100, 10)) # Рисует красную полоску
    pygame.draw.rect(screen, GREEN, (5, 5, blue_squere.health, 10)) # рисует ярко зелёную полоску в зависимости от количества здоровья
    draw_text(screen, "Health", 14, 55, 15) # пишем надпись Health
    draw_text(screen, "Score: " + str(score) + " / 470", 18, WIDTH // 2, 10) # отображаем количество очков
    pygame.display.flip()
pygame.quit()
