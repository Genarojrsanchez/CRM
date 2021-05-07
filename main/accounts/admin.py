from django.contrib import admin

# Register your models here.
# Pulling from models.py
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Tag)