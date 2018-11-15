#  This Module contains all the Book class description
#from LibraryCatalog.library import DataBaseLayer
from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class Book:
    def __init__(self, title, author, book_format, pages, publisher, language, isbn_10, isbn_13):
        self.book_id = -1  # Known placeholder until given an id out of database
        self.title = title
        self.author = author
        self.book_format = book_format
        self.pages = pages
        self.publisher = publisher
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        self.is_loanable = 1  # Always known that a book is loanable 1 = true, 0 = false

    # Example function
    def get_title(self):
        return self.title

    # Example function
    def set_title(self, title):
        self.title = title

    # Example function
    def is_loanable(self):
            return "true"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )
    def store(self):
        conn = DataBaseLayer.connectDb()
        insert_query = "INSERT INTO library_book (title,author,format,pages,publisher,language,isbn_10,isbn_13,is_loanable) VALUES("+self.title+","+self.author+","+self.book_format+","+str(self.pages)+","+self.publisher+","+self.language+","+str(self.isbn_10)+","+str(self.isbn_13)+","+str(self.is_loanable)"
        DataBaseLayer.insertCommand(conn, insert_query)
        # Update the id(from database) of the inserted book
        self.book_id = DataBaseLayer.last_id_inserted(conn)

    # to_string method
    def __str__(self):
        return "Book Details: " + str(self.book_id) + " " + self.title + " " + self.author + " " + self.book_format + " " + str(self.pages) + " " + self.publisher + " " + self.language + " " + str(self.isbn_10) + " " + str(self.is_loanable)


