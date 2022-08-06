import pygame
import requests
from utility import button
from sudoku_game_solver import solve
pygame.init()

width=880
white=(218,210,216)
blue=(20,54,66)
gold=(201,169,89)
font=pygame.font.SysFont("Times", 50)
screen = pygame.display.set_mode((width,width))
check_button = button(white,100,815,120,50,'Check')

def draw_grid(screen):
    for co in range(10):
        width = 4 if co%3 == 0 else 1
        pygame.draw.line(screen,white,(80+80*co,80),(80+80*co,800),width)
        pygame.draw.line(screen,white,(80,80+80*co),(800,80+80*co),width)

def get_list():
    global original_grid 
    global grid 

    board = requests.get("https://sugoku.herokuapp.com/board?difficulty=easy")
    grid = board.json()['board']
    original_grid = [[grid[x][y] for y in range(len(grid[0]))] for x in range(len(grid))]
    build_grid(grid)

def build_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            if(0<grid[x][y]<10):
                value = font.render(str(grid[x][y]), True, gold)
                screen.blit(value, ((y+1)*80 + 30, (x+1)*80+14))

def click(position):
    x = position[1]
    y = position[0]
    wrap = 10

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if(original_grid[x-1][y-1] != 0):
                    return
                if(event.key == 48):
                    grid[x-1][y-1] = event.key - 48
                    pygame.draw.rect(screen, blue, (position[0]*80 + wrap, position[1]*80+ wrap, 80 - 2*wrap, 80 - 2*wrap))
                    pygame.display.update()
                    return
                if(0 < event.key - 48 <10):
                    pygame.draw.rect(screen, blue, (position[0]*80 + wrap, position[1]*80+ wrap,80 -2*wrap , 80 - 2*wrap))
                    value = font.render(str(event.key-48), True, white)
                    screen.blit(value, (position[0]*80 + 30, position[1]*80+14))
                    grid[x-1][y-1] = event.key - 48
                    pygame.display.update()
                    return
                return

def main():
    pygame.display.set_caption('Sudoku')
    pygame.display.set_icon(pygame.image.load('pastime.png'))
    screen.fill(blue)
    draw_grid(screen)
    get_list()
    isCorrect = font.render('Correct', True, white, gold)
    isIncorrect = font.render('Incorrect', True, white, gold)
    cor = isCorrect.get_rect()
    incor = isCorrect.get_rect()


    while True:
        check_button.draw(screen, white)
        pygame.display.update()
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                click((pos[0]//80, pos[1]//80))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if check_button.isOver(pos):
                    if solve(original_grid)==grid:
                        screen.blit(isCorrect, cor)
                    else:
                        screen.blit(isIncorrect, incor)

            if event.type == pygame.MOUSEMOTION:
                if check_button.isOver(pos):
                    check_button.color=gold
                else:
                    check_button.color=blue

main()