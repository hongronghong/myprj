from django.contrib import admin
from models import *


class StudentAdmin(admin.ModelAdmin):
    fields = [
        'name', 'birthday','sex'
    ]

    list_display = ('name','birthday','sex')



admin.site.register(Student, StudentAdmin)

class TeacherAdmin(admin.ModelAdmin):
    fields = [
        'name', 'number','sex'
    ]

    list_display = ('name','number','sex')


admin.site.register(Teacher, TeacherAdmin)
