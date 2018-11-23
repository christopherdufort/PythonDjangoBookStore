from django import forms
from datetime import datetime
from datetime import timedelta
from . import DataBaseLayer
import time
import string
import random

# Custom form used for login
class AuthenticationForm(forms.Form):
    email = forms.CharField(max_length=255)
    password = forms.CharField(max_length=255)

# Custom form used for search
class SearchForm(forms.Form):
    Search = forms.CharField(max_length=255)

# Custom form for user creation and user data
class UserForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    address = forms.CharField(max_length=255)
    phone = forms.CharField(max_length=255)
    #is_admin = forms.BooleanField(initial=False)
    password = forms.CharField(max_length=255,widget=forms.PasswordInput)
    email = forms.EmailField(max_length=255)
  
    #session_key = forms.CharField(max_length=255)
    #session_expire = forms.DateTimeField(initial=datetime.now() + timedelta(hours=1))


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
    id = forms.IntegerField(min_value=0000000000000, max_value=9999999999999).hidden_widget


# Custom form for input of magazines
class MagazineForm(forms.Form):
    title = forms.CharField(max_length=255)
    publisher = forms.CharField(max_length=255)
    language = forms.CharField(max_length=255)   # comma separated array
    isbn_10 = forms.IntegerField(min_value=0000000000, max_value=9999999999)
    isbn_13 = forms.IntegerField(min_value=0000000000000, max_value=9999999999999)
    id = forms.IntegerField(min_value=0000000000000, max_value=9999999999999).hidden_widget


# Custom form for input of videos
class VideoForm(forms.Form):
    title = forms.CharField(max_length=255)
    director = forms.CharField(max_length=255)
    producers = forms.CharField(max_length=500)  # comma separated array
    actors = forms.CharField(max_length=500)  # comma separated array
    language = forms.CharField(max_length=255)  # comma separated array
    subtitles = forms.CharField(max_length=255)  # comma separated array
    dubbed = forms.CharField(max_length=255)   # comma separated array
    release_date = forms.CharField(max_length=255)
    run_time = forms.CharField(max_length=255)
    id = forms.IntegerField(min_value=0000000000000, max_value=9999999999999).hidden_widget


# Custom form for input of music
class MusicForm(forms.Form):
    title = forms.CharField(max_length=255)
    type = forms.CharField(max_length=255)
    artist = forms.CharField(max_length=255)   # comma separated array
    label = forms.CharField(max_length=255)
    release_date = forms.DateField()
    Asin=forms.CharField(max_length=255)
    id = forms.IntegerField(min_value=0000000000000, max_value=9999999999999).hidden_widget
    
# Search any or all book criteria
class BookSearchForm(forms.Form):
    title = forms.CharField(max_length=255, required=False)
    author = forms.CharField(max_length=255, required=False)
    minPages = forms.IntegerField(min_value=0, max_value=9999, required=False)
    maxPages = forms.IntegerField(min_value=0, max_value=9999, required=False)
    publisher = forms.CharField(max_length=255, required=False)
    language = forms.CharField(max_length=255, required=False)
    isbn_10 = forms.IntegerField(min_value=0000000000, max_value=9999999999, required=False)
    isbn_13 = forms.IntegerField(min_value=0000000000000, max_value=9999999999999, required=False)
    id = forms.IntegerField(min_value=0000000000000, max_value=9999999999999, required=False)
