import pygame.image

from code.Const import WIN_WIDTH, COLOR_WHITE, MENU_OPTION, COLOR_ORANGE, COLOR_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./asset/bk7.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/menu.mp3')
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text("Dino Runner:", 40, COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text("A Grande Fuga", 20, COLOR_WHITE, ((WIN_WIDTH / 2), 100))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(MENU_OPTION[i], 17, COLOR_YELLOW, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(MENU_OPTION[i], 15, COLOR_ORANGE, ((WIN_WIDTH / 2), 200 + 30 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]


    def menu_text(self, text: str, text_size: int, text_color: tuple, center_pos: tuple):
        text_font = pygame.font.SysFont("Consolas", text_size)
        text_surf = text_font.render(text, True, text_color).convert_alpha()
        text_rect = text_surf.get_rect(center=center_pos)

        self.window.blit(text_surf, text_rect)

