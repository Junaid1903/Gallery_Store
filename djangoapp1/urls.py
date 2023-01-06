from django.urls import path
from . import views

urlpatterns = [
    path('',views.gallery, name="gallery"),
    path('photo/<str:pk>/',views.viewPhotos,name='photo'),
    path('add/',views.addPhotos,name='add')
]