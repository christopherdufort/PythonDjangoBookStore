#  This Module contains all the Book class description
#from LibraryCatalog.library import DataBaseLayer
from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class Book:
    book_id: int = -1
    title: str
    author: str
    book_format: str
    pages: str
    publisher: str
    language: str
    isbn_10: str
    isbn_13: str


    def __init__(self):
        pass

    # def __init__(self, title, author, book_format, pages, publisher, language, isbn_10, isbn_13):
    #     self.book_id = -1  # Known placeholder until given an id out of database
    #     self.title = title
    #     self.author = author
    #     self.book_format = book_format
    #     self.pages = pages
    #     self.publisher = publisher
    #     self.language = language
    #     self.isbn_10 = isbn_10
    #     self.isbn_13 = isbn_13
    #     self.is_loanable = 1  # Always known that a book is loanable 1 = true, 0 = false

    def fillingbookitem(self, id, title, author, book_format, pages, publisher, language,isbn_13, isbn_10):

        self.book_id = id  # Known placeholder until given an id out of database
        self.title = title
        self.author = author
        self.book_format = book_format
        self.pages = pages
        self.publisher = publisher
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13
        #self.is_loanable = 1  # Always known that a book is loanable 1 = true, 0 = false

    def get_title(self):
        return self.title

        # Example function

    def set_title(self, title):
        self.title = title


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
        # conn = DataBaseLayer.connectDb()
        insert_query = "INSERT INTO book (title,author,format,pages,publisher,language,isbn_10,isbn_13)VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(self.title, self.author, self.book_format, self.pages, self.publisher, self.language, self.isbn_10, self.isbn_13)
        self.book_id = DataBaseLayer.insertCommand(insert_query)
        # Update the id(from database) of the inserted book
        #self.book_id = DataBaseLayer.last_id_inserted()

        # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )

    def updateBooktostore(self, id):
        # conn = DataBaseLayer.connectDb()
        update_query = "UPDATE book SET title='%s',author='%s',format='%s',pages='%s',publisher='%s',language='%s',isbn_10='%s',isbn_13='%s' WHERE id = '%s'"%(self.title, self.author, self.book_format, self.pages, self.publisher, self.language, self.isbn_10,self.isbn_13,id)
        # update_query="UPDATE book SET title='s',author='s',format='s',pages=5,publisher='s',language='s',isbn_10=5,isbn_13=5 WHERE id =10"
        self.book_id = DataBaseLayer.updateCommand(update_query)
        # Update the id(from database) of the inserted book
        #self.book_id = DataBaseLayer.last_id_inserted()



    def selectBookfromstore(self,id):
        select_query ="select * from book where id='%d'"% (id)
        tables=DataBaseLayer.selectCommand(select_query)
        return tables[0]
        # to_string method
  #  def __str__(self):
   #     return "Book Details: " + str(self.book_id) + ", " + self.title + ", " + self.author + ", " + self.book_format + ", " + str(self.pages) + ", " + self.publisher + ", " + self.language + ", " + str(self.isbn_10) + ", "


 # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )
    def deleterow(self,id):
        # conn = DataBaseLayer.connectDb()
        delete_query = "DELETE FROM book WHERE id='%s'"%(id)
        self.book_id = DataBaseLayer.insertCommand(delete_query)
        # Update the id(from database) of the inserted book
        #self.book_id = DataBaseLayer.last_id_inserted()
