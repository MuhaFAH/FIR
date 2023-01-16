import pygame

from enemy import ENEMY_SPRITES
from images import PLAYER_RECT_IMAGE

PLAYER_SPRITE = pygame.sprite.GroupSingle()


class Player(pygame.sprite.Sprite):
    def __init__(self, armor, position):
        super().__init__(PLAYER_SPRITE)

        self.add(PLAYER_SPRITE)
        self.image = armor[0][0][0]
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.hit_points = 125
        self.damage = 10
        self.speed = 3
        self.frame = 0
        self.last_move_index = 6
        self.attack = False
        self.alive = True
        self.dead = False

        self.sword = 0
        self.level = 1
        self.armor = armor
        self.money = 500

        self.movement_dict = {
            (pygame.K_LEFT,  False):   (0,  (-self.speed,  0)),
            (pygame.K_RIGHT, False):   (1,  (self.speed,   0)),
            (pygame.K_UP,    False):   (2,  (0,  -self.speed)),
            (pygame.K_DOWN,  False):   (3,  (0,   self.speed)),
            ('STAY',         False):   (4,  (0,            0)),
            (pygame.K_LEFT,  True):    (5,  (-self.speed,  0)),
            (pygame.K_RIGHT, True):    (6,  (self.speed,   0)),
            (pygame.K_UP,    True):    (-1, (0,  -self.speed)),
            (pygame.K_DOWN,  True):    (-1, (0,   self.speed)),
            ('STAY',         True):    (-1, (0,            0))
        }

    def change_size(self, scale=1):
        if not self.frame % 9:
            image = self.armor[self.sword][4][self.frame % 4]
            self.image = pygame.transform.scale(image, (image.get_width() * scale, image.get_height() * scale))

        self.frame = (self.frame + 1) % 36

    def update(self, pressed_button, attack, border):
        action_index, player_movement = self.movement_dict.get((pressed_button, attack), self.movement_dict[('STAY', False)])
        position, self.rect = self.rect.center, self.rect.move(player_movement)
        self.image, image, step = PLAYER_RECT_IMAGE, self.image, 7

        if self.hit_points <= 0 and self.alive:
            self.frame = 0
            self.alive = False

        if attack and self.alive and not self.attack:
            self.frame = 0
            self.attack = True

        if action_index in {0, 1, 5, 6}:
            self.last_move_index = [5, 6][(action_index // 6 + action_index % 3) % 2]

        if not self.alive:
            self.make_a_murder()
            self.rect.center = position
            step, action_index = 30, 7

        if self.attack:
            self.make_an_attack()
            action_index = self.last_move_index

        if pygame.sprite.collide_mask(self, border):
            self.rect.center = position
            action_index = 4

        self.image = self.change_image(action_index, image, step)

    def make_a_murder(self):
        if self.frame == 209:
            self.dead = True

    def make_an_attack(self):
        opponent = pygame.sprite.spritecollideany(self, ENEMY_SPRITES)
        if self.frame == 42:
            if opponent:
                opponent.hit_points -= self.damage
            self.attack = False

    def change_image(self, index, now_image, step):
        self.frame += 1
        if not self.frame % step:
            return self.armor[self.sword][index][self.frame // step % len(self.armor[self.sword][index])]
        return now_image
