#Variables
#Author: Zante M.
#
#This is the place where variables and functions used throughout
#Zreet Fighter: The Seven Forms are kept for easy access and convenience


import pygame
from pygame.locals import *

pygame.init()


clock = pygame.time.Clock()

#For the screen
width = 1366
height = 768
screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
pygame.display.set_caption("Ztreet Figher: The Seven Forms")
pygame.mouse.set_visible(True)
