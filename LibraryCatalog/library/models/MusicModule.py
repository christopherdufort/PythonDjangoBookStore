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
            return "true"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )


    # to_string method
    def __str__(self):
        return "Music Details: "

    def store(self):
        # conn = DataBaseLayer.connectDb()
        insert_query = "INSERT INTO music (title,type,artist,label,release_date,ASIN)VALUES('%s', '%s', '%s', '%s', '%s','%s')" % (self.title, self.type, self.artist, self.label, self.release_date,self.ASIN)
        self.music_id = DataBaseLayer.insertCommand(insert_query)

    def updateMusictostore(self, id):
        # conn = DataBaseLayer.connectDb()
        update_query = "UPDATE music SET title='%s',type='%s',artist='%s',label='%s',release_date='%s',ASIN='%s' WHERE id = '%s'" % (
            self.title, self.type, self.artist, self.label, self.release_date,self.ASIN, id)
        self.music_id = DataBaseLayer.updateCommand(update_query)

    def selectMusicfromstore(self, id):
        select_query = "select * from music where id='%d'" % (id)
        tables = DataBaseLayer.selectCommand(select_query)
        return tables[0]

    def selectAllMusicfromstore(self):
        select_query = "select * from music "
        tables = DataBaseLayer.selectCommand(select_query)
        return tables

    def deleterow(self, id):
        # conn = DataBaseLayer.connectDb()
        delete_query = "DELETE FROM music WHERE id='%s'" % (id)
        self.music_id = DataBaseLayer.insertCommand(delete_query)

    def getmusiclist(self):
        select_query = "select * from music"
        tables = DataBaseLayer.selectCommand(select_query)
        return tables
