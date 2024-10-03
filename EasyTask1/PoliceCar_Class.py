
class PoliceCar:
    def __init__(self, speed, color, name):
        self.Speed = speed
        self.Color = color
        self.Name = name
        self.Is_police = True

    def go(self):
        print("Тапку в пол!!!")

    def stop(self):
        print("Дал ручника!!!")

    def turn(self, direction):
        if direction == "left":
            print("Дрифт влево!!!")
        if direction == "right":
            print("Дрифт вправо!!!")


