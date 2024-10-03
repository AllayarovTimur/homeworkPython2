
class Toy:
    Name = ''
    Color = ''

class Animal(Toy):
    Type = 'Животное'

class Character(Toy):
    Type = 'Персонаж'

class Doll(Toy):
    Type = 'Кукла'

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
        if type == 'Животное':
            animal = Animal()
            animal.Name = name
            animal.Color = color
            animal.Type = type
            return animal
        if type == 'Персонаж':
            character = Character()
            character.Name = name
            character.Color = color
            character.Type = type
            return character
        if type == 'Кукла':
            doll = Doll()
            doll.Name = name
            doll.Color = color
            doll.Type = type
            return doll

toyprod = ToyProduction('Лиса','Рыжий','Кукла')

toyprod.purchase_of_raw_materials()
toyprod.sewing()
toyprod.coloring()
toyprod.release(toyprod.Name, toyprod.Color, toyprod.Type)

