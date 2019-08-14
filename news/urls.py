from django.urls import path
from . import views

urlpatterns = [

    path('', views.newz,name='newz'),
    path('cricket/', views.cricket,name='cricket'),
    path('entertainment/', views.entertainment,name='entertainment'),
    path('technology/', views.technology,name='technology'),
    path('science/', views.science,name='science'),
    path('business/', views.business,name='business'),

]