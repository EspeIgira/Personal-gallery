from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),  
    # url(r'^image/(\d+)',views.image,name ='image')
]


