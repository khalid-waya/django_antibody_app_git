from django.urls import path
from . import views

urlpatterns = [
    path('antibody_app/', views.my_app, name= 'antibody_app'),
]