import pygame
from code.Const import WIN_HEIGHT, WIN_WIDTH
from code.Menu import Menu

class Game:
    def __init__(self):
        pygame.init()
        #atribuition of the size for the window
        self.window = pygame.display.set_mode(size=(WIN_WIDTH , WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass



            #check for all events e get all
            #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                    #pygame.quit() #Close Window 
                    #quit() #end pygame




                
