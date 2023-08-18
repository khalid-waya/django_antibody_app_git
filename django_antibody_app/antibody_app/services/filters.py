import django_filters
from antibody_app.models import Antibody, Panel

class AntibodyFilter(django_filters.FilterSet):
    class Meta:
        model = Antibody
        fields = {
            'name': ['icontains'],
            'target_antigen': ['icontains'],
            'host_species': ['exact'],
            'reactivities': ['exact']
        }

class PanelFilter(django_filters.FilterSet):
    class Meta:
        model = Panel
        fields = {
            'panel_name': ['icontains']
        }