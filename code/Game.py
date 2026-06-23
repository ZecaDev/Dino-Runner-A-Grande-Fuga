import pygame

from code.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from code.Level import Level
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:

                level = Level(self.window, 'Level1', menu_return)
                level_return = level.run()

                if level_return is True:
                    self.win_screen()

                else:
                    self.lose_screen()

            elif menu_return == MENU_OPTION[1]:
                pygame.quit()
                return

    def win_screen(self):
        self.window.fill((0, 0, 0))

        font = pygame.font.SysFont("Consolas", 60)
        text = font.render("YOU WIN!", True, (0, 255, 0))

        rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(text, rect)

        pygame.display.flip()
        pygame.time.delay(2000)

    def lose_screen(self):
        self.window.fill((0, 0, 0))

        font = pygame.font.SysFont("Consolas", 60)
        text = font.render("GAME OVER", True, (255, 0, 0))

        rect = text.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
        self.window.blit(text, rect)

        pygame.display.flip()
        pygame.time.delay(2000)



