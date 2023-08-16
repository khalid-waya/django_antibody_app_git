import django_filters
from antibody_app.models import Antibody

class AntibodyFilter(django_filters.FilterSet):
    class Meta:
        model = Antibody
        fields = {
            'name': ['icontains'],
            'target_antigen': ['icontains'],
            'host_species': ['exact'],
            'reactivities': ['exact']
        }