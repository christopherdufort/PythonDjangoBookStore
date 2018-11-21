# from LibraryCatalog.library.models.BookModule import Book
from .models.BookModule import Book
from .models.VideoModule import Video
from .models.MagazineModule import Magazine
from .models.MusicModule import Music


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

        if item_type == "magazine":
            magazine = Magazine()
            magazine.fillingmagazineitem(item_data.get('id'),item_data.get('title'), item_data.get('publisher'), item_data.get('language'),
                                         item_data.get('isbn_10'), item_data.get('isbn_13'))
            magazine.store()  # Store self in database
            print(magazine)  # Debug test of correct insertion
            self.magazine_list.append(magazine)

        if item_type == "video":
                video = Video()
                video.fillingvideoitem(item_data.get('id'),item_data.get('title'), item_data.get('director'), item_data.get('producers'),
                                       item_data.get('actors'), item_data.get('language'), item_data.get('subtitles'),
                                       item_data.get('dubbed'), item_data.get('release_date'))
                video.store()
                print(video)
                self.video_list.append(video)

        if item_type == "music":
                music = Music()
                music.fillingmusicitem(item_data.get('id'),item_data.get('title'), item_data.get('type'), item_data.get('artist'), item_data.get('label'),
                                       item_data.get('release_date'),item_data.get('Asin'))
                music.store()
                print(music)
                self.music_list.append(music)


    def update_item(self, item_type, item_data,id):
        if item_type == "book":
            book = Book()
            book.fillingbookitem(item_data.get('id'),item_data.get('title'), item_data.get('author'), item_data.get('book_format'),
                        item_data.get('pages'), item_data.get('publisher'), item_data.get('language'),
                        item_data.get('isbn_10'), item_data.get('isbn_13'))
            book.updateBooktostore(id)  # Store self in database
            print(book)  # Debug test of correct insertion
            self.book_list.append(book)
        if item_type == "video":
                video = Video()
                video.fillingvideoitem(id,item_data.get('title'), item_data.get('director'), item_data.get('producers'),
                                       item_data.get('actors'), item_data.get('language'), item_data.get('subtitles'),
                                       item_data.get('dubbed'), item_data.get('release_date'))
                video.updateVideotostore(id)  # Store self in database
                print(video)  # Debug test of correct insertion
                self.book_list.append(video)

        if item_type == "magazine":
            magazine = Magazine()
            magazine.fillingmagazineitem(id,item_data.get('title'), item_data.get('publisher'), item_data.get('language'),
                                         item_data.get('isbn_10'), item_data.get('isbn_13'))
            magazine.updateMagazinetostore(id)  # Store self in database
            print(magazine)  # Debug test of correct insertion
            self.book_list.append(magazine)

        if item_type == "music":
            music = Music()
            music.fillingmusicitem(id, item_data.get('title'),item_data.get('type'), item_data.get('artist'), item_data.get('label'),
                                   item_data.get('release_date'),item_data.get('Asin'))
            music.updateMusictostore(id)  # Store self in database
            print(music)  # Debug test of correct insertion
            self.book_list.append(music)

    def get_items(self, item_type, id):
        if item_type == "book":
            book = Book()
            table = book.selectBookfromstore(id)
            book.fillingbookitem(table[0], table[1], table[2], table[3], table[4], table[5], table[6], table[7], table[8])
            return book
        if item_type == "video":
           video = Video()
           table = video.selectVideofromstore(id)
           video.fillingvideoitem(id,table[1], table[2], table[3], table[4], table[5], table[6], table[7], table[8])
           return video
        if item_type == "magazine":
            magazine = Magazine()
            table = magazine.selectMagazinefromstore(id)
            magazine.fillingmagazineitem(id,table[1], table[2], table[3], table[4], table[5])
            return magazine
        if item_type == "music":
           music = Music()
           table = music.selectMusicfromstore(id)
           music.fillingmusicitem(id,table[1], table[2], table[3], table[4], table[5],table[6])
           return music

    def delete_items(self, item_type, id):
        if item_type == "book":
            book = Book()
            affetedRow = book.deleterow(id)
            return affetedRow
        if item_type == "video":
           video = Video()
           affetedRow = video.deleterow(id)
           return affetedRow
        if item_type == "magazine":
           magazine = Magazine()
           affetedRow = magazine.deleterow(id)
           return affetedRow
        if item_type == "music":
           music = Music()
           affetedRow = music.deleterow(id)
           return affetedRow

    def listview(self, item_type):
       if item_type == "book":
            book_list = []
            book = Book()
            table = book.selectAllBookfromstore()
            for rows in table:
                single = Book()
                single.fillingbookitem(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5],
                                                rows[6], rows[7],rows[8])
                book_list.append(single)

            return book_list
       if item_type == "music":
           music_list = []
           music = Music()
           table = music.selectAllMusicfromstore()
           for rows in table:
               single = Music()
               single.fillingmusicitem(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5],rows[6])
               music_list.append(single)
           return music_list
       if item_type == "magazine":
           magazine_list = []
           magazine = Magazine()
           table = magazine.selectAllMagazinesfromstore()
           for rows in table:
               single = Magazine()
               single.fillingmagazineitem(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5])
               magazine_list.append(single)
           return magazine_list
       if item_type == "video":
           video_list = []
           video = Video()
           table = video.selectAllVideofromstore()
           for rows in table:
               single = Video()
               single.fillingvideoitem(rows[0], rows[1], rows[2], rows[3], rows[4], rows[5],
                                      rows[6], rows[7], rows[8])
               video_list.append(single)
           return video_list










