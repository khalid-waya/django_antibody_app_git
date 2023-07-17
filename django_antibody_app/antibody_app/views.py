from django.shortcuts import render
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
    fluorophore_form = FluorophoreForm()
    metal_tag_form = MetalTagForm()
    other_tag_form = OtherTagForm()

    if request.method == 'POST':
        form = antibodyForm(request.POST)
        if form.is_valid():
            print('This is checked')
            form.save()
            return JsonResponse({'success': True})

    else:
       form = antibodyForm()
    return  render(request, 'create_antibody.html', {
        'form': form,
        'fluorophore_form': fluorophore_form,
        'metal_tag_form': metal_tag_form,
        'other_tag_form': other_tag_form
    })

def add_fluorophore(request):
    if request.method == 'POST':
        form = FluorophoreForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = FluorophoreForm()

    return JsonResponse({'html': form.as_p()})

def add_metal_tag(request):
    if request.method == 'POST':
        form = MetalTagForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = MetalTagForm()

    return JsonResponse({'html': form.as_p()})

def add_other_tag(request):
    if request.method == 'POST':
        form = OtherTagForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
    else:
        form = OtherTagForm()

    return JsonResponse({'html': form.save_and_render_html()})