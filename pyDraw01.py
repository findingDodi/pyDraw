import pygame
from config import conf


class PyDraw:

    def __init__(self):
        self.screen = None
        self.background_rect = pygame.Rect(0, 0, conf.SCREEN_SIZE[0], conf.SCREEN_SIZE[1])
        self.is_running = True
        self.time_passed = 0

    def run(self):
        SCREENWIDTH = conf.SCREEN_SIZE[0]
        SCREENHEIGHT = conf.SCREEN_SIZE[1]

        pygame.init()
        pygame.display.set_caption("PyDraw")
        self.screen = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT), 0, 32)
        clock = pygame.time.Clock()
        self.is_running = True

        while self.is_running:
            # limit framespeed to 30fps
            self.time_passed = clock.tick(30)
            self.screen.fill((255, 255, 255), self.background_rect)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.is_running = False

            pygame.display.flip()


my_draw_screen = PyDraw()
my_draw_screen.run()
