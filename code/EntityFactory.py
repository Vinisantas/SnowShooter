from code.background import Background


class EntityFactory:

    @staticmethod
    def get_Entit(entity_name: str, position=(0,0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(7):
                    list_bg.append(Background(f'Level1Bg{i}', position=(0, 0)))
                    return list_bg
            
