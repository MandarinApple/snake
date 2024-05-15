import random
from settings import WIDTH, HEIGHT
class Food():
    def __init__(self):
        self.x = random.randrange(10, WIDTH-10, 5)
        self.y = random.randrange(10, HEIGHT-10, 5)
        