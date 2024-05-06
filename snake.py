from settings import *
class Snake:
    def __init__(self, pygame, screen):
        self.pygame = pygame
        self.screen = screen 
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.snake_body = []
        self.length = 1
        
    
    def move(self, vector):
        if vector == "w":
            self.y -=5
        if vector == "a":
            self.x -=5
        if vector == "s":
            self.y +=5
        if vector == "d":
            self.x +=5

    def snake(self):
        snake_head = [self.x, self.y]
        self.snake_body.append(snake_head)
        for i in self.snake_body:
            self.pygame.draw.rect(self.screen, GREEN, (i[0], i[1], SIZE, SIZE))
            if self.snake_body > self.length:
                del self.snake_body[0]

    def bord(self):
        if self.x > WIDTH:
            self.x = 0 
        if self.y > HEIGHT:
            self.y = 0 
        if self.x < 0:
            self.x = WIDTH
        if self.y < 0:
            self.y = HEIGHT
             