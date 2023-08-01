# tables.py

import django_tables2 as tables
from django.utils.html import format_html
from antibody_app.models import Antibody

class CustomCheckBoxColumn(tables.CheckBoxColumn):
    def header(self):
        return format_html('<input type="checkbox" id="select_all">', self.verbose_name)

    def render(self, value):
        return format_html('<input type="checkbox" name="selection" value="{}">', value)


class AntibodyTable(tables.Table):
    selection = CustomCheckBoxColumn(accessor='pk', orderable=False, verbose_name='Select All Items')

    reactivities = tables.ManyToManyColumn()

    class Meta:
        model = Antibody
        template_name = "django_tables2/bootstrap.html"
        fields = ( 'name', 'target_antigen', 'host_species', 'ab_type', 'isotype', 'clone', 'fluorophore', 'metal_tag', 'other_tag', 'supplier', 'catalogue_num', 'reactivities')
