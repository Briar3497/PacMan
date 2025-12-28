import pygame
from constants import *
import numpy as np

pygame.init()
timer = pygame.time.Clock()
fps = 60
white = (255, 255, 255)
black = (0, 0, 0)
grey = (180, 180, 180)
dark_grey = (60, 60, 60)
red = (200, 0, 0)
orange = (255, 150, 30)
green = (50, 255, 50)
blue = (80, 80, 255)
purple = (120, 80, 200)

WIDTH = 900
HEIGHT = 520
ROW = 21
COL = 40

player_x = WIDTH / 2
player_y = HEIGHT / 3
player_speed = 0
player_direction = 0

board = []
create_new = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
active = False
score = 0
font = pygame.font.SysFont("Arial", 30)
large_font = pygame.font.SysFont("Arial", 40)

level1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1],
          [1,0,0,0,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,0,0,0,1,1,1,1,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
          [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
          [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]


def draw_board(level):
    board_squares = []
    for x in range(ROW + 1):
        for y in range(COL + 1):
            if level[x][y] == 1:
                rect = pygame.Rect(y * 22, x * 22, 23, 23)
                pygame.draw.rect(screen, white[(level[x][y]) - 1], rect, 0)
                pygame.draw.rect(screen, black, rect, 1)
                board_squares.append((rect, (x, y)))
    return board_squares

run = True
while run:
    screen.fill(grey)
    timer.tick(fps)

    board_rects_and_pos = draw_board(level1)

    pacman = pygame.draw.circle(screen, white, (ball_x, ball_y), 10)
    pygame.draw.circle(screen, black, (ball_x, ball_y), 10, 1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not active:
                active = True
                ball_y_direction = -1
                ball_x_direction = random.choice([-1, 1])
                score = 0
                create_new = True
            if event.key == pygame.K_RIGHT and active:
                player_direction = 1
            if event.key == pygame.K_LEFT and active:
                player_direction = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT and player_direction == 1:
                player_direction = 0
            if event.key == pygame.K_LEFT and player_direction == -1:
                player_direction = 0

    score_text = font.render(f'Score: {score}', True, black)
    screen.blit(score_text, (10, 475))


    pygame.display.flip()

pygame.quit()
