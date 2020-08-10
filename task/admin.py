from django.contrib import admin

#Register your models here.
from .models import *

admin.site.register(Task_Details)
admin.site.register(Task)
admin.site.register(category)
admin.site.register(task_pool)

