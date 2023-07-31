from django.contrib import admin
from .models import OtherTag,Fluorophore, MetalTag, AbSpeciesReactivity, AbPanel

#register your models in heree.
admin.site.register(OtherTag)
admin.site.register(Fluorophore)
admin.site.register(MetalTag)
admin.site.register(AbSpeciesReactivity)
admin.site.register(AbPanel)

# Register your models here.
