from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Task_Details(models.Model):
	task_updated_id = models.AutoField(primary_key=True)
	task_id = models.IntegerField(default=0)
	update_info = models.CharField(max_length=500)
	updated_at = models.DateTimeField(auto_now_add=True)
	employee_id = models.IntegerField(default=0)

	def __str__(self):
		return '%s' %(self.task_updated_id)

class Task(models.Model):
	task_id = models.IntegerField(default=0)
	task_name = models.CharField(max_length=500)
	task_description = models.CharField(max_length=150)
	start_date = models.DateTimeField(auto_now_add=True)
	end_date = models.DateTimeField(auto_now_add=True)
	url = models.CharField(max_length=500)
	task_status = models.BooleanField(default=False)

	def __str__(self):
		return '%s' %(self.task_id)