from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, AuthenticationForm, BookForm, MagazineForm, VideoForm, AdminForm, MusicForm
from .models.BookModule import Book
from .DataBaseLayer import insertCommand, updateCommand, selectCommand

from .CatalogueModule import Catalogue
from .LoanSystem import LoanSystem
from .UserRegistry import  UserRegistry

# Single Instance of the Catalogue class will be kept
catalogue = Catalogue()
userRegistry = UserRegistry()

# PORTAL CLASS ( Entry Point -> Intermediate step between the Presentation Layer (Template)and the Business Layer)


def sign_in(request):
    if request.method == 'POST':
        auth_form = AuthenticationForm(request.POST)
        if auth_form.is_valid():
            user = UserRegistry.sign_in(auth_form)
            if (user):
                print("USER EXISTS GO TO CLIENT PAGE")
                print(user)
                if (user['is_admin']):
                    print("go to admin home")
                else:
                    return render(request, 'client-home.html')
    form = AuthenticationForm()
    return render(request, 'sign-in.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            UserForm.save(form)
            return render(request, 'client-home.html')

    form = UserForm()
    return render(request, 'create-account.html', {'form': form})


def client_home(request):
    return render(request, 'client-home.html')


def homepage(request):
    return render(request, 'homepage.html')


# Updated example using the new business logic layer duplicate this for other models
def book_entry(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_data = book_form.cleaned_data
            catalogue.add_item("book", book_data)
            return HttpResponse("Book added to database")  # Should probably direct to list of all books
    # Request is a 'GET' return an empty form
    book_form = BookForm()
    return render(request, 'book-entry.html', {'form': book_form})


def bookviewupdate(request,id):
    if request.method == 'GET':
        book_form = BookForm()
        book_data = catalogue.get_items("book",id)
        book_form["title"].initial = book_data.title
        book_form["author"].initial = book_data.author
        book_form["book_format"].initial = book_data.book_format
        book_form["pages"].initial = book_data.pages
        book_form["publisher"].initial = book_data.publisher
        book_form["language"].initial = book_data.language
        book_form["isbn_13"].initial = book_data.isbn_13
        book_form["isbn_10"].initial = book_data.isbn_10
        # book_form["id"].initial= book_data.book_id
    elif request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_data = book_form.cleaned_data
            catalogue.update_item("book", book_data, id)
            book_form = BookForm()
            return HttpResponse("Book UPDATED to database")  # Should probably direct to list of all books

    return render(request, 'book-view-update.html', {'form': book_form})


def magazine_entry(request):
    if request.method == 'POST':
        magazine_form = MagazineForm(request.POST)

        if magazine_form.is_valid():
            magazine_data = magazine_form.cleaned_data
            catalogue.add_item("magazine", magazine_data)
            return HttpResponse("Magazine added to database")


    magazine_form = MagazineForm()
    return render(request, 'magazine-entry.html', {'form': magazine_form})


def magazineviewupdate(request,id):
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
            catalogue.update_item("magazine", magazine_data, id)
            magazine_form = MagazineForm()
            return HttpResponse("Magazine UPDATED to database")

    return render(request, 'magazine-view-update.html', {'form': magazine_form})

def video_entry(request):
    if request.method == 'POST':
        video_form = VideoForm(request.POST)

        if video_form.is_valid():
            video_data = video_form.cleaned_data
            catalogue.add_item("video", video_data)
            return HttpResponse("Video added to database")  # Should probably direct to list of all books

    # Request is a 'GET' return an empty form

    video_form = VideoForm()
    return render(request, 'video-entry.html', {'form': video_form})


def videoviewupdate(request, id):
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

    elif request.method == 'POST':
        video_form = VideoForm(request.POST)
        if video_form.is_valid():
            video_data = video_form.cleaned_data
            catalogue.update_item("video", video_data,id)
            video_form = VideoForm()
            return HttpResponse("Video UPDATED to database")

    return render(request, 'video-view-update.html', {'form': video_form})


def music_entry(request):
    if request.method == 'POST':
        music_form = MusicForm(request.POST)

        if music_form.is_valid():
            music_data = music_form.cleaned_data
            catalogue.add_item("music", music_data)
            return HttpResponse("Music added to database")
    music_form = MusicForm()
    return render(request, 'music-entry.html', {'form': music_form})


def musicviewupdate(request, id):
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
            catalogue.update_item("music", music_data, id)
            music_form = MusicForm()
            return HttpResponse("Music UPDATED to database")

    return render(request, 'music-view-update.html', {'form': music_form})

def admin_dashboard(request):
    return render(request, 'admin-dashboard.html')

def active_users(request):
    #get active users
    users = UserRegistry.get_active_users()
    print("HEYOOO")
    print(users)
    return render(request, 'active-users.html',{'users': users})

def register_admin(request):
    if request.method == 'POST':
        form = AdminForm(request.POST)
        if form.is_valid():
            first_name = form["first_name"].value()
            last_name = form["last_name"].value()
            address = form["address"].value()
            phone_number = form["phone_number"].value()
            password = form["password"].value()
            email = form["email"].value()

            insertcmd = "INSERT INTO library_user(first_name,last_name,address,phone_number,is_admin,password,email,session_expire,session_key)VALUES('%s','%s','%s','%s',1,'%s','%s','2018-11-19','')" % (
            first_name, last_name, address, phone_number, password, email)
            insertCommand(insertcmd)

            return render(request, 'Admin-home.html')

    form = AdminForm()
    return render(request, 'create-admin.html', {'form': form})


def bookviewdelete(request,id):
    if request.method == 'GET':
        book_form = BookForm()
        book_data = catalogue.delete_items("book",id)
    return HttpResponse("Book Deleted from  database")  # Should probably direct to list of all books


def videoviewdelete(request,id):
    if request.method == 'GET':
        video_form = VideoForm()
        video_data = catalogue.delete_items("video", id)
    return HttpResponse("video Deleted from  database")  # Should probably direct to list of all Videos


def magazineviewdelete(request,id):
    if request.method == 'GET':
        magazine_form = MagazineForm()
        magazine_data = catalogue.delete_items("magazine", id)
    return HttpResponse("magazine Deleted from  database")


def musicviewdelete(request,id):
    if request.method == 'GET':
        music_form = MusicForm()
        music_data = catalogue.delete_items("music", id)
    return HttpResponse("Music Deleted from  database")


def booklist(request):
    if request.method == 'GET':
       book_data = catalogue.listview("book")
       context = {'book': book_data}
    return render(request, 'book-list.html', context)

def musiclist(request):
    if request.method == 'GET':
      music_data = catalogue.listview("music")
      context = {'music': music_data}
    return render(request, 'music-list.html', context)


def videolist(request):
    if request.method == 'GET':
      video_data = catalogue.listview("video")
      context = {'video': video_data}
    return render(request, 'video-list.html', context)


def magazinelist(request):
    if request.method == 'GET':
      magazine_data = catalogue.listview("magazine")
      context = {'magazine': magazine_data}
    return render(request, 'magazine-list.html', context)


def view_All(request):
    if request.method == 'GET':
        book_data = catalogue.listview("book")
        magazine_data = catalogue.listview("magazine")
        video_data = catalogue.listview("video")
        music_data = catalogue.listview("music")
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


