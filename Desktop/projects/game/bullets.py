import pygame


class GameObject:
    def __init__(self, x, y):
        self.image = pygame.image.load('bullet.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        mous_pos = pygame.mouse.get_pos()
        self.dx = mous_pos[0] - x
        self.dy = mous_pos[1] - y


    def Draw(self):
        pygame.display.set_mode((1280, 720)).blit(self.image, self.rect.center)
    
    def Shoot(self):
        self.rect.x += self.dx
        self.rect.y += self.dy


