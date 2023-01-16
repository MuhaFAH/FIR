import pygame
import pickle

from coin import Coin
from player import Player
from border import Border
from button import Button, Item
from images import                                                                                                                  \
    START_GAME_BTN_IMAGE,     SHOP_BTN_IMAGE,         ARENA_BTN_IMAGE,         WINDOW,                                              \
    CONTINUE_GAME_BTN_IMAGE,  LEAVE_GAME_BTN_IMAGE,   LEAVE_ARENA_BTN_IMAGE,   SETTINGS_BTN_IMAGE,        BACK_BTN_IMAGE,           \
    SILVER_ARMOR_BTN_IMAGES,  GOLD_ARMOR_BTN_IMAGES,  RUBIN_ARMOR_BTN_IMAGES,  EMERALD_ARMOR_BTN_IMAGES,  DIAMOND_ARMOR_BTN_IMAGES, \
    SILVER_SWORD_BTN_IMAGES,  GOLD_SWORD_BTN_IMAGES,  RUBIN_SWORD_BTN_IMAGES,  EMERALD_SWORD_BTN_IMAGES,  DIAMOND_SWORD_BTN_IMAGES, \
    HEAL_BUFF_BTN_IMAGES,     ARMOR_BUFF_BTN_IMAGES,  SPEED_BUFF_BTN_IMAGES,   DAMAGE_BUFF_BTN_IMAGES,                              \
    BORDER_IMAGE,             COIN_IMAGES,            SILVER_ARMOR,            PLAYER_RECT_IMAGE


FPS = 60
ARENA_LEVEL = 1
DATA_DIR = 'data'
CLOCK = pygame.time.Clock()
MAKE_NEW_ENEMY_EVENT = pygame.USEREVENT + 1

FONT = pygame.font.Font('assets/fonts/Comic Sans MS Pixel.ttf',       80)
INFO_FONT = pygame.font.Font('assets/fonts/Comic Sans MS Pixel.ttf',  50)
PRICE_FONT = pygame.font.Font('assets/fonts/Comic Sans MS Pixel.ttf', 40)


border = Border(BORDER_IMAGE,                              (810,  375))
player = Player(SILVER_ARMOR,                              (0,    290))
coin = Coin(COIN_IMAGES,                                   (335,  25),   player.money, 80)

start_btn = Button(START_GAME_BTN_IMAGE,             1,    WINDOW.get_rect().center)
shop_btn = Button(SHOP_BTN_IMAGE,                   -1,    (170,  50),   scale=0.50)
arena_btn = Button(ARENA_BTN_IMAGE,                 -2,    (1380, 895),  scale=0.65)
back_btn = Button(BACK_BTN_IMAGE,                    1,    (237,  870),  scale=0.60)
continue_game_btn = Button(CONTINUE_GAME_BTN_IMAGE,  1,    (805,  425),  scale=0.70)
leave_game_btn = Button(LEAVE_GAME_BTN_IMAGE,        1,    (580,  590),  scale=0.40)
leave_arena_btn = Button(LEAVE_ARENA_BTN_IMAGE,      1,    (1040, 590),  scale=0.40)
settings_btn = Button(SETTINGS_BTN_IMAGE,            1,    (810,  515),  scale=0.40)

silver_armor_btn = Item(SILVER_ARMOR_BTN_IMAGES,     0,    (750,  500),  scale=1.30)
gold_armor_btn = Item(GOLD_ARMOR_BTN_IMAGES,         15,   (925,  500),  scale=1.30)
rubin_armor_btn = Item(RUBIN_ARMOR_BTN_IMAGES,       35,   (1100, 500),  scale=1.30)
emerald_armor_btn = Item(EMERALD_ARMOR_BTN_IMAGES,   50,   (1275, 500),  scale=1.30)
diamond_armor_btn = Item(DIAMOND_ARMOR_BTN_IMAGES,   100,  (1450, 500),  scale=1.30)

silver_sword_btn = Item(SILVER_SWORD_BTN_IMAGES,     0,    (750,  300),  scale=1.30)
gold_sword_btn = Item(GOLD_SWORD_BTN_IMAGES,         15,   (925,  300),  scale=1.30)
rubin_sword_btn = Item(RUBIN_SWORD_BTN_IMAGES,       35,   (1100, 300),  scale=1.30)
emerald_sword_btn = Item(EMERALD_SWORD_BTN_IMAGES,   50,   (1275, 300),  scale=1.30)
diamond_sword_btn = Item(DIAMOND_SWORD_BTN_IMAGES,   100,  (1450, 300),  scale=1.30)

armor_buff_btn = Item(ARMOR_BUFF_BTN_IMAGES,         15,   (800,  700),  scale=1.30)
heal_buff_btn = Item(HEAL_BUFF_BTN_IMAGES,           35,   (1000, 700),  scale=1.30)
speed_buff_btn = Item(SPEED_BUFF_BTN_IMAGES,         50,   (1200, 700),  scale=1.30)
damage_buff_btn = Item(DAMAGE_BUFF_BTN_IMAGES,       100,  (1400, 700),  scale=1.30)


sword_text = FONT.render('ОРУЖИЕ',            True,  (255, 255, 255))
armor_text = FONT.render('СНАРЯЖЕНИЕ',        True,  (255, 255, 255))
buff_text = FONT.render('УСИЛИТЕЛИ',          True,  (255, 255, 255))
shop_text = FONT.render('МАГАЗИН ПРЕДМЕТОВ',  True,  (255, 255, 255))

pressed_buttons = ['STAY']
window_top = 0


pygame.draw.ellipse(BORDER_IMAGE,    pygame.Color(0, 255, 0),  (0, 0, 1450, 650), 5)
pygame.draw.rect(PLAYER_RECT_IMAGE,  pygame.Color(0, 255, 0),  (0, 0, 150, 111))

pygame.time.set_timer(MAKE_NEW_ENEMY_EVENT, 4000)


items = (
    silver_armor_btn,   silver_sword_btn,
    gold_armor_btn,     gold_sword_btn,
    rubin_armor_btn,    rubin_sword_btn,
    emerald_armor_btn,  emerald_sword_btn,
    diamond_armor_btn,  diamond_sword_btn,
    armor_buff_btn,     heal_buff_btn,
    speed_buff_btn,     damage_buff_btn
)


def save_and_load():
    for local_event in pygame.event.get():
        if local_event.type == pygame.KEYDOWN:
            if local_event.key == pygame.K_z:
                player.money = 100000

            if local_event.key == pygame.K_s:
                number = 0
                for item in items:
                    with open(f'{DATA_DIR}/save{number}.dat', 'wb') as file:
                        pickle.dump(item.purchased, file)
                    number += 1
                with open(f'{DATA_DIR}/save{number}.dat', 'wb') as file:
                    pickle.dump(player.money, file)
                number += 1
                with open(f'{DATA_DIR}/save{number}.dat', 'wb') as file:
                    pickle.dump(player.level, file)
                number += 1

            if local_event.key == pygame.K_l:
                number = 0
                for item in items:
                    with open(f'{DATA_DIR}/save{number}.dat', 'rb') as file:
                        item.purchased = pickle.load(file)
                    number += 1
                with open(f'{DATA_DIR}/save{number}.dat', 'rb') as file:
                    player.money = pickle.load(file)
                number += 1
                with open(f'{DATA_DIR}/save{number}.dat', 'rb') as file:
                    player.level = pickle.load(file)
                number += 1
