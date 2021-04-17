import pygame
pygame.init()
from pygame import Rect
size = width, height = 300, 375
black = 0, 0, 0
white = 255, 255, 255
gray = 128, 128, 128
red = 255, 0, 0
font = pygame.font.SysFont(pygame.font.get_default_font(), 50)
finished = False
winner = 0
screen = pygame.display.set_mode(size)
screen.fill(white)

pygame.display.update()
def resetpos():
    global positions
    positions = [[[(50, 50), 0, Rect(0, 0, 100, 100)], [(150, 50), 0, Rect(100, 0, 100, 100)], [(250, 50), 0, Rect(200, 0, 100, 100)]],\
                 [[(50, 150), 0, Rect(0, 100, 100, 100)], [(150, 150), 0, Rect(100, 100, 100, 100)], [(250, 150), 0, Rect(200, 100, 100, 100)]],\
                 [[(50, 250), 0, Rect(0, 200, 100, 100)], [(150, 250), 0, Rect(100, 200, 100, 100)], [(250, 250), 0, Rect(200, 200, 100, 100)]]]
    #Each position is it's own list for coordinates and status
    #To call a cell go (positions[row])[column] or use callcell function
    #The 0 at the end of each list indicates whether it is:
    #0: Empty, 1: A X, 2: A O
positions = [[[(50, 50), 0, Rect(0, 0, 100, 100)], [(150, 50), 0, Rect(100, 0, 100, 100)], [(250, 50), 0, Rect(200, 0, 100, 100)]],\
            [[(50, 150), 0, Rect(0, 100, 100, 100)], [(150, 150), 0, Rect(100, 100, 100, 100)], [(250, 150), 0, Rect(200, 100, 100, 100)]],\
            [[(50, 250), 0, Rect(0, 200, 100, 100)], [(150, 250), 0, Rect(100, 200, 100, 100)], [(250, 250), 0, Rect(200, 200, 100, 100)]]]
waystowin = [[(0, 0), (0, 1), (0, 2)], [(1, 0), (1, 1), (1, 2)], [(2, 0), (2, 1), (2, 2)],\
             [(0, 0), (1, 0), (2, 0)], [(0, 1), (1, 1), (2, 1)], [(0, 2), (1, 2), (2, 2)],\
             [(0, 0), (1, 1), (2, 2)], [(2, 0), (1, 1), (0, 2)]]

def callcell(x, y):
    global positions
    return (positions[y])[x]

def changestatus(x, y, status):
    global positions
    ((positions[y])[x])[1] = status
def drawcircle(pos):
    global screen
    global black
    pygame.draw.circle(screen, black, pos, 50, 5)
def drawx(pos):
    global screen
    global black
    x = pos[0]
    y = pos[1]
    pygame.draw.line(screen, black, (x+50, y+50), (x-50, y-50), 5)
    pygame.draw.line(screen, black, (x+50, y-50), (x-50, y+50), 5)

def grid():
    global screen
    global black
    pygame.draw.line(screen, black, (100, 0), (100, 300), 5)
    pygame.draw.line(screen, black, (200, 0), (200, 300), 5)
    pygame.draw.line(screen, black, (0, 100), (300, 100), 5)
    pygame.draw.line(screen, black, (0, 200), (300, 200), 5)
def screenfill():
    global white
    screen.fill(white)
def threeinarow():
    global positions
    global waystowin
    global red
    global finished
    global winner
    for i in waystowin:
        c1 = i[0]
        c2 = i[1]
        c3 = i[2]
        c1 = callcell(c1[0], c1[1])
        c2 = callcell(c2[0], c2[1])
        c3 = callcell(c3[0], c3[1])
        if c1[1] == c2[1] and c1[1] == c3[1] and c3[1] == c2[1] and c1[1]!= 0:
            pygame.draw.line(screen, red, c1[0], c3[0], 10)
            finished = True
            winner = c1[1]
def updatescreenonpos():
    global positions
    global white
    global screen
    global font
    global current
    global gray
    global finished
    global winner
    tie = True
    screenfill()
    if current == 1:
        bottom = "X's turn"
    else:
        bottom = "O's turn"
    rect = font.render(bottom, 1, black)
    screen.blit(rect, (0, 310))
    for row in positions:
        for cell in row:
            if cell[1] == 1:
                drawx(cell[0])
            elif cell[1] == 2:
                drawcircle(cell[0])
            else:
                tie = False
                mouse = pygame.mouse.get_pos()
                if cell[2].collidepoint(mouse):
                    pygame.draw.rect(screen, gray, cell[2])
                    if pygame.mouse.get_pressed() != (0, 0, 0):
                        cell[1] = current
                        if current == 1:
                            drawx(cell[0])
                            current = 2
                        else:
                            current = 1
                            drawcircle(cell[0])
    grid()
    threeinarow()
    pygame.display.update()
    if tie == True:
        finished = True
        winner = 0
    if finished == True:
        if winner == 1:
            bottom = "Winner: X!"
        elif winner == 2:
            bottom = "Winner: O!"
        else:
            bottom = "Tie!"
        rect = font.render(bottom, 1, black)
        pygame.draw.rect(screen, white, Rect(0, 300, 300, 200))
        screen.blit(rect, (0, 310))
        pygame.display.update()
        while pygame.mouse.get_pressed() != (0, 0, 0):
            pygame.event.get()
        while finished == True:
            if pygame.mouse.get_pressed() != (0, 0, 0):
                finished = False
            pygame.event.get()
        while pygame.mouse.get_pressed() != (0, 0, 0):
            pygame.event.get()
        resetpos()
current = 1
def checknew(x, y):
    global positions
    cell = callcell(x, y)
    if cell[1] == 0:
        return True
    else:
        return False
resetpos()
while True:
    updatescreenonpos()
    pygame.event.get()
    
    
        


