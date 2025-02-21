import pygame
from code.Const import MENU_OPTION, WIN_HEIGHT, WIN_WIDTH
from code.Level import Level
from code.Menu import Menu
from code.Score import Score

class Game:
    def __init__(self):
        pygame.init()
        #atribuition of the size for the window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGHT))

    def run(self):
        while True:
            score = Score(self.window)
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return in [MENU_OPTION[0], MENU_OPTION[1], MENU_OPTION[2]]:
                player_score = [0, 0]#[ Player1 , Player2]
                level = Level(self.window,  player_score, name='Level1', game_mode=menu_return)
                level_return = level.run(player_score)
                if level_return: #if level_return TRUE
                    level = Level(self.window, player_score, name='Level2', game_mode=menu_return)
                    level_return = level.run(player_score)
                    if level_return:
                        score.save(menu_return, player_score)


            elif menu_return == MENU_OPTION[3]:
                score.show()
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit()
            else:
                pass
                
