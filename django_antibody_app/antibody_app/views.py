import json
import tempfile
import django_tables2 as tables
from django.forms import modelformset_factory
from django.http import HttpResponseRedirect

from django.shortcuts import render, redirect, get_object_or_404
import os
from antibody_app.services.upload import *
from .forms import antibodyForm, FluorophoreForm, MetalTagForm, OtherTagForm, ExcelUploadForm, AbSpeciesReactivityForms, PanelForm
from antibody_app.services.tables import AntibodyTable, PanelTable
from .models import *
from .services.filters import AntibodyFilter, PanelFilter


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

def upload_excel(request):
    if request.method == 'POST':
        form = ExcelUploadForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                print ("It works")
                # Get the uploaded Excel file from the form
                uploaded_file = request.FILES['excel_file']

                # Create a temporary file to store the uploaded content
                with tempfile.NamedTemporaryFile(suffix='.xlsx', delete=False) as temp_file:
                    for chunk in uploaded_file.chunks():
                        temp_file.write(chunk)

                # Process the uploaded file using the upload.py script
                processUpload(temp_file.name)

                # Delete the temporary file after processing
                os.remove(temp_file.name)

                return redirect('welcome')  # Redirect to the success page or desired URL
            except Exception as e:
                raise Exception(f"Error occurred while uploading data: {e}")
    else:
        form = ExcelUploadForm()

    return render(request, 'upload_excel.html', {'form': form})

def antibody_table(request):
    queryset = Antibody.objects.all()

    try:
        filter = AntibodyFilter(request.GET, queryset=queryset)
        table = AntibodyTable(filter.qs)
        if request.method == 'POST':
            form = PanelForm(request.POST)
            if form.is_valid():
                print("It saved")
                form.save()
                # return redirect('create_panel')
        else:
            form = PanelForm()
    except Exception as e:
        raise Exception(f"Error occured when filtering {e}")
    return render(request, 'antibody_table.html', {'table': table, 'filter': filter, 'form': form})




def update_reactivity(request, ab_instance_id):
    antibody = get_object_or_404(Antibody, pk=ab_instance_id) #obtain the instance of 'antibody' that you wan to update

    #Creates a model formset factory with no extra fields for AbSpeciesReactivity using AbSpeciesReactivityForms
    reactivityform_set = modelformset_factory(AbSpeciesReactivity, form=AbSpeciesReactivityForms, extra=0)

    #Fetch all AbSpeciesReactivity instances for the antibody using the query sert
    qs = antibody.abspeciesreactivity_set.all()


    if request.method == 'POST':

        if 'new-form' in request.POST:
            print("1")
            initial_data = [{'antibody': antibody}]
            reactivityform_set = modelformset_factory(AbSpeciesReactivity, form=AbSpeciesReactivityForms, extra=1)
            qs = antibody.abspeciesreactivity_set.all()

            formset = reactivityform_set(queryset= qs, initial = initial_data)
        elif 'update-form' in request.POST:
            print("2")
            formset = reactivityform_set(request.POST, queryset=qs)
            if formset.is_valid():
                print("3")

                formset.save()
                return redirect('antibody_table')

    else:
        formset = reactivityform_set(queryset=qs)
    return render(request,'update_reactivity.html', {'formset': formset, 'pk': ab_instance_id, 'antibody': antibody})

def delete_reactivity(request, reactivity_id):

        reactivity = get_object_or_404(AbSpeciesReactivity, pk=reactivity_id)
        ab_id = reactivity.antibody.ab_instance_id
        reactivity.delete()

        return redirect(f'/update_reactivity/{ab_id}')


def create_panel (request):
    panel = Panel.objects.all()
    filter = PanelFilter(request.GET, queryset=panel)
    table = PanelTable(filter.qs)

    return render(request, 'create_panel.html', {'table': table, 'filter': filter})