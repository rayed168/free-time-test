import pygame
import random

pygame.init()
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Square!")
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 5
square_size = 30
square_x = random.randint(0, WIDTH - square_size)
square_y = 0
square_speed = 3
score = 0
font = pygame.font.SysFont(None, 36)
clock = pygame.time.Clock()
running = True

while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    square_y += square_speed
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)
    square_rect = pygame.Rect(square_x, square_y, square_size, square_size)
    if player_rect.colliderect(square_rect):
        score += 1
        square_x = random.randint(0, WIDTH - square_size)
        square_y = 0
    if square_y > HEIGHT:
        square_x = random.randint(0, WIDTH - square_size)
        square_y = 0
    pygame.draw.rect(screen, BLUE, player_rect)
    pygame.draw.rect(screen, RED, square_rect)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
