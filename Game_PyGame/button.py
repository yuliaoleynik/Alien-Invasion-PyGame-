import pygame.font

class Button():
    """Инициализирует кнопку"""
    def __init__(self, start_game, msg, number):
        self.num = number
        self.screen = start_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 170,30
        self.button_color = (25,25,112)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("PressStart2P.tff", 40)
         
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.rect_inst = pygame.Rect(497, 395, self.width, self.height)
        self.rect_inst.center = (497, 395)

        self.rect_play_inst = pygame.Rect(497, 620, self.width, self.height)
        self.rect_play_inst.center = (497,620)

        self.prep_msg(msg)

    def prep_msg(self, msg):
        if self.num == 2:
            self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect_inst.center
        elif self.num == 1:
            self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect.center
        elif self.num == 3:
            self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
            self.msg_image_rect = self.msg_image.get_rect()
            self.msg_image_rect.center = self.rect_play_inst.center

    def draw_button(self):
        if self.num == 2:
            self.screen.fill(self.button_color, self.rect_inst)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        elif self.num == 1:
            self.screen.fill(self.button_color, self.rect)
            self.screen.blit(self.msg_image, self.msg_image_rect)
        elif self.num == 3:
            self.screen.fill(self.button_color, self.rect_play_inst)
            self.screen.blit(self.msg_image, self.msg_image_rect)

