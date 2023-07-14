from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import antibodyForm

from .models import Antibody

def welcome (request):
    return render()
def create_antibody(request):
    if request.method == 'POST':
        form = antibodyForm(request.POST)

        if form.is_valid():
            print('This is checked')
            form.save()
            return render(request, 'antibody_form.html', {'form': form})
    else:
       form = antibodyForm()
    return render(request, 'antibody_form.html', {'form': form})




# Create your views here.
#