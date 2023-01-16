import pygame

ENEMY_SPRITES = pygame.sprite.Group()


class Enemy(pygame.sprite.Sprite):
    def __init__(self, damage, hit_points, attack_distance, animation_list, position, player):
        super().__init__(ENEMY_SPRITES)

        self.add(ENEMY_SPRITES)
        self.image = animation_list[2][0]
        self.rect = self.image.get_rect()
        self.rect.center = position

        self.attack_distance = attack_distance
        self.animation_list = animation_list
        self.hit_points = hit_points
        self.damage = damage

        self.pl_x = player.rect.x
        self.pl_y = player.rect.y
        self.pl = player

        self.attacking = False
        self.act = False

        self.action = 2
        self.speed = 2
        self.move_number = 0
        self.frame = 0

    def update(self):
        if pygame.sprite.spritecollideany(self, ENEMY_SPRITES) == self and self.hit_points > 0:
            action = self.get_action()
        elif self.hit_points > 0:
            action = self.stay
        else:
            action = self.die

        self.change_image(action == self.action, *action())
        self.action = action

    def change_image(self, continuation_of_the_action, images_list, step):
        if continuation_of_the_action:
            self.frame = (self.frame + 1) % (len(images_list) * step)
            self.image = images_list[self.frame // step] if not self.frame % step else self.image
        else:
            enemy_position = self.rect.midbottom
            self.frame = 1
            self.image = images_list[self.frame // step]
            self.rect = self.image.get_rect()
            self.rect.midbottom = enemy_position

    def get_action(self):
        distance_to_right = abs(self.pl.rect.centerx + 40 - self.rect.centerx)
        distance_to_left = abs(self.pl.rect.centerx - 40 - self.rect.centerx)

        self.pl_x = self.pl.rect.centerx + [-40, 40][distance_to_left > distance_to_right]
        self.pl_y = self.pl.rect.centery + 53
        self.act = self.pl.rect.centerx > self.rect.centerx
        self.move_number = ((self.rect.centerx - self.pl_x)**2 + (self.rect.bottom - self.pl_y)**2)**0.5 / self.speed

        if self.move_number <= self.attack_distance or self.attacking:
            self.attacking = True
            return self.attack
        return self.move

    def attack(self):
        if self.move_number < 1:
            self.rect.midbottom = (self.pl_x, self.pl_y)
        else:
            self.move()
        if self.frame == 40 and pygame.sprite.collide_mask(self, self.pl):
            self.pl.hit_points -= self.damage
        if self.frame == (len(self.animation_list[4]) * 5) - 1:
            self.attacking = False
        return self.animation_list[self.act + 3], 5

    def move(self):
        if not self.attacking:
            self.rect = self.rect.move((self.pl_x - self.rect.centerx) // self.move_number, (self.pl_y - self.rect.bottom) // self.move_number)
            return self.animation_list[self.act], 5

    def die(self):
        if self.frame == (len(self.animation_list[5]) * 5) - 1:
            self.kill()
        return self.animation_list[5], 5

    def stay(self):
        return self.animation_list[2], 5
