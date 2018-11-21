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

	#Search for books by any criteria
    def searchBook(self, title, author, publisher, language, isbn10, isbn13, id, minPages, maxPages):
        print("BookModule.searchBook has been called\nHere are the parameters passed in:\n")        
        print ("title =")
        print (title)
#SOURCE OF ERROR        ALL INTEGERS BEING READ AS 'NONE'   SEE CONCOLE PRINT STATEMENTS    *************************************************************************************************
        print ("ISBN10 =")
        print (isbn10)
        print ("ISBN13 =")
        print (isbn13)
        if title != '':
            title_included = True
        else:
            title_included = False
        if author != '':
            author_included = True
        else:
            author_included = False
        if publisher != '':
            publisher_included = True
        else:
            publisher_included = False
        if language != '':
            language_included = True
        else:
            language_included = False
#SOURCE OF ERROR*************************************************************************************************
        if isbn10 != 'None':
#SOURCE OF ERROR*************************************************************************************************
            isbn10_included = True
            print("BookModule.py line #154 isbn10 has been evaluated as " + str( isbn10_included ))
        else:
            isbn10_included = False
            print("BookModule.py line #157 isbn10 has been evaluated as " + str( isbn10_included ))
        if isbn13 != None:
            isbn13_included = True
        else:
            isbn13_included = False
        if id != None:
            id_included = True
        else:
            id_included = False
        if minPages != None:
            minPages_included = True
        else:
            minPages_included = False 
        if maxPages != None:
            maxPages_included = True
        else:
            maxPages_included = False   
        #PRINT TRUTH VALUES
        print("ISBN10_INCLUDED?" + str(isbn10_included))
        print("ISBN13_INCLUDED?" + str(isbn13_included))  
        print("ID_INCLUDED?" + str(id_included))  
        print("MINPAGES_INCLUDED?" + str(minPages_included))  
        print("MAXPAGES_INCLUDED?" + str(maxPages_included))                
	    #Start Query String
        returnQuery = "SELECT * FROM book where "
        #Add to string necessary components
        if title_included:
            returnQuery += "title LIKE '%%%s%%'"%(title)
            if author_included:
                returnQuery += " AND author LIKE'%%%s%%'"%(author)
            if publisher_included:
                returnQuery += " AND publisher LIKE'%%%s%%'"%(publisher)
            if language_included:
                returnQuery += " AND language LIKE'%%%s%%'"%(language)
            if isbn10_included:
                returnQuery += "AND isbn_10 = " 
                print ("str(isbn10) = ")
                print (str(isbn10))
                print ("isbn10 = ")
                print (isbn10)
                returnQuery += str(isbn10)
            if isbn13_included:
                returnQuery += " AND isbn_13 = "
                returnQuery += str(isbn13)
            if id_included:
                returnQuery += " AND id = "
                returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)      
        elif author_included:
            returnQuery += "author LIKE'%%%s%%'"%(author)
            if publisher_included:
                returnQuery += " AND publisher LIKE'%%%s%%'"%(publisher)
            if language_included:
                returnQuery += " AND language LIKE'%%%s%%'"%(language)
            if isbn10_included:
                returnQuery += "AND isbn_10 = " 
                returnQuery += str(isbn10)
            if isbn13_included:
                returnQuery += " AND isbn_13 = "
                returnQuery += str(isbn13)
            if id_included:
                returnQuery += " AND id = "
                returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)                            
        elif publisher_included:
            returnQuery += "publisher LIKE'%%%s%%'"%(publisher)
            if language_included:
                returnQuery += " AND language LIKE'%%%s%%'"%(language)
            if isbn10_included:
                returnQuery += "AND isbn_10 = " 
                returnQuery += str(isbn10)
            if isbn13_included:
                returnQuery += " AND isbn_13 = "
                returnQuery += str(isbn13)
            if id_included:
                returnQuery += " AND id = "
                returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)                            
        elif language_included:
            returnQuery += "language LIKE'%%%s%%'"%(language) 
            if isbn10_included:
                returnQuery += "AND isbn_10 = " 
                returnQuery += str(isbn10)
            if isbn13_included:
                returnQuery += " AND isbn_13 = "
                returnQuery += str(isbn13)
            if id_included:
                returnQuery += " AND id = "
                returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)
        elif isbn10_included:
            returnQuery += "AND isbn_10 = " 
            returnQuery += str(isbn10)
            if isbn13_included:
                returnQuery += " AND isbn_13 = "
                returnQuery += str(isbn13)
            if id_included:
                returnQuery += " AND id = "
                returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)

        elif isbn13_included:
            returnQuery += " AND isbn_13 = "
            returnQuery += str(isbn13)
            if id_included:
                returnQuery += " AND id = "
                returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)
        elif id_included:
            returnQuery += " AND id = "
            returnQuery += str(id)
            if minPages_included:
                returnQuery += " AND pages > "
                returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)
        elif minPages_included:
            returnQuery += " AND pages > "
            returnQuery += str(minPages)
            if maxPages_included:
                returnQuery += " AND pages < "
                returnQuery += str(maxPages)
        elif maxPages_included:
            returnQuery += " AND pages < "
            returnQuery += str(maxPages)                                                                             
        
        #Send Query String to database
        print (returnQuery)
        return DataBaseLayer.selectCommand(returnQuery)

