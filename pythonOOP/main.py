"""
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

    # class method1

    @classmethod
    def set_discount(cls, new_discount):
        cls.discount = new_discount

    # class method 2
    @classmethod
    def construct_from_string(cls, book_str):
        name, price, author_name, author_born, pages = book_str.split(',')

        return cls(name, price, author_name, author_born, pages)

    # static method
    @staticmethod
    def is_new(publishing_year):
        if publishing_year > 2016:
            print('Yes it is a new book')
        else:
            print('No it is not a new book')


# creating an instance/object of the StoryBook Class
book_1 = StoryBook('Hamlet', 400, 'Shakespeare', 1564, 500)
book_2 = StoryBook('The Kite Runner', 500, 'Khaled Hosseini', 1980, 371)
# book_1.get_book_info()
# book_1.get_author_info()
# book_2.get_book_info()
# book_2.get_author_info()
#
# print(book_1.number_of_books)
# print(book_2.number_of_books)
# print(StoryBook.number_of_books)
# print(book_1.price)
# book_1.book_discount()
book_str = 'Harry Porter, 200, JK Rowling, 1970, 400'
harry_porter = StoryBook.construct_from_string(book_str)
print(harry_porter.name)
print(book_1.price)
print(book_1.discount)
StoryBook.set_discount(0.6)
book_1.apply_discount()
print(book_1.price)

StoryBook.is_new(book_1.publishing_year)
"""


# Python Object Sorting

class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def sort_priority(self):
        return self.price


def print_toy_object(toy_list):
    for obj in toy_list:
        print(f'Toy: {obj.name}, Price: {obj.price}')


toy_1 = Toy('Woody', 100)
toy_2 = Toy('Bus', 400)
toy_3 = Toy('Helicopter', 3000)
toy_4 = Toy('Gun', 80)
toy_5 = Toy('Motor-Cycle', 565)
toys = [toy_1, toy_2, toy_3, toy_4, toy_5]
# using the sort function
# if we reverse = True the sort function will sort in descending order

# toys.sort(key=Toy.sort_priority, reverse=True)
# print_toy_object(toys)

# using sorted function
# sorted_toys = sorted(toys, key=Toy.sort_priority)
#
# print_toy_object(sorted_toys)

# lambda function allows to write a whole function in one line

# result = lambda x, y, z: x + y + z
# print(result(23, 2, 5))

toys_again = [toy_1, toy_2, toy_3, toy_4, toy_5]
# using the lambda function with sort()

toys_again.sort(key=lambda x: x.price)
print_toy_object(toys_again)

# using lambda function with sorted()

sorted_toys = sorted(toys, key=lambda x: x.price, reverse=True)
print_toy_object(sorted_toys)
