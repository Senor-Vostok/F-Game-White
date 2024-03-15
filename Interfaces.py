from Widgets import *
import Textures


class Menu:
    def __init__(self, xoy, textures=Textures.Textures()):
        self.background = BackGround(textures.main_menu['background'][0], xoy)
        self.button_start = Button(textures.main_menu['button_start'], (xoy[0] - 530, xoy[1] - 450))
        self.button_load = Button(textures.main_menu['button_loading'], (self.button_start.rect.x + 200, self.button_start.rect.y + self.button_start.rect[3] + 40))
        self.button_online = Button(textures.main_menu['button_online'], (self.button_start.rect.x + 200, self.button_start.rect.y + self.button_start.rect[3] + 115))
        self.button_setting = Button(textures.main_menu['button_setting'], (self.button_start.rect.x + 200, self.button_start.rect.y + self.button_start.rect[3] + 190))
        self.button_exit = Button(textures.main_menu['button_exit'], (self.button_start.rect.x + 200, self.button_start.rect.y + self.button_start.rect[3] + 265))

    def create_surface(self):
        return Surface(self.background, self.button_start, self.button_load, self.button_online, self.button_setting, self.button_exit)


class PopupMenu:
    def __init__(self, xoy, textures=Textures.Textures()):
        self.background = BackGround(textures.popup_menu['label'], xoy)

    def create_surface(self):
        return Surface(self.background)
