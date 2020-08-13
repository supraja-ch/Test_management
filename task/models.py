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

class category(models.Model):
	category_id = models.AutoField(primary_key=True)
	category_name = models.CharField(max_length=10)

	def __str__(self):
		return '%s' %(self.category_name)

class task_pool(models.Model):
	category = models.ForeignKey(category, on_delete=models.CASCADE)
	# message_attachment_id = models.IntegerField(default=0, null = True)
	msg_attch_id = models.IntegerField(default=0, null = True)
	# mail_box = models.ForeignKey(User, on_delete=models.CASCADE)
	mailbox_id = models.IntegerField(default = 0)
	subject = models.CharField(max_length=500)
	message_id = models.CharField(max_length=500)
	in_reply_to_id = models.IntegerField(default = 0, null = True)
	from_header = models.CharField(max_length=500)
	to_header = models.CharField(max_length=500)
	outgoing = models.BooleanField(default=False)
	body = models.TextField(blank=True,null=True)
	encoded = models.BooleanField(default=False)
	processed = models.DateTimeField(auto_now_add=True)
	read = models.DateTimeField(auto_now_add=True)
	eml = models.TextField(blank=True,null=True)

	def __str__(self):
		return '%s' %(self.mailbox_id)