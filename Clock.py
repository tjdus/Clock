import pygame
import os
import numpy as np

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

GRAY = (200, 200, 200)
BLACK = (0,0,0)
WHITE = (255,255,255)

CenterPos= WINDOW_WIDTH / 2 , WINDOW_HEIGHT /2

pygame.init()

pygame.display.set_caption("Clock")

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

Clockimg= pygame.image.load(os.path.join(assets_path, 'clock.png'))


class ClockHand():
    def __init__(self, length, time, width):
        self.time = time
        self.length = length
        self.form = np.array( [[0, 0, 0], [length, 0, 0], [0, 0, 0]])
        self.width = width
        
    def update(self):
        self.rotate()
        self.draw()
        
    def rotate(self):
        radian = np.deg2rad(second//self.time + 180)
        c = np.cos(radian)
        s = np.sin(radian)
        R = np.array( [[c, -s, 0], [s, c, 0], [0, 0, 0] ] )
        self.R=R
        points = self.R @ self.form
        self.points = points[:2, :].T + CenterPos
    def draw(self):
        pygame.draw.line(screen, BLACK, self.points[0], self.points[1], self.width)



second = 0

SecondHand = ClockHand(300,1, 5)
MinuteHand = ClockHand(150, 60, 8)
HourHand = ClockHand(100,3600, 10)

done = False

width, height = Clockimg.get_size()
clockposition = np.array(CenterPos) - np.array((width/2, height/2))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    pygame.display.flip()

    second+=1
    screen.fill(WHITE)
    
    
    screen.blit(Clockimg, clockposition)
    SecondHand.update()
    MinuteHand.update()
    HourHand.update()
    clock.tick(60)


pygame.quit()
