from django.contrib import admin
from django.db.models.query_utils import subclasses
from main.models import *

# Register your models here.

admin.site.register(Sex)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(SubCategory)

