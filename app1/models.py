# -*- coding: utf-8 -*- 
from django.db import models

class Student(models.Model):
    name = models.CharField(u"名字",max_length=100)
    birthday = models.DateTimeField(u"生日")
    sex = models.BooleanField(u"性别")
