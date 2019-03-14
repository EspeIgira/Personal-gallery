from django.shortcuts import render
from django.http  import HttpResponse



def gallery(request):
    return HttpResponse('Welcome to my Personal gallery')


