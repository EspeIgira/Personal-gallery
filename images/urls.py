from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.gallery,name = 'gallery'),  
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)