import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, xoy, name, animation=None):
        pygame.sprite.Sprite.__init__(self)
        self.animation = animation
        self.name = name
        self.image = image[0]
        self.select_image = image[1]
        self.rect = self.image.get_rect(center=xoy)

        self.select = False

        self.second_animation = 0
        self.speed_animation = 80

    def self_animation(self, stadia):
        self.image = self.animation[stadia - 1]

    def draw(self, screen, there):
        self.select = self.rect.colliderect(there[0], there[1], 1, 1)
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.select:
            screen.blit(self.select_image, (self.rect.x, self.rect.y))

    def update(self, synchronous, move, y_n):
        if self.animation:
            stadia = (synchronous // self.speed_animation + 1) % len(self.animation)
            self.self_animation(stadia)

        if y_n:
            self.rect.y += move[1]
            self.rect.x += move[0]
