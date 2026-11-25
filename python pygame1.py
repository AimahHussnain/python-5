import pygame
pygame.init()
screen = pygame.display.set_module((400,500))
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT():
            pygame.quit()
    display.pygame.flip()
