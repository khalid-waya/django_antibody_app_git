from django import forms

from .models import *

class antibodyForm(forms.ModelForm):
    class Meta:
        model = Antibody
        fields = []
        help_texts= ('Input a valid name and antigen. These are necessary fields.')



