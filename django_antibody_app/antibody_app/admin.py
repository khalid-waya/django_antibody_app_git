from django.contrib import admin
from .models import OtherTag,Fluorophore, MetalTag, AbSpeciesReactivity, Panel

#register your models in heree.
admin.site.register(OtherTag)
admin.site.register(Fluorophore)
admin.site.register(MetalTag)
admin.site.register(AbSpeciesReactivity)
admin.site.register(Panel)

# Register your models here.
