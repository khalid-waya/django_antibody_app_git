import tempfile
from django.shortcuts import render, redirect
import os
from antibody_app.services.upload import *
from .forms import antibodyForm, FluorophoreForm, MetalTagForm, OtherTagForm, ExcelUploadForm
from antibody_app.services.tables import AntibodyTable
from .models import *
# from services import upload

from django.http import HttpResponseRedirect, JsonResponse
from django.http import HttpResponse
from django.template import loader
from django import forms



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
    queryset = Antibody.objects.all()  # Fetch all Antibody objects from the database
    table = AntibodyTable(queryset)  # Create a table instance with the queryset
    return render(request, 'antibody_table.html', {'table': table})