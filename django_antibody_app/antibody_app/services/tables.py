import django_tables2 as tables
from antibody_app.models import Antibody


class AntibodyTable(tables.Table):
    class Meta:
        model = Antibody
        template_name = "django_tables2/bootstrap5.html"
        fields = ('ab_instance_id', 'name', 'target_antigen', 'host_species','ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag','supplier','catalogue_num')


