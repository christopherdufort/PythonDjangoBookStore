from django.http import HttpResponse
from django.shortcuts import render

def sign_in(request):
    return render(request, 'sign-in.html')


def homepage(request):
    return HttpResponse("home")