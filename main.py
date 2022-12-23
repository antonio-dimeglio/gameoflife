import pygame
import numpy as np 

SIZE = (1024, 768)
SQUARE_SIZE = 6
ROWS = SIZE[0]//SQUARE_SIZE
COLS = SIZE[1]//SQUARE_SIZE



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
surface = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game of life")
surface.fill(BLACK)


def generate_grid():
    grid = np.random.randint(2, size=(ROWS+1, COLS+1))
    grid[0, 0:(COLS+1)] = 0
    grid[ROWS, 0:(COLS+1)] = 0
    grid[0:(ROWS+1), 0] = 0
    grid[0:(ROWS+1), COLS] = 0
    return grid 

def draw_grid(grid):
    surface.fill(BLACK)
    for i in range(1, ROWS):
        for j in range(1, COLS):
            if grid[i, j] == 1:
                pygame.draw.rect(surface, WHITE, pygame.Rect((i*SQUARE_SIZE, j*SQUARE_SIZE), (SQUARE_SIZE, SQUARE_SIZE)))

    pygame.display.flip()

def update_grid(grid):
    for i in range(1, ROWS):
        for j in range(1, COLS):
            total = np.sum(grid[i-1:i+2, j-1:j+2]) -1
            if grid[i, j] == 1:
                if total in [2, 3]:
                    grid[i, j] = 1
                else:
                    grid[i, j] = 0
            else:
                if total == 3:
                    grid[i, j] = 1

running = True

grid = generate_grid()
while running:
    draw_grid(grid)
    update_grid(grid)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                grid = generate_grid()