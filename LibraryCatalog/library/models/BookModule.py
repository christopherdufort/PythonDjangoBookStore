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
    def is_loanable(self):
            return "true"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )
    def store(self):
        insert_query = "INSERT INTO book (title,author,format,pages,publisher,language,isbn_10,isbn_13)VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(self.title, self.author, self.book_format, self.pages, self.publisher, self.language, self.isbn_10, self.isbn_13)
        self.book_id = DataBaseLayer.insertCommand(insert_query)

# update record
    def updateBooktostore(self, id):
        # conn = DataBaseLayer.connectDb()
        update_query = "UPDATE book SET title='%s',author='%s',format='%s',pages='%s',publisher='%s',language='%s',isbn_10='%s',isbn_13='%s' WHERE id = '%s'"%(self.title, self.author, self.book_format, self.pages, self.publisher, self.language, self.isbn_10,self.isbn_13,id)
        self.book_id = DataBaseLayer.updateCommand(update_query)
        # Update the id(from database) of the inserted book
        #self.book_id = DataBaseLayer.last_id_inserted()

# retrieve record based on ID
    def selectBookfromstore(self, id):
        select_query = "select * from book where id='%d'"% (id)
        tables = DataBaseLayer.selectCommand(select_query)
        return tables[0]

# retrieve all record
    def selectAllBookfromstore(self,):
        select_query = "select * from book "
        tables = DataBaseLayer.selectCommand(select_query)
        return tables

# delete record
    def deleterow(self, id):
        # conn = DataBaseLayer.connectDb()
        delete_query = "DELETE FROM book WHERE id='%s'"%(id)
        self.book_id = DataBaseLayer.deleteCommand(delete_query)
        
 #Function for searching any book 
    #   - title, author, language                   from forms.BookSearchForm
    #   - findBookByTitle()                         from module/BookModule.py

     def findBookByISBN10(self, search_data):
	    book = Book()
	    print("search input was " + search_data.get('ISBN_Search'))
	    matching_books = book.findBookByISBN10(search_data.get('ISBN_Search'))		
	    return matching_books

    def findBookByAny(self, search_data):
        book = Book()
        #Print all inputs from for to console
        print("CatalogueModule.py.findBookANY - title of search input was " + search_data.get('title'))
        print("CatalogueModule.py.findBookANY - author of search input was " + search_data.get('author'))
        print("CatalogueModule.py.findBookANY - language of search input was " + search_data.get('language'))
        print("CatalogueModule.py.findBookANY - publisher of search input was " + search_data.get('publisher'))
        print("CatalogueModule.py.findBookANY - id search input was ")
        print(search_data.get('id'))
        print("CatalogueModule.py.findBookANY - minPages search input was ")
        print(search_data.get('minPages'))
        print("CatalogueModule.py.findBookANY -  maxPages search input was ")
        print(search_data.get('maxPages'))
        print("CatalogueModule.py.findBookANY -  isbn10 search input was ")
        print(search_data.get('isbn_10'))
        print("CatalogueModule.py.findBookANY -  isbn13 search input was ")
        print(search_data.get('isbn_13'))
        #Assign True to values that are included in the search
        if search_data.get('title') != '':
            title_included = True
        else:
            title_included = False
        if search_data.get('author') != '':
            author_included = True
        else:
            author_included = False
        if search_data.get('publisher') != '':
            publisher_included = True
        else:
            publisher_included = False
        if search_data.get('language') != '':
            language_included = True
        else:
            language_included = False
        #Conditions for filtering search
        #If title included only
        #
        if title_included or author_included or publisher_included or language_included:
            return book.searchBook(search_data.get('title'), search_data.get('author'), search_data.get('publisher'), search_data.get('language'), search_data.get('isbn10'), search_data.get('isbn13'), search_data.get('id'), search_data.get('minPages'), search_data.get('maxPages'))
        else:
            return book.findBookByTitle(search_data.get('titleSearch'))

