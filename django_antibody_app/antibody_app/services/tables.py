# tables.py

import django_tables2 as tables
from django.utils.html import format_html
from django_tables2 import A

from antibody_app.models import Antibody


class AntibodyTable(tables.Table):

    update = tables.LinkColumn(
        'update_reactivity',
        args=[A("ab_instance_id")],
        text="Update Reactivity",


    )
    class Meta:
        model = Antibody
        template_name = "django_tables2/bootstrap.html"
        fields = ( 'name', 'target_antigen', 'host_species', 'ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag', 'supplier', 'catalogue_num', 'reactivities')
