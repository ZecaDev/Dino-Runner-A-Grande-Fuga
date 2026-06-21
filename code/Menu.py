import pygame.image

from code.Const import WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/bk7.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Dino Runner:", 40, COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text("A Grande Fuga", 20, COLOR_WHITE, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                self.menu_text(MENU_OPTION[i], 15, COLOR_ORANGE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

    def menu_text(self, text: str, text_size: int, text_color: tuple, center_pos: tuple):
        text_font = pygame.font.SysFont("Consolas", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=center_pos)

        # sombra = text_font.render("START", True, (0, 0, 0))
        # texto = text_font.render("START", True, (255, 215, 0))

        self.window.blit(text_surf, text_rect)
        # self.window.blit(sombra, (251, 201))
        # self.window.blit(texto, (250, 200))
