from tkinter.font import Font
from pygame import Rect, Surface
import pygame.image
from code.Const import COLOR_RED, COLOR_WHITE, MENU_OPTION, WIN_WIDTH


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self, ):
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Snow", text_color=COLOR_RED , text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=COLOR_RED , text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=20, text=MENU_OPTION[i] , text_color=COLOR_WHITE , text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))



            pygame.display.flip()

            #check for all events e get all
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window 
                    quit() #end pygame


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect) 