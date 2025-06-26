import pygame, sys, random

# Initialize Pygame
pygame.init()
pygame.font.init()

# Constants
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
FPS = 10

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Setup screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()

# Font for scoreboard
font = pygame.font.SysFont(None, 36)

# Snake and food setup
snake = [(100, 100), (80, 100), (60, 100)]
direction = (CELL_SIZE, 0)
food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
        random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
score = 0

def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, CELL_SIZE, CELL_SIZE))

def draw_food(position):
    pygame.draw.rect(screen, RED, (*position, CELL_SIZE, CELL_SIZE))

def move_snake(snake, direction):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    return [new_head] + snake[:-1]

def grow_snake(snake, direction):
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    return [new_head] + snake

def check_collision(snake):
    head = snake[0]
    return (head in snake[1:] or
            head[0] < 0 or head[0] >= WIDTH or
            head[1] < 0 or head[1] >= HEIGHT)

# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                direction = (0, -CELL_SIZE)
            elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                direction = (0, CELL_SIZE)
            elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                direction = (-CELL_SIZE, 0)
            elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                direction = (CELL_SIZE, 0)

    # Check if food is eaten
    next_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if next_head == food:
        snake = grow_snake(snake, direction)
        score += 1
        food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    else:
        snake = move_snake(snake, direction)

    if check_collision(snake):
        print("Game Over! Final Score:", score)
        pygame.quit()
        sys.exit()

    screen.fill(BLACK)
    draw_snake(snake)
    draw_food(food)

    # Draw score
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(FPS)
