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


# Python Composition

class StoryBook:
    # Class Variables
    number_of_books = 0
    discount = 0.05

    def __init__(self, name, price, author_name, author_born, number_of_pages):
        self.name = name
        self.price = price
        self.author_name = author_name
        self.author_born = author_born
        self.number_of_pages = number_of_pages
        self.publishing_year = 2022
        StoryBook.number_of_books += 1

    def get_book_info(self):
        print(f'The book name: {self.name}, Price: {self.price}, Pages: {self.number_of_pages} ')

    def get_author_info(self):
        print(f'Author Name: {self.author_name}, Born: {self.author_born}')

    def apply_discount(self):
        self.price = self.price - self.price * self.discount


class Library:
    def __init__(self, book_list=None):
        if book_list is None:
            self.book_list = []
        else:
            self.book_list = book_list

    def get_all_book(self):
        for book in self.book_list:
            print(f'Title: {book.name}, Author: {book.author_name}, Price: {book.price}')

    def add_book(self, book):
        self.book_list.append(book)

    def remove_book(self, book):
        self.book_list.remove(book)


# creating an instance/object of the StoryBook Class
book_1 = StoryBook('Hamlet', 400, 'Shakespeare', 1564, 500)
book_2 = StoryBook('The Kite Runner', 500, 'Khaled Hosseini', 1980, 371)
book_3 = StoryBook('The Dark Side of mine', 700, 'Md Omar Kaushru', 1994, 1213)

public_library = Library()
public_library.add_book(book_1)
public_library.add_book(book_2)
public_library.add_book(book_3)

public_library.get_all_book()
public_library.remove_book(book_2)
public_library.get_all_book()
"""


# Python Magic Method


class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point2D ({self.x, self.y})'

    def __str__(self):
        return f'Class: Pint2D, ' \
               f'X: {self.x} ' \
               f'Y: {self.y}'


p1 = Point2d(12, 13)
p2 = Point2d(13, 14)

print(p1)
print(p2)
