from django.shortcuts import render,redirect
from django.http  import HttpResponse
import datetime as dt
from .models import Image,Category



def gallery(request):
    return render(request, 'gallery.html')


def images_of_day(request):
    date = dt.date.today()
    images = Image.objects.all()
    return render(request, 'all-images/todays|_images.html', {"date": date,"images":images})


def image(request,image_id):
    try:
        image = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/images.html", {"image":image})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        name = request.GET.get("category")
        searched_categories = Image.search_by_category(name)
        message = f"{name}"

        return render(request, 'all-images/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})      

