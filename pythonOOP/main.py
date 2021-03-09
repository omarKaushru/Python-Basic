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

    def book_discount(self):
        self.price = self.price - self.price * self.discount


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
print(book_1.price)
book_1.discount = 0.20
book_1.book_discount()
print(book_1.price)
"""
