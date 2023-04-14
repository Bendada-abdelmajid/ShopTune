from django.contrib import admin
from .models import Ordedr, OrdedrItem, OrdedrOption
# Register your models here.
admin.site.register(Ordedr)
admin.site.register(OrdedrItem)
admin.site.register(OrdedrOption)