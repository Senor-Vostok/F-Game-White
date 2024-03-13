import pygame
from Player import Player
import Interfaces
from Textures import Textures
from Machine import World
from Generation import Generation
from Cam_class import Cam
import sys
import os
from win32api import GetSystemMetrics

import Widgets

class Game: #мб потом сюды Game_state_handler прикрутить
    def __init__(self):
        self.width = GetSystemMetrics(0)
        self.height = GetSystemMetrics(1)
        self.center = (self.width // 2, self.height // 2)

        self.screen = pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN, vsync=1)

        self.world_size = 50
        self.barrier = 20
        self.gen_world = Generation(self.world_size, self.screen, self.center) # Получаем массив сгенерированной "земли"
        self.gen_world.generation()
        self.gen_world = self.gen_world.add_barrier(self.barrier)

        self.world_pos_x = (self.world_size + self.barrier) // 2
        self.world_pos_y = (self.world_size + self.barrier) // 2

        self.camera = Cam()  # Создание камеры

        self.world = World(self.screen, self.center, [self.world_pos_x, self.world_pos_y],
                           self.gen_world)  # Инициализация мира (его отображение)
        self.world.create()  # заполнение динамической сетки

        self.player = Player(777)
        self.player.start_point = (self.world.sq2 // 2, self.world.sq1 // 2)
        start_x = self.player.start_point[0]
        start_y = self.player.start_point[1]
        self.player.setup(self.world.great_world[start_x][start_y])  # на старте поселение игрока спавнится в центральной клетке (пустая клетка)

        self.clock = pygame.time.Clock()
        self.open_some = False
        self.flag = True
        self.textures = Textures()

    def players_init(self):
        self.player = Player(777)
        self.player.start_point = (self.world.sq2 // 2, self.world.sq1 // 2)
        start_x = self.player.start_point[0]
        start_y = self.player.start_point[1]
        self.player.setup(self.world.great_world[start_x][start_y])  # на старте поселение игрока спавнится в центральной клетке

    def pygame_init(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        my_font = pygame.font.SysFont('Futura book C', 30)
        self.screen.blit(self.textures.loading, (self.center[0] - 960, self.center[1] - 540))
        pygame.display.update()

    def run(self):
        while True:
            normal = self.clock.tick(60)
            for i in pygame.event.get(
                    [pygame.QUIT, pygame.KEYUP, pygame.KEYDOWN, pygame.MOUSEBUTTONUP, pygame.MOUSEBUTTONDOWN,
                     pygame.MOUSEMOTION]):
                self.camera.event(i)
                if i.type == pygame.KEYDOWN:
                    #  временно так
                    if i.key == pygame.K_1:
                        with open('Protocols', mode='w') as file:
                            w = '\n'.join('\t'.join('|'.join(k) for k in i) for i in self.gen_world.masbiom)
                            file.write(f'm-0-{w}')
                    if i.key == pygame.K_2 and self.flag:
                        self.flag = False
                        os.startfile(rf'{os.getcwd()}\H.py')
                    # временно так
                if i.type == pygame.QUIT:
                    sys.exit()
            self.camera.inter()
            self.camera.speed = self.camera.const_for_speed / (self.clock.get_fps() + 1)
            self.world.draw(self.camera.i, self.camera.move, self.open_some)  # Вырисовываем картинку
            self.screen.blit(self.textures.point, (self.camera.i[0] - 10, self.camera.i[1] - 10))
            self.screen.blit(self.textures.font.render(f'fps: {self.clock.get_fps() // 1}', False, (99, 73, 47)), (30, 30))
            pygame.display.update()


if __name__ == "__main__":
    game = Game()
    game.pygame_init()
    game.players_init()
    game.run()
