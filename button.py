import pygame

from images import WINDOW


class Button:
    def __init__(self, image, index, position, scale=1):
        self.image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.clicked = False
        self.index = index

    def draw(self):
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return self.index


class Item(Button):
    def __init__(self, images, price, position, scale=1):
        super().__init__(images[-1], 1, position, scale)
        self.price = price
        self.images = images
        self.scale = scale
        self.purchased = False if self.price else True

    def draw(self):
        self.image = pygame.transform.scale(
            self.images[0],
            (self.images[0].get_width() * self.scale, self.images[0].get_height() * self.scale)
        ) if self.purchased else pygame.transform.scale(
            self.images[1],
            (self.images[1].get_width() * self.scale, self.images[1].get_height() * self.scale)
        )
        WINDOW.blit(self.image, (self.rect.x, self.rect.y))

        if self.rect.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return self.index

    def equip(self):
        if self.draw():
            if self.purchased:
                return True
        return False

    def buy(self, money):
        if self.draw():
            if not self.purchased and money >= self.price:
                return True
        return False
