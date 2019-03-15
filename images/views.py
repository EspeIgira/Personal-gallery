from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image



# def gallery(request):
#     return HttpResponse('Welcome to my Personal gallery')

def gallery(request):
    return render(request, 'gallery.html')


def images_of_today(request):
    date = dt.date.today()
    images = Image.todays_images()
    return render(request, 'all-images/picture.html', {"date": date,"images":images})


def The_images(request):

    my_images = Image.objects.all()
    return render(request, 'all-images/picture.html', {"my_images":my_images})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"categories": searched_categories})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})      

def image(request,image_id):
    try:
        article = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/picture.html", {"image":image})
