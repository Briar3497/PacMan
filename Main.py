import pygame
from constants import *
from level1 import boardlvl1
import math

pygame.init()
screen = pygame.display.set_mode(SCREENSIZE)
timer = pygame.time.Clock()
fps = 60
PI = math.pi

player_x = SCREENWIDTH / 2
player_y = SCREENHEIGHT / 3
player_speed = 0
player_direction = 0

create_new = True
active = False
score = 0
font = pygame.font.SysFont('PressStart2P-Regular.ttf', 30)
large_font = pygame.font.SysFont("Arial", 40)


def draw_board(level):
    board_squares = []
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, WHITE, (j * TILEWIDTH + (0.5 * TILEWIDTH), i * TILEHEIGHT + (0.5 * TILEWIDTH)), 4)
            if level[i][j] == 2:
                pygame.draw.circle(screen, WHITE, (j * TILEWIDTH + (0.5 * TILEWIDTH), i * TILEHEIGHT + (0.5 * TILEWIDTH)), 10)
            if level[i][j] == 3:
                pygame.draw.line(screen, BLUE, (j * TILEWIDTH + (0.5 * TILEWIDTH), i * TILEHEIGHT),
                                 (j * TILEWIDTH + (0.5 * TILEWIDTH), i * TILEHEIGHT + TILEHEIGHT), 3)
            if level[i][j] == 4:
                pygame.draw.line(screen, BLUE, (j * TILEWIDTH, i * TILEHEIGHT + (0.5 * TILEHEIGHT)),
                                 (j * TILEWIDTH + TILEWIDTH, i * TILEHEIGHT + (0.5 * TILEHEIGHT)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, BLUE, [(j * TILEWIDTH - (TILEWIDTH * 0.4)) - 2, (i * TILEHEIGHT + (0.5 * TILEHEIGHT)), TILEWIDTH, TILEHEIGHT], 0, PI / 2, 3)
            if level[i][j] == 6:
                pygame.draw.arc(screen, BLUE,
                                [(j * TILEWIDTH + (TILEWIDTH * 0.5)), (i * TILEHEIGHT + (0.5 * TILEHEIGHT)), TILEWIDTH, TILEHEIGHT], PI / 2, PI,  3)
            if level[i][j] == 7:
                pygame.draw.arc(screen, BLUE,
                                [(j * TILEWIDTH + (TILEWIDTH * 0.5)), (i * TILEHEIGHT - (0.4 * TILEHEIGHT)),
                                 TILEWIDTH, TILEHEIGHT], PI, 3 + PI / 2, 3)
            if level[i][j] == 8:
                pygame.draw.arc(screen, BLUE,
                                [(j * TILEWIDTH - (TILEWIDTH * 0.4)) - 1, (i * TILEHEIGHT - (0.5 * TILEHEIGHT)),
                                 TILEWIDTH, TILEHEIGHT], 3 * PI / 2, 2 * PI, 3)
            if level[i][j] == 9:
                pygame.draw.line(screen, WHITE, (j * TILEWIDTH, i * TILEHEIGHT + (0.5 * TILEHEIGHT)),
                                 (j * TILEWIDTH + TILEWIDTH, i * TILEHEIGHT + (0.5 * TILEHEIGHT)), 3)

    return board_squares

run = True
while run:
    screen.fill(BLACK)
    timer.tick(fps)

    board_rects_and_pos = draw_board(boardlvl1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (SCREENWIDTH * 0.03, SCREENHEIGHT * 0.92))


    pygame.display.flip()

pygame.quit()
