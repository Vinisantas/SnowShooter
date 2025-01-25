import pygame

print('setup start')
pygame.init()
#atribuition of the size for the window
window = pygame.display.set_mode(size=(600, 480))

print('setup End')
while True:
    #check for all events e get all
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quiting')
            pygame.quit() #Close Window 
            quit() #end pygame
            
