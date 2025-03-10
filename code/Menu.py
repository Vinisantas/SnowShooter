from tkinter.font import Font
from pygame import Rect, Surface
import pygame.image
from code.Const import C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION, WIN_WIDTH


class Menu:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)


    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./asset/Menu.mp3')
        pygame.mixer_music.play(-1)
        while True:
            #DRAW IMAGES AND SELECTED COLOR AND FONTS FOR MENU
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Snow", text_color=C_ORANGE , text_center_pos=((WIN_WIDTH / 2), 70))
            self.menu_text(text_size=50, text="Shooter", text_color=C_ORANGE , text_center_pos=((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(text_size=20, text=MENU_OPTION[i] , text_color=C_YELLOW , text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(text_size=20, text=MENU_OPTION[i] , text_color=C_WHITE , text_center_pos=((WIN_WIDTH / 2), 200 + 25 * i))
            pygame.display.flip()

            #END IMAGES

            #INIT FOR THE EVENTS
            #check for all events e get all
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() #Close Window 
                    quit() #end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: #VERIFY PRESS THE KEY DOWN
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP: #VERIFY PRESS THE KEY UP
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option =  len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN: #VERIFY PRESS THE ENTER
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect) 