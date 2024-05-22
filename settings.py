import pygame
pygame.init()

bg = pygame.mixer.Sound("sounds/bg.mp3")
eat = pygame.mixer.Sound("sounds/eat.mp3")
gameover = pygame.mixer.Sound("sounds/gameover.mp3")

WIDTH = 500
HEIGHT = 600
FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 
GREEN = (0, 255, 0)
RED = (255, 0, 0)

SIZE = 20
vector = None 