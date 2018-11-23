#  This Module contains all the Video class description

from .. import DataBaseLayer


# Custom made Book class (model) not using Django ORM at all, contains attributes and functions
# This model communicates with the database through the DataBaseLayer module
class Video:
    video_id: int = -1
    title: str
    director: str
    producers: str
    actors: str
    language: str
    subtitles: str
    dubbed: str
    release_date: str
    run_time: str

    def __init__(self):
        pass

    def fillingvideoitem(self, id, title, director, producers, actors, language, subtitles, dubbed, release_date, run_time):

        self.video_id = id  # Known placeholder until given an id out of database
        self.title = title
        self.director = director
        self.producers = producers
        self.actors = actors
        self.language = language
        self.subtitles = subtitles
        self.dubbed = dubbed
        self.release_date = release_date
        self.run_time = run_time

    # Example function
    def is_loanable(self):
            return "Yes"

    # A model is responsible for knowing how to store itself in the database( by use of DataBaseLayer module )
    # Save Record
    def store(self):
        insert_query = "INSERT INTO video (title,director,producers,actors,language,subtitles,dubbed,release_date,run_time)VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"%(self.title, self.director, self.producers, self.actors, self.language, self.subtitles, self.dubbed, self.release_date, self.run_time)
        self.video_id = DataBaseLayer.insertCommand(insert_query)

# Retrieve based on Id
    def selectVideofromstore(self, id):
        select_query = "select * from video where id='%d'"% (id)
        tables = DataBaseLayer.selectCommand(select_query)
        return tables[0]

# retrieve record based on Title
    def selectVideobytitlefromstore(self, title,sortBy):
            titlesearch = '%' + title + '%'
            select_query = "SELECT * from video WHERE CONCAT (title,director,actors,language,subtitles,release_date) LIKE '%s'" % (titlesearch)
            if (sortBy != "Random"):
                select_query = select_query + " " + "ORDER BY" + " " + sortBy
            tables = DataBaseLayer.selectCommand(select_query)
            return tables

# Retrieve all records
    def selectAllVideofromstore(self):
        select_query = "select * from video "
        tables = DataBaseLayer.selectCommand(select_query)
        return tables

# Record Update
    def updateVideotostore(self, id):

        update_query = "UPDATE video SET title='%s',director='%s',producers='%s',actors='%s',language='%s',subtitles='%s',dubbed='%s',release_date='%s',run_time='%s' WHERE id = '%s'"%(self.title, self.director, self.producers, self.actors, self.language, self.subtitles, self.dubbed, self.release_date, self.run_time, id)
        self.video_id = DataBaseLayer.updateCommand(update_query)

# Record deletion
    def deleterow(self,id):

        delete_query = "DELETE FROM video WHERE id='%s'"%(id)
        self.video_id = DataBaseLayer.deleteCommand(delete_query)






