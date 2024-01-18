import pygame
import sys
import random

pygame.init()

# Constants
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Initialize Pygame
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Snake initialization
snake = [(100, 100), (90, 100), (80, 100)]
snake_direction = (GRID_SIZE, 0)

# Food initialization
food = (random.randrange(1, WIDTH // GRID_SIZE) * GRID_SIZE,
        random.randrange(1, HEIGHT // GRID_SIZE) * GRID_SIZE)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_direction != (0, GRID_SIZE):
        snake_direction = (0, -GRID_SIZE)
    elif keys[pygame.K_DOWN] and snake_direction != (0, -GRID_SIZE):
        snake_direction = (0, GRID_SIZE)
    elif keys[pygame.K_LEFT] and snake_direction != (GRID_SIZE, 0):
        snake_direction = (-GRID_SIZE, 0)
    elif keys[pygame.K_RIGHT] and snake_direction != (-GRID_SIZE, 0):
        snake_direction = (GRID_SIZE, 0)

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    # Check for collision with food
    if snake[0] == food:
        snake.append(snake[-1])  # Grow the snake
        food = (random.randrange(1, WIDTH // GRID_SIZE) * GRID_SIZE,
                random.randrange(1, HEIGHT // GRID_SIZE) * GRID_SIZE)

    # Check for collision with walls or itself
    if (snake[0][0] < 0 or snake[0][0] >= WIDTH or
            snake[0][1] < 0 or snake[0][1] >= HEIGHT or
            snake[0] in snake[1:]):
        pygame.quit()
        sys.exit()

    # Draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (food[0], food[1], GRID_SIZE, GRID_SIZE))

    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    pygame.display.flip()
    clock.tick(FPS)
