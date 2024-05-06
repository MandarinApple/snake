import pygame
from menu import menu
from settings import *
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
menu.main_menu().mainloop(screen)

def draw():
    screen.fill(BLACK)
    pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

