import sys

import pygame

from vars import *
from coin import COIN_SPRITE
from enemy import ENEMY_SPRITES, Enemy
from player import PLAYER_SPRITE

from functions import *
from images import \
    SILVER_ARMOR, GOLD_ARMOR, RUBIN_ARMOR, EMERALD_ARMOR, DIAMOND_ARMOR, \
    BACKGROUND_IMAGE, PAUSE_MENU_IMAGE, HEALTHBAR


def first_screen():
    silver_sword_btn.selected = silver_armor_btn.selected = True
    while not start_btn.draw():
        check_closure()
        WINDOW.blit(BACKGROUND_IMAGE, (0, 0))
    rewind(0)


def second_screen():
    while not (index := (arena_btn.draw() or shop_btn.draw())):
        if silver_armor_btn.equip():
            player.armor = SILVER_ARMOR
            for i in ['rubin', 'gold', 'emerald', 'diamond']: eval(f'{i}_armor_btn').selected = False
        if gold_armor_btn.equip():
            player.armor = GOLD_ARMOR
            for i in ['silver', 'rubin', 'emerald', 'diamond']: eval(f'{i}_armor_btn').selected = False
        if rubin_armor_btn.equip():
            player.armor = RUBIN_ARMOR
            for i in ['silver', 'gold', 'emerald', 'diamond']: eval(f'{i}_armor_btn').selected = False
        if emerald_armor_btn.equip():
            player.armor = EMERALD_ARMOR
            for i in ['silver', 'gold', 'rubin', 'diamond']: eval(f'{i}_armor_btn').selected = False
        if diamond_armor_btn.equip():
            player.armor = DIAMOND_ARMOR
            for i in ['silver', 'gold', 'emerald', 'rubin']: eval(f'{i}_armor_btn').selected = False

        if silver_sword_btn.equip():
            player.sword = 0
            for i in ['rubin', 'gold', 'emerald', 'diamond']: eval(f'{i}_sword_btn').selected = False
        if gold_sword_btn.equip():
            player.sword = 1
            for i in ['silver', 'rubin', 'emerald', 'diamond']: eval(f'{i}_sword_btn').selected = False
        if rubin_sword_btn.equip():
            player.sword = 2
            for i in ['silver', 'gold', 'emerald', 'diamond']: eval(f'{i}_sword_btn').selected = False
        if emerald_sword_btn.equip():
            player.sword = 3
            for i in ['silver', 'gold', 'rubin', 'diamond']: eval(f'{i}_sword_btn').selected = False
        if diamond_sword_btn.equip():
            player.sword = 4
            for i in ['silver', 'gold', 'emerald', 'rubin']: eval(f'{i}_sword_btn').selected = False

        if armor_buff_btn.equip():
            print('УСИЛИТЕЛЬ')
        if heal_buff_btn.equip():
            print('УСИЛИТЕЛЬ')
        if speed_buff_btn.equip():
            print('УСИЛИТЕЛЬ')
        if damage_buff_btn.equip():
            print('УСИЛИТЕЛЬ')

        check_closure()

        WINDOW.blit(BACKGROUND_IMAGE, (0, -1440))
        WINDOW.blit(sword_text, (965, 155))
        WINDOW.blit(armor_text, (885, 359))
        WINDOW.blit(buff_text, (895, 559))
        WINDOW.blit(coin.text, (400, 10))

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
            sys.exit()
        if leave_arena_btn.draw():
            player.dead = True
            return
        if settings_btn.draw():
            print('НАСТРОЙКИ')

        check_closure()


