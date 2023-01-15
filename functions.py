import sys
import random
import pygame

from vars import CLOCK, FPS, INFO_FONT, PRICE_FONT
from images import WINDOW, BACKGROUND_IMAGE, SKELETON_IMAGES, BOSS_IMAGES


def rewind(top, coefficient=-1):
    for distance in range(1, 24, 2):
        for _ in range(5):
            WINDOW.blit(BACKGROUND_IMAGE, (0, (top := top + distance * coefficient)))
            check_closure()

    for distance in range(23, 0, -2):
        for _ in range(5):
            WINDOW.blit(BACKGROUND_IMAGE, (0, (top := top + distance * coefficient)))
            check_closure()

    return top


def check_closure():
    for local_event in pygame.event.get():
        if local_event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    CLOCK.tick(FPS)


def draw(text, x, y):
    for line in text:
        y += 50
        tmp = INFO_FONT.render(line, True, (255, 255, 255))
        WINDOW.blit(tmp, (x, y))


def draw_prices(prices, y):
    x = 100
    for price in prices:
        tmp = PRICE_FONT.render(price, True, (255, 255, 255))
        WINDOW.blit(tmp, (x, y))
        x += 390


def get_enemy_characteristic(level, enemy='SKELETON', coefficient=1):
    images, number = {
        'SKELETON': (SKELETON_IMAGES, 3 * level),
        'BOSS':     (BOSS_IMAGES,     5 * level)
    }[enemy]

    return [
        5 * coefficient + number,
        10**1 + number,
        20 * coefficient,
        images,
    ]