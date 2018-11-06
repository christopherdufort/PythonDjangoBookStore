from django import forms
from .models import User, Book, Magazine, Video, Music



class AuthenticationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','password')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'password', 'phone_number', 'address')


class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=('title','author','format','pages','publisher','language','isbn_10','isbn_13')

class MagazineForm(forms.ModelForm):
    class Meta:
        model=Magazine
        fields=('title','publisher','language','isbn_10','isbn_13')

class VideoForm(forms.ModelForm):
    class Meta:
        model=Video
        fields=('title','director','producers','actors','language','subtitles','dubbed','release_date','is_loanable')

class MusicForm(forms.ModelForm):
    class Meta:
        model=Music
        fields=('title','type','artist','label','release_date','subtitles','dubbed','release_date','is_loanable')