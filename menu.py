import pygame_menu
from settings import WIDTH, HEIGHT

class Menu:
    def main_menu(self):
        self.mainmenu = pygame_menu.Menu("snake", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_GREEN)
        self.mainmenu.add.button("Play", self.mainmenu.disable)
        self.mainmenu.add.button("Exit",quit)
        return self.mainmenu


menu = Menu()
