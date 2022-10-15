import pygame
import conf
import random


class PyDraw:

    def __init__(self):
        self.screen = None
        self.screen_width = conf.SCREEN_SIZE[0]
        self.screen_height = conf.SCREEN_SIZE[1]
        self.background_rect = pygame.Rect(0, 0, 0, 0)
        self.is_running = True
        self.time_passed = 0
        self.mouse_pressed = False
        self.mouse_pos_x = -1
        self.mouse_pos_y = -1
        self.pencil_color = (0, 0, 0)
        self.brush_size = 1

    def set_screen_size(self, width, height):
        self.screen_width = width
        self.screen_height = height
        self.background_rect = pygame.Rect(0, 0, self.screen_width, self.screen_height)
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height), 0, 32)
        self.screen.fill((255, 255, 255), self.background_rect)

    def set_fill_screen(self, color=(255, 255, 255)):
        self.screen.fill(color, self.background_rect)

    def save_file(self):
        image_name = input("Enter Filename with extension: ")
        full_path = "drawings/" + image_name
        pygame.image.save(self.screen, full_path)

    def load_file(self):
        image_name = input("Enter Filename with extension: ")
        full_path = "drawings/" + image_name
        background = pygame.image.load(full_path)
        background_rect = background.get_rect()
        self.set_screen_size(background_rect[2], background_rect[3])
        self.screen.blit(background, self.background_rect)

    def draw(self):
        x, y = pygame.mouse.get_pos()
        if x != self.mouse_pos_x or y != self.mouse_pos_y:
            if self.mouse_pos_x >= 0:
                pygame.draw.line(self.screen, self.pencil_color, (self.mouse_pos_x, self.mouse_pos_y), (x, y), self.brush_size)
            self.mouse_pos_x = x
            self.mouse_pos_y = y

    def run(self):
        pygame.init()
        pygame.display.set_caption("PyDraw")
        self.set_screen_size(self.screen_width, self.screen_height)
        self.set_fill_screen()

        clock = pygame.time.Clock()
        self.is_running = True

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
                        self.set_screen_size(new_screen_width, new_screen_height)
                    elif event.key == pygame.K_f:
                        self.set_fill_screen(self.pencil_color)
                    elif event.key == pygame.K_s:
                        self.save_file()
                    elif event.key == pygame.K_l:
                        self.load_file()

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
