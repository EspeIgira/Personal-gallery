from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images


# def gallery(request):
#     return HttpResponse('Welcome to my Personal gallery')

def gallery(request):
    return render(request, 'gallery.html')

def upload_images(request):

    my_images = Images.objects.all()
    return render(request, 'all-images/picture.html', {"my_images":my_images})


       