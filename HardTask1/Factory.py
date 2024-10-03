
class Toy:
    Name = ''
    Color = ''
    Type = ''



class ToyProduction:
    def __init__(self, name, color, type):
        self.Name = name
        self.Color = color
        self.Type = type

    def purchase_of_raw_materials(self):
        print('Закупка маетриала')

    def sewing(self):
        print('Пошив игрушки')

    def coloring(self):
        print('Покраска игрушки')

    def release(self,name, color, type):
        toy = Toy()
        toy.Name = name
        toy.Color = color
        toy.Type = type
        return toy


toyprod = ToyProduction('Лиса','Рыжий','Животное')

toyprod.purchase_of_raw_materials()
toyprod.sewing()
toyprod.coloring()
toyprod.release(toyprod.Name, toyprod.Color, toyprod.Type)

