from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=255) 
    last_name = models.CharField(max_length=255) 
    address = models.CharField(max_length=255) 
    phone_number = models.CharField(max_length=255) 
    is_admin = models.BooleanField(default=False)
    password = models.CharField(max_length=255) 
    email = models.CharField(max_length=255) 
    session_key = models.CharField(max_length=255)
    session_expire = models.DateField(auto_now_add=True, blank=True)

    def authenticate(request, email=None, password=None):
        print("AUTH  CALLED")
        try:
            user = User.objects.get(email=email, password=password)
        except User.DoesNotExist:
            return "user not found"
        except User.MultipleObjectsReturned:
            return "multiple users with this email exist"
        print("User found")
        return user


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    format = models.CharField(max_length=255)
    pages = models.IntegerField(10)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    isbn_10 = models.IntegerField(10)
    isbn_13 = models.IntegerField(13)
    is_loanable = models.BooleanField(default=True)    


class Magazine(models.Model):
    title = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    isbn_10 = models.IntegerField(10)
    isbn_13 = models.IntegerField(13)
    is_loanable = models.BooleanField(default=True) 


class Video(models.Model):
    title = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    producers = models.CharField(max_length=500)#array
    actors = models.CharField(max_length=500)#array
    language = models.CharField(max_length=255)
    subtitles = models.CharField(max_length=255)
    dubbed = models.CharField(max_length=255)
    release_date = models.DateField()
    is_loanable = models.BooleanField(default=True) 


class Music(models.Model):
    title = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    artist = models.CharField(max_length=255)
    label = models.CharField(max_length=255)
    release_date = models.DateField()
    is_loanable = models.BooleanField(default=True) 
    subtitles= models.CharField(max_length=255)
    dubbed=models.CharField(max_length=255)


#join table
class CatalogItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    magazine = models.ForeignKey(Magazine, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
