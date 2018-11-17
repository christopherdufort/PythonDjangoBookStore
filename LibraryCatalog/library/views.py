from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, AuthenticationForm, BookForm, MagazineForm, VideoForm, AdminForm
from .models.BookModule import Book
from .DataBaseLayer import  insertCommand,updateCommand,selectCommand

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
            user_data = auth_form.cleaned_data
            user = userRegistry.sign_in(user_data)
            if (user):
                print("USER EXISTS GO TO CLIENT PAGE")
                if (user.is_admin):
                    print("go to admin home")
                else:
                    return render(request, 'client-home.html')
    form = AuthenticationForm()
    return render(request, 'sign-in.html', {'form': form})


def create_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
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
        form = MagazineForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'magazine-entry.html')
    form = MagazineForm()
    return render(request, 'magazine-entry.html', {'form': form})


def video_entry(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'video-entry.html')
    form = VideoForm()
    return render(request, 'video-entry.html', {'form': form})


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
