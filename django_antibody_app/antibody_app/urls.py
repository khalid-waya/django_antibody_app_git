from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('create_antibody/', views.create_antibody, name='create_antibody'),
    path('add_fluorophore/', views.add_fluorophore, name='add_fluorophore'),
    path('add_metal_tag/', views.add_metal_tag, name = 'add_metal_tag'),
    path('add_other_tag/', views.add_other_tag, name = 'add_other_tag'),
    path('upload_excel/', views.upload_excel, name = 'upload_excel'),
    path('antibody_table/', views.antibody_table, name = 'antibody_table'),
    path('update-reactivity/', views.update_reactivity, name='update_reactivity')


]

