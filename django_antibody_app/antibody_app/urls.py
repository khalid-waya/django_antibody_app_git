from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('create_antibody', views.create_antibody, name='antibody_app'),

]