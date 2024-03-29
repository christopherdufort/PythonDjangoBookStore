#  This Module contains all the Music class description

from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class Music:
    music_id: int = -1
    title: str
    type: str
    artist: str
    label: str
    release_date: str
    ASIN:str


    def __init__(self):
        pass


    def fillingmusicitem(self, id, title,type,artist,label,release_date,ASIN):

        self.music_id = id  # Known placeholder until given an id out of database
        self.title = title
        self.type = type
        self.artist = artist
        self.label = label
        self.release_date = release_date
        self.ASIN=ASIN


    # Example function
    def is_loanable(self):
            return "Yes"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )

# Save Record
    def store(self):
        # conn = DataBaseLayer.connectDb()
        insert_query = "INSERT INTO music (title,type,artist,label,release_date,ASIN)VALUES('%s', '%s', '%s', '%s', '%s','%s')" % (self.title, self.type, self.artist, self.label, self.release_date,self.ASIN)
        self.music_id = DataBaseLayer.insertCommand(insert_query)

# Update record
    def updateMusictostore(self, id):
        # conn = DataBaseLayer.connectDb()
        update_query = "UPDATE music SET title='%s',type='%s',artist='%s',label='%s',release_date='%s',ASIN='%s' WHERE id = '%s'" % (
            self.title, self.type, self.artist, self.label, self.release_date,self.ASIN, id)
        self.music_id = DataBaseLayer.updateCommand(update_query)

# Retrieve record based on ID
    def selectMusicfromstore(self, id):
        select_query = "select * from music where id='%d'" % (id)
        tables = DataBaseLayer.selectCommand(select_query)
        return tables[0]

# retrieve record based on Title
    def selectMusicbytitlefromstore(self, title,sortBy):
            titlesearch = '%' + title + '%'
            select_query = "SELECT * from music WHERE CONCAT (title,artist,type,release_date,ASIN) LIKE '%s'" % (titlesearch)
            if (sortBy != "Random"):
                select_query = select_query + " " + "ORDER BY" + " " + sortBy
            tables = DataBaseLayer.selectCommand(select_query)
            return tables

# Retrieve all records
    def selectAllMusicfromstore(self):
        select_query = "select * from music "
        tables = DataBaseLayer.selectCommand(select_query)
        return tables

# Delete Record
    def deleterow(self, id):
        # conn = DataBaseLayer.connectDb()
        delete_query = "DELETE FROM music WHERE id='%s'" % (id)
        self.music_id = DataBaseLayer.deleteCommand(delete_query)
