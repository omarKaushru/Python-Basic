"""
class Robot:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def move_forward(self):
        print(f'{self.name} is moving forward!')

    def move_backward(self):
        print(f'{self.name} is moving backward!')

    def move_left(self):
        print(f'{self.name} is moving left!')

    def move_right(self):
        print(f'{self.name} is moving right!')


class HouseBot(Robot):
    def __init__(self, name, version, area_covered):
        super().__init__(name, version)

        self.area_covered = area_covered

    def clean(self):
        if self.area_covered > 0:
            print(f'{self.name} is cleaning the house!')
            self.area_covered -= 30
            if self.area_covered < 0:
                self.area_covered = 0
        else:
            print('Can no clean! Please reset the area covered parameter')

    def set_cover_area(self, area):
        if self.area_covered == 0:
            self.area_covered = area
        else:
            print('I can still clean more area!')

    @staticmethod
    def halt():
        print('I am halting......!')


class SchoolBot(HouseBot):
    pass


hBot = HouseBot('hBot', 2.3, 35)
print(hBot.name)
hBot.move_backward()
# schoolBot = SchoolBot('School Bot', 3.4, 45)
# schoolBot.move_right()
hBot.clean()
hBot.halt()


print(help(Robot))

print(help(HouseBot))

print(issubclass(HouseBot, Robot))
print(issubclass(Robot, HouseBot))
print(issubclass(Robot, object))


print(isinstance(hBot, Robot))
print(isinstance(hBot, HouseBot))
print(isinstance(hBot, object))
print(isinstance(Robot, object))
"""


# Python Multiple Inheritance

class Dancer:
    def __init__(self, style):
        self.style = style

    def dance(self):
        print(f'Dancing in {self.style} style')


class Singer:
    def __init__(self, genre):
        self.genre = genre

    def sing(self):
        print(f'Singing {self.genre} music')


class Artist:
    def __init__(self, painting_material):
        self.painting_material = painting_material

    def paint(self):
        print(f'Painting with {self.painting_material}')


class SuperHuman(Dancer, Singer, Artist):
    def __init__(self, style, genre, painting_material, sport):
        Dancer.__init__(self, style)
        Singer.__init__(self, genre)
        Artist.__init__(self, painting_material)
        self.sport = sport

    def play_sport(self):
        print(f'Playing {self.sport}')


s = SuperHuman('Hip-Hop', 'Classical', 'Acrylic', 'Football')
print(s.style)
print(s.genre)
print(s.painting_material)
print(s.sport)
s.sing()
