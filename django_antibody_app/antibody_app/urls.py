from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('create_antibody/', views.create_antibody, name='create_antibody'),
    path('add_fluorophore/', views.add_fluorophore, name='add_fluorophore'),

]

