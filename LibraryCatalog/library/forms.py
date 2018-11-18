from django import forms
from datetime import datetime
from datetime import timedelta
from . import DataBaseLayer
import time

# Custom form used for login
class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)


# Custom form for user creation and user data
class UserForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    is_admin = forms.BooleanField(initial=False)
    password = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)
    session_key = forms.CharField(max_length=255)
    #session_expire = forms.DateTimeField(initial=datetime.now() + timedelta(hours=1))

    def save(form):
        print("THIS IS THE FORM TO SAVE")
        session_expire = (datetime.today()+timedelta(days=30))
        conn = DataBaseLayer.connectDb()
        sql = "INSERT INTO `soen341`.`user`(`first_name`, `last_name`, `email`, `address`, `phone_number`, `password`, `session_key`, `session_expire`, `is_admin`) VALUES('";
        sql += form.cleaned_data['first_name'] + "', '"
        sql += form.cleaned_data['last_name'] + "', '"
        sql += form.cleaned_data['email'] + "', '"
        sql += form.cleaned_data['address'] + "', '"
        sql += form.cleaned_data['phone_number'] + "', '"
        sql += form.cleaned_data['password'] + "', '"
        sql += form.cleaned_data['session_key'] + "', '"
        sql += str(session_expire)  + "', '"
        sql += ("1" if form.cleaned_data['is_admin']else "0")+ "');" 
        print("THIS IS THE SQL QUERRY")
        print(sql)
        DataBaseLayer.insertCommand(conn, sql)


# Custom form for admin creation and admin data
class AdminForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    phone_number = forms.CharField(max_length=255)
    is_admin = forms.BooleanField(initial=True)
    password = forms.CharField(max_length=255)
    email = forms.CharField(max_length=255)


# Custom form for input of books
class BookForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
    book_format = forms.CharField(max_length=255)   # comma separated array
    pages = forms.IntegerField(min_value=0, max_value=9999)
    publisher = forms.CharField(max_length=255)
    language = forms.CharField(max_length=255)   # comma separated array
    isbn_10 = forms.IntegerField(min_value=0000000000, max_value=9999999999)
    isbn_13 = forms.IntegerField(min_value=0000000000000, max_value=9999999999999)


# Custom form for input of magazines
class MagazineForm(forms.Form):
    title = forms.CharField(max_length=255)
    publisher = forms.CharField(max_length=255)
    language = forms.CharField(max_length=255)   # comma separated array
    isbn_10 = forms.IntegerField(min_value=0000000000, max_value=9999999999)
    isbn_13 = forms.IntegerField(min_value=0000000000000, max_value=9999999999999)


# Custom form for input of videos
class VideoForm(forms.Form):
    title = forms.CharField(max_length=255)
    director = forms.CharField(max_length=255)
    producers = forms.CharField(max_length=500)  # comma separated array
    actors = forms.CharField(max_length=500)  # comma separated array
    language = forms.CharField(max_length=255)  # comma separated array
    subtitles = forms.CharField(max_length=255)  # comma separated array
    dubbed = forms.CharField(max_length=255)   # comma separated array
    release_date = forms.DateField()


# Custom form for input of music
class MusicForm(forms.ModelForm):
    title = forms.CharField(max_length=255)
    type = forms.CharField(max_length=255)
    artist = forms.CharField(max_length=255)   # comma separated array
    label = forms.CharField(max_length=255)
    release_date = forms.DateField()
