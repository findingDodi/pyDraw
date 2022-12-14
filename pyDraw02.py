import pygame
from config import conf
import random


class PyDraw:

    def __init__(self):
        self.screen = None
        self.background_rect = pygame.Rect(0, 0, conf.SCREEN_SIZE[0], conf.SCREEN_SIZE[1])
        self.is_running = True
        self.time_passed = 0
        self.mouse_pressed = False
        self.mouse_pos_x = -1
        self.mouse_pos_y = -1

    def draw(self):
        pencil_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        x, y = pygame.mouse.get_pos()
        # pygame.draw.circle(self.screen, pencil_color, (x, y), 7)
        if x != self.mouse_pos_x or y != self.mouse_pos_y:
            if self.mouse_pos_x >= 0:
                pygame.draw.line(self.screen, pencil_color, (self.mouse_pos_x, self.mouse_pos_y), (x, y), 4)
            self.mouse_pos_x = x
            self.mouse_pos_y = y

    def run(self):
        SCREENWIDTH = conf.SCREEN_SIZE[0]
        SCREENHEIGHT = conf.SCREEN_SIZE[1]

        pygame.init()
        pygame.display.set_caption("PyDraw")
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
        clock = pygame.time.Clock()
        self.is_running = True

        self.screen.fill((255, 255, 255), self.background_rect)

        while self.is_running:
            # limit framespeed to 30fps
            self.time_passed = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_pressed = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouse_pressed = False
                    self.mouse_pos_x = -1
                    self.mouse_pos_y = -1

            if self.mouse_pressed:
                self.draw()

            pygame.display.flip()


my_draw_screen = PyDraw()
my_draw_screen.run()
