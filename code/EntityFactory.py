from code.background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name= str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(0, 0)))
                    list_bg.append(Background(name=f'Level1Bg{i}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player1':
                return Player('Player1', (10, WIN_HEIGHT / 2))
    
            
