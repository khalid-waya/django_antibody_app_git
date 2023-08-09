from django import forms
from django.template.loader import render_to_string

from .models import *

class antibodyForm(forms.ModelForm):
    # csv_file = forms.FileField(label='Upload CSV File', required=False)
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

    # def __init__(self, *args, **kwargs):
    #     super( ).__init__(*args, **kwargs)
    #
    #     instance = getattr(self, 'instance', None)
    #
    #
    #
    #     # Check if the form is used for updating an existing record
    #     if instance:
    #         self.fields['antibody'].disabled = True

    class Meta:
        model = AbSpeciesReactivity
        fields = ['antibody', 'species_reactivity', 'reactivity_tested']
    # def __init__(self, *args, **kwargs):
    #     super(AbSpeciesReactivityForms, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields['antibody'].widget.attrs['readonly'] = True
    # def clean_antibody(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         return instance.antibody
    #     else:
    #         return self.clean_antibody['antibody']
    #