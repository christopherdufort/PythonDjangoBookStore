# from LibraryCatalog.library.models.BookModule import Book
from .models.BookModule import Book


class Catalogue:
    book_list = []
    music_list = []
    video_list = []
    magazine_list = []

    def __init__(self):
        pass

    def add_item(self, item_type, item_data):
        if item_type == "book":
            book = Book()
            book.fillingbookitem(item_data.get('id'),item_data.get('title'), item_data.get('author'), item_data.get('book_format'),
                 item_data.get('pages'), item_data.get('publisher'), item_data.get('language'),
                 item_data.get('isbn_10'), item_data.get('isbn_13'))
            book.store()  # Store self in database
            print(book)  # Debug test of correct insertion
            self.book_list.append(book)

        # if item_type == "magazine":
            # Do magazine stuff
        # if item_type == "Video":
            # Do Video stuff
        # if item_type == "music":
            # Do music stuff


    def update_item(self, item_type, item_data,id):
        if item_type == "book":
            book = Book()
            book.fillingbookitem(item_data.get('id'),item_data.get('title'), item_data.get('author'), item_data.get('book_format'),
                        item_data.get('pages'), item_data.get('publisher'), item_data.get('language'),
                        item_data.get('isbn_10'), item_data.get('isbn_13'))
            book.updateBooktostore(id)  # Store self in database
            print(book)  # Debug test of correct insertion
            self.book_list.append(book)

    def get_items(self, item_type, id):
        if item_type == "book":
            book = Book()
            table = book.selectBookfromstore(id)
            book.fillingbookitem(table[0],table[1],table[2],table[3],table[4],table[5],table[6],table[7],table[8])
        return book

    def delete_items(self, item_type, id):
        if item_type == "book":
            book = Book()
            affetedRow = book.deleterow(id)
        return affetedRow
