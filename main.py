import pygame
import random
from food import Food 
from snake import Snake
from menu import menu
from settings import *
pygame.init()

bg.play(loops = 1)
bg.set_volume(0.4)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")
snake = Snake(pygame, screen)
xfood = Food()
menu.main_menu().mainloop(screen)

def draw():
    screen.fill(BLACK)
    food = pygame.draw.rect(screen, RED, (xfood.x, xfood.y, SIZE, SIZE))
    if food.x + SIZE > snake.x > food.x - SIZE and food.y + SIZE > snake.y > food.y - SIZE:
        xfood.x = random.randrange(10, WIDTH-10, 5)
        xfood.y = random.randrange(10, HEIGHT-10, 5)
        snake.length += 1
        eat.play()
        eat.set_volume(0.5)
    snake.move(vector)
    snake.bord()
    snake.snake()
    snake.gameover()
    font_style = pygame.font.SysFont("Arial", size = 25)
    message = font_style.render(f"Очки: {snake.length -1}", True, WHITE)
    screen.blit(message, [10, 10])
    pygame.display.update()


while True:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                if vector != "s" or snake.length == 1:
                    vector = "w"
            if event.key == pygame.K_s:
                if vector != "w" or snake.length == 1:
                    vector = "s"
            if event.key == pygame.K_a:
                if vector != "d" or snake.length == 1:
                    vector = "a"
            if event.key == pygame.K_d:
                if vector != "a" or snake.length == 1:
                    vector = "d"
            if event.key == pygame.K_m:
                menu.main_menu().mainloop(screen)
    pygame.time.Clock().tick(FPS)
