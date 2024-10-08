# Generated by Django 4.2.3 on 2023-07-11 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antibody_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AbPanel',
            fields=[
                ('panel_id', models.AutoField(primary_key=True, serialize=False)),
                ('panel_name', models.CharField(max_length=45)),
                ('owner', models.CharField(max_length=10)),
                ('is_public', models.IntegerField()),
                ('application', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ab_panel',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AbSpeciesReactivity',
            fields=[
                ('ab_species_reactivity_id', models.AutoField(primary_key=True, serialize=False)),
                ('reactivity_tested', models.IntegerField()),
            ],
            options={
                'db_table': 'ab_species_reactivity',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Antibody',
            fields=[
                ('ab_instance_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('target_antigen', models.CharField(blank=True, max_length=45, null=True)),
                ('ab_type', models.CharField(blank=True, db_column='Ab_type', max_length=15, null=True)),
                ('isotype', models.CharField(blank=True, max_length=5, null=True)),
                ('clone', models.CharField(blank=True, max_length=25, null=True)),
                ('fluo_txt', models.CharField(blank=True, max_length=45, null=True)),
                ('metal_tag_txt', models.CharField(blank=True, max_length=45, null=True)),
                ('other_tag_txt', models.CharField(blank=True, max_length=45, null=True)),
                ('supplier', models.CharField(blank=True, max_length=45, null=True)),
                ('catalogue_num', models.CharField(blank=True, max_length=45, null=True)),
                ('other_details', models.CharField(blank=True, db_column='other details', max_length=255, null=True)),
                ('select_for_panel', models.IntegerField(blank=True, null=True)),
                ('metal', models.CharField(blank=True, max_length=255, null=True)),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('reactivity1', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'antibody',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AntibodyAssay',
            fields=[
                ('ab_assay_id', models.AutoField(primary_key=True, serialize=False)),
                ('ab_dilution', models.CharField(blank=True, max_length=45, null=True)),
                ('ab_assay_notes', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'antibody_assay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AntibodyLoading',
            fields=[
                ('idantibody_loading', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('target_antigen', models.CharField(blank=True, max_length=255, null=True)),
                ('ab_type', models.CharField(blank=True, db_column='Ab_type', max_length=255, null=True)),
                ('isotype', models.CharField(blank=True, max_length=255, null=True)),
                ('host_species', models.CharField(blank=True, max_length=20, null=True)),
                ('clone', models.CharField(blank=True, max_length=20, null=True)),
                ('fluorophore', models.CharField(blank=True, max_length=20, null=True)),
                ('metal', models.CharField(blank=True, max_length=255, null=True)),
                ('other', models.CharField(blank=True, max_length=255, null=True)),
                ('reactivity1', models.CharField(blank=True, max_length=255, null=True)),
                ('reactivity1_confirmed', models.CharField(blank=True, db_column='reactivity1 confirmed', max_length=255, null=True)),
                ('reactivity2', models.CharField(blank=True, max_length=255, null=True)),
                ('reactivity2_confirmed', models.CharField(blank=True, db_column='reactivity2 confirmed', max_length=255, null=True)),
                ('reactivity3', models.CharField(blank=True, max_length=255, null=True)),
                ('reactivity3_confirmed', models.CharField(blank=True, db_column='reactivity3 confirmed', max_length=255, null=True)),
                ('reactivity4', models.CharField(blank=True, max_length=255, null=True)),
                ('reactivity4_confirmed', models.CharField(blank=True, db_column='reactivity4 confirmed', max_length=255, null=True)),
                ('supplier', models.CharField(blank=True, max_length=255, null=True)),
                ('catalog_num', models.CharField(blank=True, max_length=255, null=True)),
                ('also_known_as', models.CharField(blank=True, db_column='also known as', max_length=255, null=True)),
                ('other_details', models.CharField(blank=True, db_column='other details', max_length=255, null=True)),
                ('unique_key', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'antibody_loading',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Assay',
            fields=[
                ('assay_id', models.AutoField(primary_key=True, serialize=False)),
                ('assay_name', models.CharField(blank=True, max_length=45, null=True)),
                ('application', models.CharField(blank=True, max_length=45, null=True)),
                ('successful', models.IntegerField()),
                ('assay_notes', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'assay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fluorophore',
            fields=[
                ('fluorophore_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('absorption_wavelength', models.IntegerField(blank=True, null=True)),
                ('emission_wavelength', models.IntegerField(blank=True, null=True)),
                ('excitation_laser', models.CharField(blank=True, max_length=45, null=True)),
                ('visible_color', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'fluorophore',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('lab_id', models.AutoField(primary_key=True, serialize=False)),
                ('lab_name', models.CharField(max_length=100)),
                ('group_leader', models.CharField(blank=True, max_length=100, null=True)),
                ('lab_or_stp', models.CharField(blank=True, max_length=6, null=True)),
            ],
            options={
                'db_table': 'lab',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MetalTag',
            fields=[
                ('metal_tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('metal', models.CharField(max_length=15)),
                ('isotope', models.IntegerField()),
                ('isotope_txt', models.CharField(blank=True, max_length=3, null=True)),
                ('description', models.CharField(blank=True, max_length=18, null=True)),
            ],
            options={
                'db_table': 'metal_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OtherTag',
            fields=[
                ('other_tag_id', models.AutoField(primary_key=True, serialize=False)),
                ('tag_name', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'other_tag',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PanelAntibody',
            fields=[
                ('panel_antibody_id', models.AutoField(primary_key=True, serialize=False)),
                ('ab_dilution', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'panel_antibody',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PanelAssay',
            fields=[
                ('panel_assay_id', models.AutoField(primary_key=True, serialize=False)),
                ('panel_assay_notes', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'panel_assay',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PanelPublication',
            fields=[
                ('panel_publication_id', models.AutoField(primary_key=True, serialize=False)),
                ('publication_details', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'panel_publication',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('species_id', models.AutoField(primary_key=True, serialize=False)),
                ('species_name', models.CharField(max_length=45, unique=True)),
                ('species_abbrev', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('can_be_host', models.IntegerField()),
            ],
            options={
                'db_table': 'species',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZzAntigenReactivity',
            fields=[
                ('spec_id', models.AutoField(primary_key=True, serialize=False)),
                ('target_antigen', models.CharField(max_length=45)),
                ('species_reactivity', models.PositiveIntegerField()),
                ('specificity_confirmed', models.IntegerField()),
            ],
            options={
                'db_table': 'zz_antigen_reactivity',
                'db_table_comment': 'could also be a polyclonal - this is more about species reactivity, antigen, etc.',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ZzCloneSpeciesReactivity',
            fields=[
                ('clone_species_reactivity_id', models.AutoField(primary_key=True, serialize=False)),
                ('reactivity_tested', models.IntegerField()),
            ],
            options={
                'db_table': 'zz_clone_species_reactivity',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='my_app_database',
        ),
    ]
