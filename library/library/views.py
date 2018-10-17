from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def sign_in(request):
    return render(request, 'sign-in.html')

def create_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            print("lamooo is valid")
       
    form = UserForm()
    return render(request, 'create-account.html', {'form': form})

def homepage(request):
    return HttpResponse("home")

