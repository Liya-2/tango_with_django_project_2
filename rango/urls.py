from django.urls import path

from rango import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('', views.index, name='index'),
]