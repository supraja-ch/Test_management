from django.contrib import admin

#Register your models here.
from .models import *

admin.site.register(Task_Details)
admin.site.register(Task)
