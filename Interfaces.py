from Widgets import *
import Textures


class Pause:
    def __init__(self, xoy, textures=Textures.Textures()):
        self.background = BackGround(textures.pause['background'][0], xoy)
        self.button_menu = Button(textures.pause['button_menu'], xoy)
        self.button_setting = Button(textures.pause['button_setting'], (xoy[0], xoy[1] + 80 * textures.resizer))

    def create_surface(self):
        return Surface(self.background, self.button_menu, self.button_setting)


class Menu:
    def __init__(self, xoy, textures=Textures.Textures()):
        self.background = BackGround(textures.main_menu['background'][0], xoy)
        self.button_start = Button(textures.main_menu['button_start'], (xoy[0] - 530 * textures.resizer, xoy[1] - 450 * textures.resizer))
        self.button_load = Button(textures.main_menu['button_loading'], ( self.button_start.rect.x + 200 * textures.resizer, self.button_start.rect.y + self.button_start.rect[3] + 40 * textures.resizer))
        self.button_online = Button(textures.main_menu['button_online'], (
            self.button_start.rect.x + 200 * textures.resizer, self.button_start.rect.y + self.button_start.rect[3] + 115 * textures.resizer))
        self.button_setting = Button(textures.main_menu['button_setting'], (
            self.button_start.rect.x + 200 * textures.resizer, self.button_start.rect.y + self.button_start.rect[3] + 190 * textures.resizer))
        self.button_exit = Button(textures.main_menu['button_exit'], (
            self.button_start.rect.x + 200 * textures.resizer, self.button_start.rect.y + self.button_start.rect[3] + 265 * textures.resizer))

    def create_surface(self):
        return Surface(self.background, self.button_start, self.button_load, self.button_online, self.button_setting, self.button_exit)


class PopupMenu:
    def __init__(self, xoy, textures=Textures.Textures()):
        self.background = BackGround(textures.popup_menu['label'], xoy)

    def create_surface(self):
        return Surface(self.background)
