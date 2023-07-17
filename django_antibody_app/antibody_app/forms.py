from django import forms
from django.template.loader import render_to_string

from .models import *

class antibodyForm(forms.ModelForm):
    # csv_file = forms.FileField(label='Upload CSV File', required=False)
    class Meta:
        model = Antibody
        fields = ['ab_instance_id', 'name', 'target_antigen', 'host_species','ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag','supplier','catalogue_num']
class FluorophoreForm(forms.ModelForm):
    class Meta:
        model = Fluorophore
        fields = ['name']

    def save_and_render_html(self):
        self.instance = self.save(commit=False)
        html = render_to_string('fluorophore_form.html', {'form': self})
        return html

class MetalTagForm(forms.ModelForm):
    class Meta:
        model = MetalTag
        fields = ['metal']

    def save_and_render_html(self):
        self.instance = self.save(commit=False)
        html = render_to_string('metal_tag_form.html', {'form': self})
        return html

class OtherTagForm(forms.ModelForm):
    class Meta:
        model = OtherTag
        fields = ['tag_name']

    def save_and_render_html(self):
        self.instance = self.save(commit=False)
        html = render_to_string('other_tag_form.html', {'form': self})
        return html


# class CSVUploadForm(forms.Form):
#     csv_file = forms.FileField(label='Upload CSV File', required= False)

