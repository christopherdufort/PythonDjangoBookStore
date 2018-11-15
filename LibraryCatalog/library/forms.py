from django import forms
from .models import User, Magazine, Video, Music


class AuthenticationForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'password')


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'phone_number', 'address')


# Custom
class BookForm(forms.Form):
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)
    book_format = forms.CharField(max_length=255)
    pages = forms.IntegerField(min_value=0, max_value=9999)
    publisher = forms.CharField(max_length=255)
    language = forms.CharField(max_length=255)
    isbn_10 = forms.IntegerField(min_value=0000000000, max_value=9999999999)
    isbn_13 = forms.IntegerField(min_value=0000000000000, max_value=9999999999999)


# class BookForm(forms.ModelForm):
#     class Meta:
#         model = Book
#         fields = ('title', 'author', 'format', 'pages', 'publisher', 'language', 'isbn_10', 'isbn_13')


class MagazineForm(forms.ModelForm):
    class Meta:
        model = Magazine
        fields = ('title', 'publisher', 'language', 'isbn_10', 'isbn_13')


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'director', 'producers', 'actors', 'language', 'subtitles', 'dubbed',
                  'release_date', 'is_loanable')


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ('title', 'type', 'artist', 'label', 'release_date', 'is_loanable')


class AdminForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password', 'phone_number', 'address')
