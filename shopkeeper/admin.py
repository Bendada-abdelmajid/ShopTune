from django.contrib import admin
from .models import categorys,mainCat,subCat, Profile,pruduct, TodoList,Color, Image, Review
# Register your models here.
admin.site.register(categorys)
admin.site.register(Profile)
admin.site.register(pruduct)
admin.site.register(mainCat)
admin.site.register(subCat)
admin.site.register(Image)
admin.site.register(Review)

admin.site.register(TodoList)

