from django import forms

from .models import *

class antibodyForm(forms.ModelForm):
    class Meta:
        model = Antibody
        fields = ['ab_instance_id', 'name', 'target_antigen', 'host_species','ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag','supplier','catalogue_num']




