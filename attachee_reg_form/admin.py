from re import I
from django.contrib import admin
from .models import Form, Code, Issue

# Register your models here.

admin.site.register(Form)
admin.site.register(Issue)
admin.site.register(Code)