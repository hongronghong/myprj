from django.contrib import admin
from models import *


class StudentAdmin(admin.ModelAdmin):
    fields = [
        'name', 'birthday','sex'
    ]

    list_display = ('name','birthday','sex')

admin.site.register(Student, StudentAdmin)
# Register your models here.
