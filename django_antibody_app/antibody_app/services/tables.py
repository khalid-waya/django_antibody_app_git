# tables.py

import django_tables2 as tables
from django.utils.html import format_html
from django_tables2 import A

from antibody_app.models import Antibody, Panel

class CustomCheckboxColumn(tables.CheckBoxColumn):
    def render(self, value, record, bound_column):
        self.attrs['type'] = 'checkbox'
        self.attrs['value'] =  record.ab_instance_id # Assuming 'id' is the primary key of the Antibody model
        return super().render(value, record, bound_column)

class AntibodyTable(tables.Table):
    checkbox = CustomCheckboxColumn(accessor='ab_instance_id', orderable=False)

    update = tables.LinkColumn(
        'update_reactivity',
        args=[A("ab_instance_id")],
        text="Update Reactivity",


    )
    class Meta:
        model = Antibody
        template_name = "django_tables2/bootstrap.html"
        fields = ( 'checkbox','name', 'target_antigen', 'host_species', 'ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag', 'supplier', 'catalogue_num', 'reactivities')

class PanelTable(tables.Table):
    update = tables.LinkColumn(
        'update_panel',
        args=[A("panel_id")],
        text="Update Panel",

    )
    class Meta:
        model = Panel
        templates: "django_tables2/bootstrap.html"
        fields = ("panel_name", "owner", "is_public", "application", "antibodies")


