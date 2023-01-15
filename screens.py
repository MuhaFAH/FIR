from vars import *
from coin import COIN_SPRITE
from enemy import ENEMY_SPRITES, Enemy
from player import PLAYER_SPRITE

from functions import *
from images import                                                       \
    SILVER_ARMOR, GOLD_ARMOR, RUBIN_ARMOR, EMERALD_ARMOR, DIAMOND_ARMOR, \
    BACKGROUND_IMAGE, PAUSE_MENU_IMAGE


def first_screen():
    while not start_btn.draw():
        check_closure()
        WINDOW.blit(BACKGROUND_IMAGE, (0, 0))
    rewind(0)


def second_screen():
    while not (index := (arena_btn.draw() or shop_btn.draw())):
        if silver_armor_btn.equip():
            player.armor = SILVER_ARMOR
        if gold_armor_btn.equip():
            player.armor = GOLD_ARMOR
        if rubin_armor_btn.equip():
            player.armor = RUBIN_ARMOR
        if emerald_armor_btn.equip():
            player.armor = EMERALD_ARMOR
        if diamond_armor_btn.equip():
            player.armor = DIAMOND_ARMOR

        if silver_sword_btn.equip():
            player.weapon = 0
        if gold_sword_btn.equip():
            player.weapon = 1
        if rubin_sword_btn.equip():
            player.weapon = 2
        if emerald_sword_btn.equip():
            player.weapon = 3
        if diamond_sword_btn.equip():
            player.weapon = 4

        if armor_buff_btn.equip():
            print('УСИЛИТЕЛЬ')
        if heal_buff_btn.equip():
            print('УСИЛИТЕЛЬ')
        if speed_buff_btn.equip():
            print('УСИЛИТЕЛЬ')
        if damage_buff_btn.equip():
            print('УСИЛИТЕЛЬ')

        check_closure()

        WINDOW.blit(BACKGROUND_IMAGE,  (0,   -1440))
        WINDOW.blit(sword_text,        (965, 155))
        WINDOW.blit(armor_text,        (885, 359))
        WINDOW.blit(buff_text,         (895, 559))
        WINDOW.blit(coin.text,         (400, 10))

        player.change_size(6)
        coin.change_size(4)

        PLAYER_SPRITE.draw(WINDOW)
        COIN_SPRITE.draw(WINDOW)
        COIN_SPRITE.update(player.money)

    return index


def pause_menu():
    while True:
        WINDOW.blit(PAUSE_MENU_IMAGE, (WINDOW.get_width() / 2 - PAUSE_MENU_IMAGE.get_width() / 2,
                                       250))
        if continue_game_btn.draw():
            return
        if leave_game_btn.draw():
            print('ВЫХОД')
        if leave_arena_btn.draw():
            player.dead = True
            return
        if settings_btn.draw():
            print('НАСТРОЙКИ')

        check_closure()


