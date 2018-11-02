from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm, AuthenticationForm
from .models import User

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

<<<<<<< HEAD
def book_entry(request):
    return render(request, 'book-entry.html')
=======
>>>>>>> 966919996673002a2f4a8513f798ea36977676c6
