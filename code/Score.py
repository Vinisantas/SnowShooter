import datetime
import sys
from tkinter.font import Font
import pygame
from code.DBProxy import DBProxy
from code.Const import C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS


class Score:

    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/ScoreBg.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(text_size=48, text='YOU WINN!!', text_color=C_YELLOW, text_center_pos=SCORE_POS['Title'])
            text = 'Enter Player 1 name (4 characters):'
            score = player_score[0]
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player 1 enter name(4 characteres):'
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1] ) / 2
                text = 'Enter Team name(4 characteres):'
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    text = 'Enter Player 1 name(4 characteres):'
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name(4 characteres):'
            self.score_text(text_size=20, text=text , text_color=C_WHITE, text_center_pos=SCORE_POS['Entername'])
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(text_size=20, text=name , text_color=C_WHITE, text_center_pos=SCORE_POS['Name'])
            pygame.display.flip()
            pass


    def show(self):
        pygame.mixer_music.load('./asset/Score.mp3')
        pygame.mixer_music.play(-1)
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(text_size=48, text='TOP 10 SCORE', text_color=C_YELLOW, text_center_pos=SCORE_POS['Title'])
        self.score_text(text_size=20, text='NAME     SCORE            DATE ', text_color=C_YELLOW, text_center_pos=SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(text_size=20, text=f'{name}     {score :05d}            {date}', text_color=C_YELLOW,
                        text_center_pos=SCORE_POS[list_score.index(player_score)])

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit() 
                if event.type ==  pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return                           
            pygame.display.flip()
            

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
