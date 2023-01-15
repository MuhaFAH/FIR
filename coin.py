import pygame

from images import COIN_IMAGES

COIN_SPRITE = pygame.sprite.Group()


class Coin(pygame.sprite.Sprite):
    def __init__(self, images, position, money, font_size):
        super().__init__(COIN_SPRITE)
        self.add(COIN_SPRITE)
        self.image = images[0]
        self.rect = self.image.get_rect()
        self.rect.center = position
        self.font = pygame.font.Font('assets/fonts/Comic Sans MS Pixel.ttf', font_size)
        self.text = self.font.render(f'{money}', True, (255, 255, 255))
        self.scale = 1

        self.frame = 0
        self.tick = 0

    def change_size(self, scale=1):
        self.scale = scale

    def update(self, money):
        self.text = self.font.render(f'{money}', True, (255, 255, 255))
        if not self.tick:
            self.frame = (self.frame + 1) % 8
            image = COIN_IMAGES[self.frame % 8]
            self.image = pygame.transform.scale(image, (image.get_width() * self.scale, image.get_height() * self.scale))
        self.tick = (self.tick + 1) % 7
