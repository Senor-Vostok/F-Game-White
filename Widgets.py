import pygame


class Button(pygame.sprite.Sprite):
    def __init__(self, image, xoy):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.func = None
        self.rect = self.image.get_rect(center=xoy)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))

    def connect(self, func, **args):
        self.func = func(**args)

    def update(self, there):
        if self.rect.colliderect(there[0], there[1], 1, 1) and there[2] and there[3] == 1:
            self.func()


class InteractLabel(pygame.sprite.Sprite):
    def __init__(self, image, xoy):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.text = ""
        # self.font.render(self.text, False, (99, 73, 47))
        self.rect = self.image.get_rect(center=xoy)
        self.font = pygame.font.SysFont("Futura book C", self.rect[3] - 2)
        self.can_write = False

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))
        screen.blit(self.font.render(self.text, False, (99, 73, 47)), (self.rect.x + 2, self.rect.y + 2))

    def update(self, there):
        if not self.rect.colliderect(there[0], there[1], 1, 1) and there[2] and there[3] == 1:
            self.can_write = False
        if self.rect.colliderect(there[0], there[1], 1, 1) and there[2] and there[3] == 1:
            self.can_write = True
        if self.can_write:
            self.Go_write()

    def Go_write(self, command):
        if command == pygame.K_BACKSPACE:
            self.text = self.text[:-1]
        else:
            self.text += str(pygame.key)


class Surface:
    def __init__(self, size, **args):
        self.surface = pygame.Surface(size)
        for i in args:
            self.surface.blit(i, (i.rect.x, i.rect.y))

