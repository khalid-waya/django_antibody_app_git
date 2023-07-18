from django.shortcuts import render, redirect
import csv
from .models import *

from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.template import loader
from django import forms
from .forms import antibodyForm,  FluorophoreForm, MetalTagForm, OtherTagForm


def welcome (request):
    return render(request, 'welcome_page.html')

def create_antibody(request):
    if request.method == 'POST':
        form = antibodyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')  # Redirect to a success page or the desired URL
    else:
        form = antibodyForm()
        if request.session.keys().__contains__('flu_id'):
            form.fields['fluorophore'].initial = request.session['flu_id']
            del request.session['flu_id']
        if request.session.keys().__contains__('metal_tag_id'):
            form.fields['metal_tag'].initial = request.session['metal_tag_id']
            del request.session['metal_tag_id']
        if request.session.keys().__contains__('other_tag_id'):
            form.fields['other_tag'].initial = request.session['other_tag_id']
            del request.session['other_tag_id']

    return render(request, 'create_antibody.html', {'form': form})

def add_fluorophore(request):
    if request.method == 'POST':
        form = FluorophoreForm(request.POST)
        if form.is_valid():
            flu = form.save()
            request.session['flu_id'] = flu.fluorophore_id

            return redirect('create_antibody')  # Redirect to the welcome page or desired URL
    else:
        form = FluorophoreForm()

    return render(request, 'add_fluorophore_form.html', {'form': form})


def add_metal_tag(request):
    if request.method == 'POST':
        form = MetalTagForm(request.POST)
        if form.is_valid():
            metal = form.save()
            request.session['metal_tag_id'] = metal.metal_tag_id
            return redirect('create_antibody')  # Redirect to the welcome page or desired URL
    else:
        form = MetalTagForm()

    return render(request, 'add_metal_tag_form.html', {'form': form})
def add_other_tag(request):
    if request.method == 'POST':
        form = OtherTagForm(request.POST)
        if form.is_valid():
            other = form.save()
            request.session['other_tag_id'] = other.other_tag_id
            return redirect('create_antibody')  # Redirect to the welcome page or desired URL
    else:
        form = OtherTagForm()

    return render(request, 'add_other_tag_form.html', {'form': form})


