import pygame

print('Setup started')
pygame.init()
screen = pygame.display.set_mode(size=(600, 480))
print('Setup finished')

print('Setup started')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()