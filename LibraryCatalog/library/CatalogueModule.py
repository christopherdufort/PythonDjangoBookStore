# from LibraryCatalog.library.modelz.BookModule import Book
from .modelz.BookModule import Book


class Catalogue:
    book_list = []
    music_list = []
    video_list = []
    magazine_list = []

    def __init__(self):
        pass

    def add_item(self, item_type, item_data):
        if item_type == "book":
            book = Book(item_data.get('title'), item_data.get('author'), item_data.get('book_format'),
                        item_data.get('pages'), item_data.get('publisher'), item_data.get('language'),
                        item_data.get('isbn_10'), item_data.get('isbn_13'))
            book.store()  # Store self in database
            print(book)  # Debug test of correct insertion
            self.book_list.append(book)
            #return print(book)
        # if item_type == "magazine":
            # Do magazine stuff
        # if item_type == "Video":
            # Do Video stuff
        # if item_type == "music":
            # Do music stuff
