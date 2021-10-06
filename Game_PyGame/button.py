import pygame.font

class Button():
    """Инициализирует кнопку"""
    def __init__(self, start_game, msg, number):
        self.num = number
        self.screen = start_game.screen
        self.screen_rect = self.screen.get_rect()

        self.width, self.height = 200,50
        self.button_color = (0, 0 , 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont("PressStart2PRegular.tff", 48)
         
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        self.rect_inst = pygame.Rect(497, 395, self.width, self.height)
        self.rect_inst.center = (495, 395)

        self.rect_play_inst = pygame.Rect(497, 550, self.width, self.height)
        self.rect_play_inst.center = (490, 550)

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

