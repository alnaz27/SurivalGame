import pygame
import random

from pygame import Surface

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Выживание")
clock = pygame.time.Clock()

backround = pygame.image.load("fon.jpg")
backround = pygame.transform.scale(backround, (WIDTH, HEIGHT))
player_x, player_y = 400, 300
player_size = 30
speed = 5

player_img = pygame.image.load("igrok.png")
player_img = pygame.transform.scale(player_img, (player_size, player_size))

enemies = []
enemy_size = 25
enemy_speed = 2
spawn_delay = 0

enemy_img = pygame.image.load("vrag.png")
enemy_img = pygame.transform.scale(enemy_img, (enemy_size, enemy_size))

score = 0
font = pygame.font.Font(None, 36)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += speed
    if keys[pygame.K_UP] and player_y > 0:
        player_y -= speed
    if keys[pygame.K_DOWN] and player_y < HEIGHT - player_size:
        player_y += speed

    spawn_delay += 1
    if spawn_delay >= 60:
        spawn_delay = 0
        x = random.choice([0, WIDTH - enemy_size])
        y = random.randint(0, HEIGHT - enemy_size)
        enemies.append([x, y])

    for enemy in enemies:
        if enemy[0] < player_x:
            enemy[0] += enemy_speed
        elif enemy[0] > player_x:
            enemy[0] -= enemy_speed
        if enemy[1] < player_y:
            enemy[1] += enemy_speed
        elif enemy[1] > player_y:
            enemy[1] -= enemy_speed

    for enemy in enemies:
        if abs(player_x - enemy[0]) < player_size and abs(player_y - enemy[1]) < player_size:
            running = False


    score += 0.1

    screen.blit(backround, (0, 0))

    screen.blit(player_img,(player_x, player_y))
    for enemy in enemies:
        screen.blit(enemy_img, (enemy[0], enemy[1]))

    text = font.render(f"Счет: {int(score)}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

    author_text = font.render("Автор: Alnaz", True, (100, 100, 100))
    screen.blit(author_text, (WIDTH - 150, HEIGHT - 30))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()