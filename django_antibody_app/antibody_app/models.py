# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Panel(models.Model):
    panel_id = models.AutoField(primary_key=True)
    panel_name = models.CharField(max_length=45)
    owner = models.CharField(max_length=10)
    is_public = models.BooleanField(default= False)
    application = models.CharField(max_length=45, blank=True, null=True)
    antibodies = models.ManyToManyField('Antibody', related_name= 'Panel', through= 'PanelAntibody')

    class Meta:
        managed = False
        db_table = 'panel'

    def __str__(self):
        return f"{self.panel_name}"


class AbSpeciesReactivity(models.Model):
    ab_species_reactivity_id = models.AutoField(primary_key=True)
    antibody = models.ForeignKey('Antibody', models.PROTECT, db_column='antibody')
    species_reactivity = models.ForeignKey('Species', models.PROTECT, db_column='species_reactivity', blank=True, null=True)
    reactivity_tested = models.BooleanField(default= False)

    class Meta:
        managed = False
        db_table = 'ab_species_reactivity'

    def __str__(self):
        return f"{self.antibody} - {self.species_reactivity}"


class Antibody(models.Model):
    ab_instance_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    target_antigen = models.CharField(max_length=45, blank=True, null=True)
    host_species = models.ForeignKey(
        'Species', models.PROTECT,
        db_column='host_species',
        blank=True, null=True,
        limit_choices_to={'can_be_host': 1}
    )
    ab_type = models.CharField(db_column='Ab_type', max_length=15, blank=True, null=True)  # Field name made lowercase.
    isotype = models.CharField(max_length=5, blank=True, null=True)
    clone = models.CharField(max_length=25, blank=True, null=True)
    fluorophore = models.ForeignKey('Fluorophore', models.PROTECT, db_column='fluorophore', blank=True, null=True)
    fluo_txt = models.CharField(max_length=45, blank=True, null=True)
    metal_tag = models.ForeignKey('MetalTag', models.PROTECT, db_column='metal_tag', blank=True, null=True)
    metal_tag_txt = models.CharField(max_length=45, blank=True, null=True)
    other_tag = models.ForeignKey('OtherTag', models.PROTECT, db_column='other_tag', blank=True, null=True)
    other_tag_txt = models.CharField(max_length=45, blank=True, null=True)
    supplier = models.CharField(max_length=45, blank=True, null=True)
    catalogue_num = models.CharField(max_length=45, blank=True, null=True)
    other_details = models.CharField(db_column='other details', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    select_for_panel = models.IntegerField(blank=True, null=True)
    metal = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    reactivities = models.ManyToManyField('Species', related_name= 'antibodies', through= 'AbSpeciesReactivity')


    class Meta:
        managed = False
        db_table = 'antibody'
        unique_together = (('name', 'host_species', 'clone', 'fluorophore'),)

    def __str__(self):
        return self.name
class AntibodyAssay(models.Model):
    ab_assay_id = models.AutoField(primary_key=True)
    assay = models.ForeignKey('Assay', models.PROTECT, db_column='assay')
    antibody = models.ForeignKey(Antibody, models.PROTECT, db_column='antibody')
    ab_dilution = models.CharField(max_length=45, blank=True, null=True)
    ab_assay_notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antibody_assay'
    def __str__(self):
        return self.ab_assay_id

class AntibodyLoading(models.Model):
    idantibody_loading = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    target_antigen = models.CharField(max_length=255, blank=True, null=True)
    ab_type = models.CharField(db_column='Ab_type', max_length=255, blank=True, null=True)  # Field name made lowercase.
    isotype = models.CharField(max_length=255, blank=True, null=True)
    host_species = models.CharField(max_length=20, blank=True, null=True)
    clone = models.CharField(max_length=20, blank=True, null=True)
    fluorophore = models.CharField(max_length=20, blank=True, null=True)
    metal = models.CharField(max_length=255, blank=True, null=True)
    other = models.CharField(max_length=255, blank=True, null=True)
    reactivity1 = models.CharField(max_length=255, blank=True, null=True)
    reactivity1_confirmed = models.CharField(db_column='reactivity1 confirmed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reactivity2 = models.CharField(max_length=255, blank=True, null=True)
    reactivity2_confirmed = models.CharField(db_column='reactivity2 confirmed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reactivity3 = models.CharField(max_length=255, blank=True, null=True)
    reactivity3_confirmed = models.CharField(db_column='reactivity3 confirmed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    reactivity4 = models.CharField(max_length=255, blank=True, null=True)
    reactivity4_confirmed = models.CharField(db_column='reactivity4 confirmed', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    supplier = models.CharField(max_length=255, blank=True, null=True)
    catalog_num = models.CharField(max_length=255, blank=True, null=True)
    also_known_as = models.CharField(db_column='also known as', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    other_details = models.CharField(db_column='other details', max_length=255, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    unique_key = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'antibody_loading'
        unique_together = (('name', 'host_species', 'clone', 'fluorophore'),)

        def __str__(self):
            return self.name


class Assay(models.Model):
    assay_id = models.AutoField(primary_key=True)
    assay_name = models.CharField(max_length=45, blank=True, null=True)
    application = models.CharField(max_length=45, blank=True, null=True)
    lab = models.ForeignKey('Lab', models.PROTECT, db_column='lab', blank=True, null=True)
    successful = models.IntegerField()
    assay_notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'assay'
    def __str__(self):
        return self.assay_name

class Fluorophore(models.Model):
    fluorophore_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    absorption_wavelength = models.IntegerField(blank=True, null=True)
    emission_wavelength = models.IntegerField(blank=True, null=True)
    excitation_laser = models.CharField(max_length=45, blank=True, null=True)
    visible_color = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fluorophore'

    def __str__(self):
        return self.name
class Lab(models.Model):
    lab_id = models.AutoField(primary_key=True)
    lab_name = models.CharField(max_length=100)
    group_leader = models.CharField(max_length=100, blank=True, null=True)
    lab_or_stp = models.CharField(max_length=6, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab'

    def __str__(self):
        return self.lab_name

class MetalTag(models.Model):
    metal_tag_id = models.AutoField(primary_key=True)
    metal = models.CharField(max_length=15)
    isotope = models.IntegerField()
    # isotope_txt = models.CharField(max_length=3, blank=True, null=True)
    # description = models.CharField(max_length=18, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'metal_tag'
        unique_together = (('metal', 'isotope'),)

    def __str__(self):
        return f'{self.isotope}{self.metal}'


class OtherTag(models.Model):
    other_tag_id = models.AutoField(primary_key=True)
    tag_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'other_tag'

    def __str__(self):
        return self.tag_name


class PanelAntibody(models.Model):
    panel_antibody_id = models.AutoField(primary_key=True)
    antibody = models.ForeignKey(Antibody, models.PROTECT, db_column='antibody', blank=True, null=True)
    panel = models.ForeignKey(Panel, models.PROTECT, db_column='panel')
    ab_dilution = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panel_antibody'

    def __str__(self):
        return f"{self.panel} - {self.antibody}"


class PanelAssay(models.Model):
    panel_assay_id = models.AutoField(primary_key=True)
    panel = models.ForeignKey(Panel, models.PROTECT, db_column='panel', blank=True, null=True)
    assay = models.ForeignKey(Assay, models.PROTECT, db_column='assay', blank=True, null=True)
    panel_assay_notes = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panel_assay'


class PanelPublication(models.Model):
    panel_publication_id = models.AutoField(primary_key=True)
    panel = models.ForeignKey(Panel, models.PROTECT, db_column='panel')
    publication_details = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'panel_publication'

    def __str__(self):
        return self.panel

class Species(models.Model):
    species_id = models.AutoField(primary_key=True)
    species_name = models.CharField(unique=True, max_length=45)
    species_abbrev = models.CharField(unique=True, max_length=5, blank=True, null=True)
    can_be_host = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'species'

    def __str__(self):
        return self.species_name


