import pygame

from code.Entity import Entity


class DinoPlayer(Entity):
    def __init__(self, name, position: tuple):
        super().__init__(name, position)
        self.frames = [
            pygame.image.load('./asset/Run1.png').convert_alpha(),
            pygame.image.load('./asset/Run2.png').convert_alpha(),
            pygame.image.load('./asset/Run3.png').convert_alpha(),
            pygame.image.load('./asset/Run4.png').convert_alpha(),
            pygame.image.load('./asset/Run5.png').convert_alpha(),
            pygame.image.load('./asset/Run6.png').convert_alpha(),
            pygame.image.load('./asset/Run7.png').convert_alpha(),
            pygame.image.load('./asset/Run8.png').convert_alpha()
        ]

        self.jump_frame = pygame.image.load('./asset/Jump.png').convert_alpha()

        self.jumping = False
        self.jump_speed = 0
        self.gravity = 1
        self.ground_y = position[1]

        self.frame_atual = 0
        self.surf = self.frames[0]

        self.timer = 0


    def update(self):
        if self.jumping:
            self.surf = self.jump_frame
            return

        self.timer += 1

        if self.timer >= 10:  # velocidade da animação
            self.timer = 0
            self.frame_atual += 1

            if self.frame_atual >= len(self.frames):
                self.frame_atual = 0

            self.surf = self.frames[self.frame_atual]

    def move(self):
        self.update()

        if self.jumping:
            self.rect.y += self.jump_speed
            self.jump_speed += self.gravity

            if self.rect.y >= self.ground_y:
                self.rect.y = self.ground_y
                self.jumping = False
                self.jump_speed = 0


    def jump(self):
        if not self.jumping:
            self.jumping = True
            self.jump_speed = -18