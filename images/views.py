from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


# def gallery(request):
#     return HttpResponse('Welcome to my Personal gallery')

def gallery(request):
    return render(request, 'gallery.html')

def The_images(request):

    my_images = Image.objects.all()
    return render(request, 'all-images/picture.html', {"my_images":my_images})


def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_categories = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-images/search.html',{"message":message})      

def image(request,image_id):
    try:
        article = Image.objects.get(id = image_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"all-images/picture.html", {"image":image})
    