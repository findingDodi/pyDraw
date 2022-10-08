import pygame
import conf
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
        self.pencil_color = (0, 0, 0)
        self.brush_size = 1

    def draw(self):
        x, y = pygame.mouse.get_pos()
        if x != self.mouse_pos_x or y != self.mouse_pos_y:
            if self.mouse_pos_x >= 0:
                pygame.draw.line(self.screen, self.pencil_color, (self.mouse_pos_x, self.mouse_pos_y), (x, y), self.brush_size)
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
                    elif event.key == pygame.K_r:
                        self.pencil_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                    elif event.key == pygame.K_PLUS:
                        self.brush_size += 1
                    elif event.key == pygame.K_MINUS:
                        if self.brush_size > 1:
                            self.brush_size -= 1
                    elif event.key == pygame.K_DELETE:
                        self.pencil_color = (255, 255, 255)
                    elif event.key == pygame.K_n:
                        new_screen_width = int(input("Enter new Screen Width: "))
                        new_screen_height = int(input("Enter new Screen Height: "))
                        self.background_rect = pygame.Rect(0, 0, new_screen_width, new_screen_height)
                        self.screen = pygame.display.set_mode((new_screen_width, new_screen_height), 0, 32)
                        self.screen.fill((255, 255, 255), self.background_rect)
                    elif event.key == pygame.K_f:
                        self.screen.fill(self.pencil_color, self.background_rect)
                    elif event.key == pygame.K_s:
                        image_name = input("Enter Filename with extension: ")
                        full_path = "drawings/" + image_name
                        pygame.image.save(self.screen, full_path)
                    elif event.key == pygame.K_l:
                        image_name = input("Enter Filename with extension: ")
                        full_path = "drawings/" + image_name
                        background = pygame.image.load(full_path)
                        self.background_rect = background.get_rect()
                        self.screen = pygame.display.set_mode((self.background_rect[2], self.background_rect[3]), 0, 32)
                        self.screen.blit(background, self.background_rect)
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
