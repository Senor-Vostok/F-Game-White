import pygame


class Ground(pygame.sprite.Sprite):
    def __init__(self, image, xoy, name, animation=None):
        pygame.sprite.Sprite.__init__(self)
        self.animation = animation
        self.name = name
        self.image = image
        self.rect = self.image.get_rect(center=xoy)

        self.select = False

        self.second_animation = 0
        self.speed_animation = 80

    def self_animation(self, stadia):
        self.image = self.animation[stadia - 1]

    def draw(self, screen, there):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        if self.rect.colliderect(there[0], there[1], 1, 1):
            screen.blit(pygame.image.load('data/ground/ground_select.png').convert_alpha(), (self.rect.x, self.rect.y))

    def update(self, synchronous, move, y_n):
        if self.animation:
            stadia = (synchronous // self.speed_animation + 1) % len(self.animation)
            self.self_animation(stadia)

        if y_n:
            self.rect.y += move[1]
            self.rect.x += move[0]
