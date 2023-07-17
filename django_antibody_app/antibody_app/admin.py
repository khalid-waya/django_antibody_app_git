from django.contrib import admin
from .models import OtherTag,Fluorophore, MetalTag

#register your models in heree.
admin.site.register(OtherTag)
admin.site.register(Fluorophore)
admin.site.register(MetalTag)

# Register your models here.
