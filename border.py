import pygame

BORDER_SPRITE = pygame.sprite.GroupSingle()


class Border(pygame.sprite.Sprite):
    def __init__(self, image, position):
        super().__init__(BORDER_SPRITE)

        self.add(BORDER_SPRITE)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = position
