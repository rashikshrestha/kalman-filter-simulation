# import numpy as np
import pygame, sys
from pygame.locals import QUIT

# set up the colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)

class Simulation:

    def __init__(self,resolution, name):

        self.button_state = [False,False,False,False]

        pygame.init()
        self.DISPLAYSURF = pygame.display.set_mode(resolution, 0, 32)
        pygame.display.set_caption(name)
        self.DISPLAYSURF.fill(BLACK)  # Initialize display

    def handle_events(self):
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.button_state[0] = True
                if event.key == pygame.K_DOWN:
                    self.button_state[1] = True
                if event.key == pygame.K_LEFT:
                    self.button_state[2] = True
                if event.key == pygame.K_RIGHT:
                    self.button_state[3] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.button_state[0] = False
                if event.key == pygame.K_DOWN:
                    self.button_state[1] = False
                if event.key == pygame.K_LEFT:
                    self.button_state[2] = False
                if event.key == pygame.K_RIGHT:
                    self.button_state[3] = False

            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def update_screen(self,X,X_est,Z):
        self.DISPLAYSURF.fill(BLACK)

        pygame.draw.circle(self.DISPLAYSURF, BLUE, (int(Z[0,0]), int(Z[1,0]) ), 5, 0)

        pygame.draw.circle(self.DISPLAYSURF, GREEN, (int(X_est[0,0]), int(X_est[1,0]) ), 5, 0)

        pygame.draw.circle(self.DISPLAYSURF, RED, (int(X[0,0]), int(X[1,0]) ), 5, 0)


        pygame.display.update()