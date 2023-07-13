from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import antibodyForm

from .models import Antibody

#jjjsjsjsj


def create_antibody(request):
    if request.method == 'POST':
        form = antibodyForm(request.POST)

        if form.is_valid():
            print('This is checked')
            return render(request, 'myfirst.html', {'form': form})
    else:
       form = antibodyForm()
    return render(request, 'myfirst.html', {'form': form})




# Create your views here.
#