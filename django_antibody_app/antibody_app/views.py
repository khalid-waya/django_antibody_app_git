from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import antibodyForm

from .models import Antibody

#jjjsjsjsj


# def antibodyApp(request):
#     if request.method == 'POST':
#         form = antibodyForm(request.POST)
#         if form.is_valid():
#             return HttpResponseRedirect("Valid Inputs")
#     else:
#         antibodyForm()
#         return render(request, 'antibody_app/templates/myfirst.html', {'form': antibodyForm})


def my_app(request):
    template = loader.get_template('myfirst.html')
    return HttpResponse(template.render())

# Create your views here.
#