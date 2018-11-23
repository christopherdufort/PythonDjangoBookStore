from django.shortcuts import redirect
from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, AuthenticationForm, BookForm, MagazineForm, VideoForm, MusicForm, BookSearchForm, SearchForm
from .models.BookModule import Book
from . import DataBaseLayer

from .CatalogueModule import Catalogue
from .LoanSystem import LoanSystem
from .UserRegistry import  UserRegistry

# Single Instance of the Catalogue class will be kept
catalogue = Catalogue()
userRegistry = UserRegistry()

# PORTAL CLASS ( Entry Point -> Intermediate step between the Presentation Layer (Template)and the Business Layer)

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        if(request.POST.get('logout') and ('user_id' in request.COOKIES)):
            sql_insert = "UPDATE user SET session_expire = NULL, session_key = NULL WHERE id = '" + str(request.COOKIES.get('user_id') )+"';"
            DataBaseLayer.insertCommand(sql_insert)
            #resp = render(request, 'sign-in.html', {'form': form})
            resp = render(request, 'homepage.html')
            #resp.set_cookie('user_id', ['user_id'])
            resp.delete_cookie('user_id')
            resp.delete_cookie('session_key')
            resp.delete_cookie('email')
            return resp
        auth_form = AuthenticationForm(request.POST)
        if auth_form.is_valid():
            user = UserRegistry.sign_in(auth_form)
            if (user):
                if (user['is_admin']):
                    resp = render(request, 'admin-dashboard.html')
                    resp.set_cookie('user_id', user['id'])
                    resp.set_cookie('session_key', user['session_key'])
                    return resp
                else:
                    resp = render(request, 'homepage.html')
                    resp.set_cookie('user_id', user['id'])
                    resp.set_cookie('session_key', user['session_key'])
                    return resp
        return render(request, 'sign-in.html', {'error': "Incorrect credentials",'form': form})
    return render(request, 'sign-in.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_data = user_form.cleaned_data
            newUser = userRegistry.registerNewUser(user_data,0)
            resp = render(request, 'homepage.html')
            resp.set_cookie('user_id', newUser.user_id)
            resp.set_cookie('email', newUser.email)
            resp.set_cookie('session_key', newUser.session_key)
            print(newUser)
            return resp

    form = UserForm()
    return render(request, 'create-account.html', {'form': form})

def registerNewadministrators(request):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_data = user_form.cleaned_data
            newUser = userRegistry.registerNewUser(user_data,1)
            return render(request, 'admin-dashboard.html')

    form = UserForm()
    return render(request, 'create-account.html', {'form': form})


def client_home(request):
    return render(request, 'homepage.html')


def homepage(request):
    return render(request, 'homepage.html')


# Updated example using the new business logic layer duplicate this for other models
def makeNewBookEntry(request):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_data = book_form.cleaned_data
            catalogue.addItems("book", book_data)
            return redirect(detailedView)
            #HttpResponse("Book added to database")  # Should probably direct to list of all books
    # Request is a 'GET' return an empty form
    book_form = BookForm()
    return render(request, 'book-entry.html', {'form': book_form})


def modifyExistingBookRecord(request,id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        book_form = BookForm()
        book_data = catalogue.get_items("book",id)
        book_form["title"].initial = book_data.title
        book_form["author"].initial = book_data.author
        book_form["book_format"].initial = book_data.book_format
        book_form["pages"].initial = book_data.pages
        book_form["publisher"].initial = book_data.publisher
        book_form["language"].initial = book_data.language
        book_form["isbn_10"].initial = book_data.isbn_10
        book_form["isbn_13"].initial = book_data.isbn_13
        # book_form["id"].initial= book_data.book_id
    elif request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_data = book_form.cleaned_data
            catalogue.modifyitems("book", book_data, id)
            book_form = BookForm()
            return redirect(detailedView)  # Should probably direct to list of all books

    return render(request, 'book-view-update.html', {'form': book_form})


def makeNewMagazineEntry(request):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'POST':
        magazine_form = MagazineForm(request.POST)

        if magazine_form.is_valid():
            magazine_data = magazine_form.cleaned_data
            catalogue.addItems("magazine", magazine_data)
            return redirect(detailedView)


    magazine_form = MagazineForm()
    return render(request, 'magazine-entry.html', {'form': magazine_form})


def modifyExistingMagazineRecord(request,id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        magazine_form = MagazineForm()
        magazine_data = catalogue.get_items("magazine",id)
        magazine_form["title"].initial = magazine_data.title
        magazine_form["publisher"].initial = magazine_data.publisher
        magazine_form["language"].initial = magazine_data.language
        magazine_form["isbn_10"].initial = magazine_data.isbn_10
        magazine_form["isbn_13"].initial = magazine_data.isbn_13

    elif request.method == 'POST':
        magazine_form = MagazineForm(request.POST)
        if magazine_form.is_valid():
            magazine_data = magazine_form.cleaned_data
            catalogue.modifyitems("magazine", magazine_data, id)
            magazine_form = MagazineForm()
            return redirect(detailedView)

    return render(request, 'magazine-view-update.html', {'form': magazine_form})

def makeNewVideoEntry(request):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'POST':
        video_form = VideoForm(request.POST)

        if video_form.is_valid():
            video_data = video_form.cleaned_data
            catalogue.addItems("video", video_data)
            return redirect(detailedView) # Should probably direct to list of all books

    # Request is a 'GET' return an empty form

    video_form = VideoForm()
    return render(request, 'video-entry.html', {'form': video_form})


def modifyExistingVideoRecord(request, id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        video_form = VideoForm()
        video_data = catalogue.get_items("video", id)
        video_form["title"].initial = video_data.title
        video_form["director"].initial = video_data.director
        video_form["producers"].initial = video_data.producers
        video_form["actors"].initial = video_data.actors
        video_form["language"].initial = video_data.language
        video_form["subtitles"].initial = video_data.subtitles
        video_form["dubbed"].initial = video_data.dubbed
        video_form["release_date"].initial = video_data.release_date
        video_form["run_time"].initial = video_data.run_time

    elif request.method == 'POST':
        video_form = VideoForm(request.POST)
        if video_form.is_valid():
            video_data = video_form.cleaned_data
            catalogue.modifyitems("video", video_data,id)
            video_form = VideoForm()
            return redirect(detailedView)

    return render(request, 'video-view-update.html', {'form': video_form})


def makeNewMusicEntry(request):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'POST':
        music_form = MusicForm(request.POST)

        if music_form.is_valid():
            music_data = music_form.cleaned_data
            catalogue.addItems("music", music_data)
            return redirect(detailedView)
    music_form = MusicForm()
    return render(request, 'music-entry.html', {'form': music_form})


def modifyExistingMusicRecord(request, id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        music_form = MusicForm()
        music_data = catalogue.get_items("music", id)
        music_form["title"].initial = music_data.title
        music_form["type"].initial = music_data.type
        music_form["artist"].initial = music_data.artist
        music_form["label"].initial = music_data.label
        music_form["release_date"].initial = music_data.release_date
        music_form["Asin"].initial = music_data.ASIN

    elif request.method == 'POST':
        music_form = MusicForm(request.POST)
        if music_form.is_valid():
            music_data = music_form.cleaned_data
            catalogue.modifyitems("music", music_data, id)
            music_form = MusicForm()
            return redirect(detailedView)

    return render(request, 'music-view-update.html', {'form': music_form})


def admin_dashboard(request):
    if checkIfAdmin(request) == False:
        return render(request, 'homepage.html', {'adminAlert': "admin"})

    return render(request, 'admin-dashboard.html')

def viewLoggedUsers(request):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    #get active users
    users = UserRegistry.viewLoggedUsers()
    return render(request, 'active-users.html',{'users': users})


def deleteExistingBookRecord(request,id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        book_form = BookForm()
        book_data = catalogue.deleteItems("book",id)
    return redirect(detailedView)  # Should probably direct to list of all books


def deleteExistingVideoRecord(request,id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        video_form = VideoForm()
        video_data = catalogue.deleteItems("video", id)
    return redirect(detailedView) # Should probably direct to list of all Videos


def deleteExistingMagazineRecord(request,id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        magazine_form = MagazineForm()
        magazine_data = catalogue.deleteItems("magazine", id)
    return redirect(detailedView)


def deleteExistingMusicRecord(request,id):
    if checkIfAdmin(request) == False:
            return render(request, 'homepage.html', {'adminAlert': "admin"})
    if request.method == 'GET':
        music_form = MusicForm()
        music_data = catalogue.deleteItems("music", id)
    return redirect(detailedView)


def booklist(request):
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_data = search_form.cleaned_data
            book = catalogue.listtitleview("book", search_data.get('Search'))
            return render(request, 'book-list.html', {'form': search_form, 'book': book})

    if request.method == 'GET':
       book = catalogue.detailedView("book")
       return render(request, 'book-list.html', {'form': search_form, 'book': book})

def musiclist(request):
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_data = search_form.cleaned_data
            music = catalogue.listtitleview("music", search_data.get('Search'))
            return render(request, 'music-list.html', {'form': search_form, 'music': music})

    if request.method == 'GET':
      music = catalogue.detailedView("music")
      return render(request, 'music-list.html', {'form': search_form, 'music': music})


def videolist(request):
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_data = search_form.cleaned_data
            video = catalogue.listtitleview("video", search_data.get('Search'))
            return render(request, 'video-list.html', {'form': search_form, 'video': video})

    if request.method == 'GET':
      video = catalogue.detailedView("video")
      return render(request, 'video-list.html', {'form': search_form, 'video': video})


def magazinelist(request):
    search_form = SearchForm()
    if request.method == 'POST':
        search_form = SearchForm(request.POST)
        if search_form.is_valid():
            search_data = search_form.cleaned_data
            magazine = catalogue.listtitleview("magazine", search_data.get('Search'))
            return render(request, 'magazine-list.html', {'form': search_form, 'magazine': magazine})

    if request.method == 'GET':
      magazine = catalogue.detailedView("magazine")
      return render(request, 'magazine-list.html', {'form': search_form, 'magazine': magazine})


def detailedView(request):
    if request.method == 'GET':
        book_data = catalogue.detailedView("book")
        magazine_data = catalogue.detailedView("magazine")
        video_data = catalogue.detailedView("video")
        music_data = catalogue.detailedView("music")
        context = {'books': book_data, 'magazines': magazine_data, 'video': video_data, 'music': music_data}
    return render(request, 'view-All.html', context)


def bookdetails(request, id):
    if request.method == 'GET':
        book_form = BookForm()
        book_data = catalogue.get_items("book", id)
        context = {'b': book_data}
        return render(request, 'book-details.html', context)


def musicdetails(request, id):
    if request.method == 'GET':
        music_form = MusicForm()
        music_data = catalogue.get_items("music", id)
        context = {'b': music_data}
        return render(request, 'music-details.html', context)


def videodetails(request, id):
    if request.method == 'GET':
        video_form = VideoForm()
        video_data = catalogue.get_items("video", id)
        context = {'b': video_data}
        return render(request, 'video-details.html', context)


def magazinedetails(request, id):
        if request.method == 'GET':
            magazine_form = MagazineForm()
            magazine_data = catalogue.get_items("magazine", id)
            context = {'b': magazine_data}
            return render(request, 'magazine-details.html', context)


def catalogview(request):
    if request.method == 'GET':
        book_data = catalogue.detailedView("book")
        magazine_data = catalogue.detailedView("magazine")
        video_data = catalogue.detailedView("video")
        music_data = catalogue.detailedView("music")
        context = {'books': book_data, 'magazines': magazine_data, 'video': video_data, 'music': music_data}
    return render(request, 'catalogue.html', context)

#BOOK SEARCH BY ANY CRITERIA
def booksearch(request):
    search_form = BookSearchForm()
    if request.method == 'POST':
        search_form = BookSearchForm(request.POST)
        print("\nPrint request is: \n")
        print(str(request.POST))
        if search_form.is_valid():
            search_data = search_form.cleaned_data
            print("\nSearch data is\n")
            print(search_data)
            results = catalogue.findBookByAny(search_data)
        return render(request, 'book-searchresults.html', {'form': search_form, 'results': results})
    if request.method == 'GET':
        print("METHOD WENT TO GET IN VIEWS.py/booksearch()")
        return render(request, 'book-search.html', {'form': search_form})


def checkIfAdmin(request):
    sessionKey = request.COOKIES.get('session_key')
    if sessionKey:
        retrieveUserQuery = "SELECT is_admin FROM user WHERE session_key = '%s'"%(sessionKey)
        is_admin = DataBaseLayer.selectCommand(retrieveUserQuery)[0][0]
        if is_admin == 0:
            return False
        return True
    return False

def checkIfClient(request):
    sessionKey = request.COOKIES.get('session_key')
    if sessionKey:
        retrieveUserQuery = "SELECT is_admin FROM user WHERE session_key = '%s'"%(sessionKey)
        is_admin = DataBaseLayer.selectCommand(retrieveUserQuery)[0][0]
        if is_admin == 0:
            return True
        return False
    return False

def loansystem(request):
    if checkIfClient(request) == False:
        return render(request, 'homepage.html', {'clientAlert': "client"})
    return render(request, 'Loan-system.html')


