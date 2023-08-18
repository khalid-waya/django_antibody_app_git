from django import forms
from django.template.loader import render_to_string

from .models import *

class antibodyForm(forms.ModelForm):

    class Meta:
        model = Antibody
        fields = ['ab_instance_id', 'name', 'target_antigen', 'host_species','ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag','supplier','catalogue_num', 'reactivities']
class FluorophoreForm(forms.ModelForm):
    class Meta:
        model = Fluorophore
        fields = ['name', 'absorption_wavelength', 'emission_wavelength', 'excitation_laser', 'visible_color']

class MetalTagForm(forms.ModelForm):
    class Meta:
        model = MetalTag
        fields = ['metal', 'isotope']

class OtherTagForm(forms.ModelForm):

    class Meta:
        model = OtherTag
        fields = ['tag_name']

class ExcelUploadForm(forms.Form):
    excel_file = forms.FileField(label='Upload Excel File', required= False, widget=forms.ClearableFileInput(attrs={'accept': '.xlsx, .xls'}))

class AbSpeciesReactivityForms(forms.ModelForm):

    class Meta:
        model = AbSpeciesReactivity
        fields = ['antibody', 'species_reactivity', 'reactivity_tested']

class PanlForm (forms.ModelForm):
    class Meta:
        model = Panel
