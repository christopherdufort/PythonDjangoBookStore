#  This Module contains all the Magazine class description

from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class Magazine:
    magazine_id: int = -1
    title: str
    publisher: str
    language: str
    isbn_10: str
    isbn_13: str

    def __init__(self):
        pass

    def fillingmagazineitem(self,id, title, publisher, language, isbn_10, isbn_13):

        self.magazine_id = id  # Known placeholder until given an id out of database
        self.title = title
        self.publisher = publisher
        self.language = language
        self.isbn_10 = isbn_10
        self.isbn_13 = isbn_13

    # Example function
    def is_loanable(self):
            return "No"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )


# Save record
    def store(self):
        # conn = DataBaseLayer.connectDb()
        insert_query = "INSERT INTO magazine (title,publisher,language,isbn_10,isbn_13) VALUES('%s', '%s', '%s', '%s', '%s')" % (self.title, self.publisher, self.language, self.isbn_10, self.isbn_13)
        self.magazine_id = DataBaseLayer.insertCommand(insert_query)
        # Update the id(from database) of the inserted book
        # self.book_id = DataBaseLayer.last_id_inserted()

        # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )

# Update record
    def updateMagazinetostore(self, id):
        # conn = DataBaseLayer.connectDb()
        update_query = "UPDATE magazine SET title='%s',publisher='%s',language='%s',isbn_10='%s',isbn_13='%s' WHERE id = '%s'" % (self.title, self.publisher, self.language, self.isbn_10, self.isbn_13, id)
        # update_query="UPDATE book SET title='s',publisher='s',language='s',isbn_10=5,isbn_13=5 WHERE id =10"
        self.magazine_id = DataBaseLayer.updateCommand(update_query)

# retrieve record based on ID
    def selectMagazinefromstore(self, id):
        select_query = "select * from magazine where id='%d'" % (id)
        tables = DataBaseLayer.selectCommand(select_query)
        return tables[0]

# retrieve record based on Title
    def selectMagazinebytitlefromstore(self, title):
            titlesearch = '%' + title + '%'
            select_query = "SELECT * from magazine WHERE CONCAT (title,publisher,language,isbn_10,isbn_13) LIKE '%s'" % (titlesearch)
            tables = DataBaseLayer.selectCommand(select_query)
            return tables

# Retrieve all record
    def selectAllMagazinesfromstore(self):
        select_query = "select * from magazine "
        tables = DataBaseLayer.selectCommand(select_query)
        return tables

# Delete Record
    def deleterow(self, id):
        # conn = DataBaseLayer.connectDb()
        delete_query = "DELETE FROM magazine WHERE id='%s'" % (id)
        self.magazine_id = DataBaseLayer.deleteCommand(delete_query)





