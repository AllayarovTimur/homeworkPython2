import random

class Person:
    def __init__(self, health, damage, armor):
        self.Health = health
        self.Damage = damage
        self.Armor = armor

    def damage_count(self, person):
        if person.Armor<=0:
            person.Armor = 1
        damage = self.Damage + 5/person.Armor
        return damage

    def heal(self):
        self.Health+=1
        if self.Health > 20:
            self.Health = 20

class Player(Person):
    def __init__(self, stamina):
        super().__init__(20, 1, 10)
        self.Stamina = stamina

    def attack(self, enemy, damage):
        if enemy.Armor <= 0:
            enemy.Health -= damage
        else:
            enemy.Health -= damage/2
            enemy.Armor -= damage/2


class Enemy(Person):
    def __init__(self, mana):
        super().__init__(20, 1, 10)
        self.Mana = mana

    def attack(self, player, damage):
        if player.Armor <= 0:
            player.Health -= damage
        else:
            player.Health -= damage / 2
            player.Armor -= damage / 2


hero = Player(10)

villain = Enemy(10)

while (hero.Health>0 and villain.Health>0):
    villain.attack(hero, villain.damage_count(hero))
    r1 = random.randint(0,1)
    if r1 == 0:
        hero.attack(villain, hero.damage_count(villain))
    if r1 == 1:
        hero.heal()
    hero.attack(villain, hero.damage_count(villain))
    r2 = random.randint(0, 1)
    if r2 == 0:
        villain.attack(hero, villain.damage_count(hero))
    if r2 == 1:
        villain.heal()

    print('ХП героя: '+ str(hero.Health)+' ' + 'ХП злодея: '+ str(villain.Health))