def shop():
    price_text = ['15', '35', '50', '100']
    info_text = (
        ('Золотая', '+50 HP'),
        ('Рубиновая', '+75 HP'),
        ('Нефритовая', '+100 HP'),
        ('Алмазная', '+125 HP'),
        ('Золотой', '15 DAMAGE'),
        ('Жнец', '25 DAMAGE'),
        ('Жемчуг', '35 DAMAGE'),
        ('Небесный', '50 DAMAGE'),
        ('Починка', 'брони'),
        ('Лечение на', 'поле боя'),
        ('Увеличение', 'скорости'),
        ('Увеличение', 'урона')
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
            player.hit_points = 150
            coin.update(15)
        if rubin_armor_btn.buy(player.money):
            rubin_armor_btn.purchased = True
            player.money -= rubin_armor_btn.price
            player.armor = RUBIN_ARMOR
            player.hit_points = 175
            coin.update(35)
        if emerald_armor_btn.buy(player.money):
            emerald_armor_btn.purchased = True
            player.money -= emerald_armor_btn.price
            player.armor = EMERALD_ARMOR
            player.hit_points = 200
            coin.update(50)
        if diamond_armor_btn.buy(player.money):
            diamond_armor_btn.purchased = True
            player.money -= diamond_armor_btn.price
            player.armor = DIAMOND_ARMOR
            player.hit_points = 225
            coin.update(100)

        if gold_sword_btn.buy(player.money):
            gold_sword_btn.purchased = True
            player.money -= gold_sword_btn.price
            player.sword = 1
            player.damage = 20
            coin.update(15)
        if rubin_sword_btn.buy(player.money):
            rubin_sword_btn.purchased = True
            player.money -= rubin_sword_btn.price
            player.sword = 2
            player.damage = 35
            coin.update(35)
        if emerald_sword_btn.buy(player.money):
            emerald_sword_btn.purchased = True
            player.money -= emerald_sword_btn.price
            player.sword = 3
            player.damage = 50
            coin.update(50)
        if diamond_sword_btn.buy(player.money):
            diamond_sword_btn.purchased = True
            player.money -= diamond_sword_btn.price
            player.sword = 4
            player.damage = 75
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
        WINDOW.blit(BACKGROUND_IMAGE, (0, -1440))
        WINDOW.blit(shop_text, (455, 0))
        WINDOW.blit(coin.text, (830, 65))

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
    armor_buff_btn.scale = heal_buff_btn.scale = speed_buff_btn.scale = damage_buff_btn.scale = 0.8
    armor_buff_btn.rect.x = 1300
    armor_buff_btn.rect.y = 765
    heal_buff_btn.rect.x = 1300
    heal_buff_btn.rect.y = 860
    speed_buff_btn.rect.x = 1390
    speed_buff_btn.rect.y = 765
    damage_buff_btn.rect.x = 1390
    damage_buff_btn.rect.y = 860
    rewind(-1440)
    player.frame = 0
    player.change_size()
    player.rect.center = WINDOW.get_rect().center
    player.last_move_index = 6
    player.alive = True
    player.dead = False
    player.attack = False
    boss_spawned = boss_dead = False
    healthbar = player.hit_points

    enemies = [
                  get_enemy_characteristic(player.level // 2) + [(random.randint(300, 1000), random.randint(200, 400)),
                                                                 player]
                  for _
                  in range(player.level // 2 * 3 + 5)
              ]

    while len(pressed_buttons) > 1:
        pressed_buttons.pop(-1)

    for enemy in ENEMY_SPRITES:
        enemy.kill()

    while (not player.dead) and not boss_dead:
        player_attack = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event == pygame.K_ESCAPE:
                pause_menu()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    if 100 <= player.hit_points < healthbar:
                        player.hit_points += (player.hit_points + 25) - healthbar if player.hit_points + 25 > healthbar else 25
                if event.key == pygame.K_y:
                    player.speed += 1
                if event.key == pygame.K_u:
                    player.damage += 15
                if event.key == pygame.K_t:
                    if player.hit_points < 100:
                        player.hit_points += (player.hit_points + 35) - 100 if player.hit_points + 35 > 100 else 35
                pressed_buttons.append(event.key)
            if event.type == pygame.KEYUP and len(pressed_buttons) > 1:
                pressed_buttons.remove(event.key)
            if event.type == MAKE_NEW_ENEMY_EVENT and enemies:
                Enemy(*enemies.pop(0))
            if not (ENEMY_SPRITES or enemies) and not boss_spawned:
                Enemy(*[get_enemy_characteristic(player.level // 2, 'BOSS', 3) + [
                      (random.randint(300, 1000), random.randint(200, 400)), player]
                  for _
                  in range(1)].pop(0))
                boss_spawned = True
            if boss_spawned:
                if not ENEMY_SPRITES:
                    boss_dead = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_attack = True
        if boss_dead:
            player.level += 1
        if player.hit_points <= 100:
            player.armor = SILVER_ARMOR
        WINDOW.blit(BACKGROUND_IMAGE, (0, -2880))
        draw_text('R', (1260, 780))
        draw_text('T', (1260, 875))
        draw_text('Y', (1485, 780))
        draw_text('U', (1485, 875))
        if armor_buff_btn.use():
            player.hit_points += (player.hit_points + 25) - healthbar if player.hit_points + 25 > healthbar else 25
        if heal_buff_btn.use():
            player.hit_points += (player.hit_points + 35) - 100 if player.hit_points + 35 > 100 else 35
        if speed_buff_btn.use():
            player.speed += 1
        if damage_buff_btn.use():
            player.damage += 10
        WINDOW.blit(arena_text, (35, 10))
        WINDOW.blit(HEALTHBAR, (10, 825))
        pygame.draw.rect(WINDOW, 'black', (100, 830, healthbar * 3, 60))
        if player.hit_points > 100:
            pygame.draw.rect(WINDOW, 'green', (100, 830, 100 * 3, 60))
            pygame.draw.rect(WINDOW, 'blue', (100 + 100 * 3, 830, (player.hit_points - 100) * 3, 60))
        else:
            pygame.draw.rect(WINDOW, 'green', (100, 830, player.hit_points * 3, 60))
        pygame.draw.rect(WINDOW, 'white', (100, 830, healthbar * 3, 60), 5)
        PLAYER_SPRITE.draw(WINDOW)
        ENEMY_SPRITES.draw(WINDOW)
        PLAYER_SPRITE.update(pressed_buttons[-1], player_attack, border)
        ENEMY_SPRITES.update()

        pygame.display.flip()
        CLOCK.tick(FPS)
    player.hit_points = 125
    player.change_size(6)
    player.rect.center = (0, 290)
    player.frame = 0
    rewind(-2880, 1)
