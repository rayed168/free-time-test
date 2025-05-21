import pygame
import random

pygame.init()
WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)

cell_size = 20
snake = [(WIDTH // 2, HEIGHT // 2)]
direction = (cell_size, 0)
food = (random.randrange(0, WIDTH, cell_size), random.randrange(0, HEIGHT, cell_size))
score = 0
font = pygame.font.SysFont("Arial", 30)
clock = pygame.time.Clock()
running = True

def move_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    return [head] + snake[:-1]

def grow_snake(snake, direction):
    head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    return [head] + snake

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, cell_size):
                direction = (0, -cell_size)
            elif event.key == pygame.K_DOWN and direction != (0, -cell_size):
                direction = (0, cell_size)
            elif event.key == pygame.K_LEFT and direction != (cell_size, 0):
                direction = (-cell_size, 0)
            elif event.key == pygame.K_RIGHT and direction != (-cell_size, 0):
                direction = (cell_size, 0)

    next_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

    if (next_head[0] < 0 or next_head[0] >= WIDTH or
        next_head[1] < 0 or next_head[1] >= HEIGHT or
        next_head in snake):
        running = False

    if next_head == food:
        snake = grow_snake(snake, direction)
        score += 1
        while True:
            food = (random.randrange(0, WIDTH, cell_size), random.randrange(0, HEIGHT, cell_size))
            if food not in snake:
                break
    else:
        snake = move_snake(snake, direction)

    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, cell_size, cell_size))
    pygame.draw.rect(screen, RED, (*food, cell_size, cell_size))

    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(10)
pygame.quit()