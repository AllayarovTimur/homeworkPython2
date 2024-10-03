
class Car:
    def __init__(self, speed, color, name, is_police):
        self.Speed = speed
        self.Color = color
        self.Name = name
        self.Is_police = is_police

    def go(self):
        print("Тапку в пол!!!")

    def stop(self):
        print("Дал ручника!!!")

    def turn(self, direction):
        if direction == "left":
            print("Дрифт влево!!!")
        if direction == "right":
            print("Дрифт вправо!!!")

class PoliceCar(Car):
    def __init__(self, police_lights):
        super().__init__()
        self.Police_lights = police_lights

    def begin_chase(self, target):
        print("Начинаю преследование. Цель: "+target)

class SportCar(Car):
    def __init__(self, max_speed):
        super().__init__()
        self.Max_speed = max_speed

    def begin_race(self, name_of_racer):
        print("Скоро начнется гонка! Гонщик: "+name_of_racer)

class TownCar(Car):
    def __init__(self, price):
        super().__init__()
        self.Price = price

    def begin_drive(self, destination):
        print("Начало поездки. Место назначения: "+destination)

class WorkCar(Car):
    def __init__(self, organization):
        super().__init__()
        self.Organization = organization

    def begin_work(self, work_time):
        print("Начало работы. Оставшееся время работы: "+work_time)