def shop():
    price_text = ['15', '35', '50', '100']
    info_text = (
        ('Золотая',     '+50 HP'),
        ('Рубиновая',   '+75 HP'),
        ('Нефритовая',  '+100 HP'),
        ('Алмазная',    '+125 HP'),
        ('Золотой',     '15 DAMAGE'),
        ('Жнец',        '25 DAMAGE'),
        ('Жемчуг',      '35 DAMAGE'),
        ('Небесный',    '50 DAMAGE'),
        ('Починка',     'брони'),
        ('Лечение на',  'поле боя'),
        ('Увеличение',  'скорости'),
        ('Увеличение',  'урона')
    )

    gold_armor_btn.rect.x = gold_sword_btn.rect.x = armor_buff_btn.rect.x = 60
    rubin_armor_btn.rect.x = rubin_sword_btn.rect.x = heal_buff_btn.rect.x = 450
    emerald_armor_btn.rect.x = emerald_sword_btn.rect.x = speed_buff_btn.rect.x = 840
    diamond_armor_btn.rect.x = diamond_sword_btn.rect.x = damage_buff_btn.rect.x = 1230
    coin.rect.x, coin.rect.y = 755, 75

    for y in range(200, 700, 200):
        for x in range(70, 1300, 390):
            small_coin = Coin(COIN_IMAGES, (x, y), 0, 100)
            small_coin.change_size(2)
    coin.change_size(4)

    while not back_btn.draw():
        if gold_armor_btn.buy(player.money):
            gold_armor_btn.purchased = True
            player.money -= gold_armor_btn.price
            player.armor = GOLD_ARMOR
            coin.update(15)
        if rubin_armor_btn.buy(player.money):
            rubin_armor_btn.purchased = True
            player.money -= rubin_armor_btn.price
            player.armor = RUBIN_ARMOR
            coin.update(35)
        if emerald_armor_btn.buy(player.money):
            emerald_armor_btn.purchased = True
            player.money -= emerald_armor_btn.price
            player.armor = EMERALD_ARMOR
            coin.update(50)
        if diamond_armor_btn.buy(player.money):
            diamond_armor_btn.purchased = True
            player.money -= diamond_armor_btn.price
            player.armor = DIAMOND_ARMOR
            coin.update(100)

        if gold_sword_btn.buy(player.money):
            gold_sword_btn.purchased = True
            player.money -= gold_sword_btn.price
            player.weapon = 1
            coin.update(15)
        if rubin_sword_btn.buy(player.money):
            rubin_sword_btn.purchased = True
            player.money -= rubin_sword_btn.price
            player.weapon = 2
            coin.update(35)
        if emerald_sword_btn.buy(player.money):
            emerald_sword_btn.purchased = True
            player.money -= emerald_sword_btn.price
            player.weapon = 3
            coin.update(50)
        if diamond_sword_btn.buy(player.money):
            diamond_sword_btn.purchased = True
            player.money -= diamond_sword_btn.price
            player.weapon = 4
            coin.update(100)

        if armor_buff_btn.buy(player.money):
            print('УСИЛИТЕЛЬ')
        if heal_buff_btn.buy(player.money):
            print('УСИЛИТЕЛЬ')
        if speed_buff_btn.buy(player.money):
            print('УСИЛИТЕЛЬ')
        if damage_buff_btn.buy(player.money):
            print('УСИЛИТЕЛЬ')

        for i in range(4):
            draw(info_text[i], 200 + 390 * i, 400)
            draw(info_text[i + 4], 200 + 390 * i, 200)
            draw(info_text[i + 8], 200 + 390 * i, 600)
            draw_prices(price_text, 189 + 200 * (i % 3))

        check_closure()
        WINDOW.blit(BACKGROUND_IMAGE,  (0,   -1440))
        WINDOW.blit(shop_text,         (455, 0))
        WINDOW.blit(coin.text,         (830, 65))

        COIN_SPRITE.draw(WINDOW)
        COIN_SPRITE.update(player.money)

    for coins in COIN_SPRITE:
        if coins != coin:
            coins.kill()

    gold_armor_btn.rect.x = gold_sword_btn.rect.x = 860
    rubin_armor_btn.rect.x = rubin_sword_btn.rect.x = 1035
    emerald_armor_btn.rect.x = emerald_sword_btn.rect.x = 1210
    diamond_armor_btn.rect.x = diamond_sword_btn.rect.x = 1385
    armor_buff_btn.rect.x, heal_buff_btn.rect.x = 735, 935
    speed_buff_btn.rect.x, damage_buff_btn.rect.x = 1135, 1335
    coin.rect.x, coin.rect.y = 327, 17


def third_screen():
    rewind(-1440)
    player.frame = 0
    player.change_size()
    player.rect.center = WINDOW.get_rect().center
    player.hit_points = 100
    player.last_move_index = 6
    player.alive = True
    player.dead = False
    player.attack = False

    enemies = [
        get_enemy_characteristic(player.level // 2) + [(random.randint(300, 1000), random.randint(200, 400)), player]
        for _
        in range(player.level // 2 * 3 + 5)
    ] + [
        get_enemy_characteristic(player.level // 2, 'BOSS', 3) + [(random.randint(300, 1000), random.randint(200, 400)), player]
        for _
        in range(1)
    ]

    while len(pressed_buttons) > 1:
        pressed_buttons.pop(-1)

    for enemy in ENEMY_SPRITES:
        enemy.kill()

    while (not player.dead) and (ENEMY_SPRITES or enemies):
        player_attack = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event == pygame.K_ESCAPE:
                pause_menu()
            if event.type == pygame.KEYDOWN:
                pressed_buttons.append(event.key)
            if event.type == pygame.KEYUP and len(pressed_buttons) > 1:
                pressed_buttons.remove(event.key)
            if event.type == MAKE_NEW_ENEMY_EVENT and enemies:
                Enemy(*enemies.pop(0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_attack = True

        WINDOW.blit(BACKGROUND_IMAGE, (0, -2880))
        PLAYER_SPRITE.draw(WINDOW)
        ENEMY_SPRITES.draw(WINDOW)
        PLAYER_SPRITE.update(pressed_buttons[-1], player_attack, border)
        ENEMY_SPRITES.update()

        pygame.display.flip()
        CLOCK.tick(FPS)

    player.change_size(6)
    player.rect.center = (0, 290)
    player.frame = 0
    rewind(-2880, 1)
