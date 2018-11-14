from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, AuthenticationForm, BookForm, MagazineForm, VideoForm,AdminForm
from .models import User, Book, Magazine, Video

from .DataBaseLayer import connectDb,insertCommand,selectCommand

def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = User.authenticate(request, email, password)
            if(user):
                print("USER EXISTS GO TO CLIENT PAGE")
                if(user.is_admin):
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
    return HttpResponse("home")


def book_entry(request):
    if request.method=='POST':
        form=BookForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'book-entry.html')
    form = BookForm()
    return render(request, 'book-entry.html', {'form': form})


def magazine_entry(request):
    if request.method=='POST':
        form=MagazineForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'magazine-entry.html')
    form = MagazineForm()
    return render(request, 'magazine-entry.html', {'form': form})


def video_entry(request):
    if request.method == 'POST':
        form=VideoForm(request.POST)
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

            insertcmd = "INSERT INTO library_user(first_name,last_name,address,phone_number,is_admin,password,email,session_expire,session_key)VALUES('%s','%s','%s','%s',1,'%s','%s','2018-11-19','')" % (first_name, last_name, address, phone_number, password, email)
            insertCommand(connectDb(), insertcmd)

            return render(request, 'Admin-home.html')

    form = AdminForm()
    return render(request, 'create-admin.html', {'form': form})




