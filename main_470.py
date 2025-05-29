import pygame
pygame.init()
from random import randrange, choice
from object_470 import *
from content_470 import *


while game_loop:
    # Это необходимо для того, чтобы синий квадратик не перемещался слишком быстро
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
    all_sprites.update()
    yellow_collisions = pygame.sprite.spritecollide(blue_squere, yellow_squere, True)
    for collision in yellow_collisions:
        score += 10
        blue_squere.health = min(100, blue_squere.health + 0)
        yellow_object = YellowSquere()
        all_sprites.add(yellow_object)
        yellow_squere.add(yellow_object)
    red_collisions = pygame.sprite.spritecollide(blue_squere, red_squeres, False)
    for collision in red_collisions:
        blue_squere.health -= 5
        if collision.rect.centerx > blue_squere.rect.centerx:
            blue_squere.rect.x -= 20
        else:
            blue_squere.rect.x += 20

        if collision.rect.centery > blue_squere.rect.centery:
            blue_squere.rect.y -= 20
        else:
            blue_squere.rect.y += 20

        if blue_squere.health <= 0:
            game_loop = False
    if score >= 470:
        print("You win! You collected 470 points!")
        game_loop = False
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.draw.rect(screen, RED, (5, 5, 100, 10))
    pygame.draw.rect(screen, GREEN, (5, 5, blue_squere.health, 10))
    draw_text(screen, "Health", 14, 55, 15)
    draw_text(screen, "Score: " + str(score) + " / 470", 18, WIDTH // 2, 10)
    pygame.display.flip()
pygame.quit()
