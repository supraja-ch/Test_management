from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.forms.models import model_to_dict
from task.models import *
from rest_framework import status
from django_mailbox.models import MessageAttachment, Message
import base64

#Create your views here.
class task_data(APIView):
	def get(self,request):
		task_obj = Task_Details.objects.all()
		data = list(task_obj.values())
		return JsonResponse(data, safe=False)

	def post(self,request):
		task_id = request.GET.get('id', None)
		update_info = request.GET.get("update_info", None)
		employee_id = request.GET.get('employee_id', None)
		task = Task_Details.objects.create(task_id=task_id,update_info=update_info,employee_id=employee_id)
		task.save()
		return Response(status=status.HTTP_200_OK)

class get_task_details(APIView):
	def get(self,request):
		task_obj = Task.objects.all()
		data = list(task_obj.values())
		return JsonResponse(data, safe=False)

	def post(self,request):
		task_id = request.GET.get('id', None)
		task_name = request.GET.get("task_name", None)
		task_description = request.GET.get('task_description', None)
		start_date = request.GET.get('start_date', None)
		end_date = request.GET.get('end_date', None)
		url = request.GET.get('url', None)
		task_status = True

		task = Task.objects.create(task_id=task_id,task_name=task_name,task_description=task_description,
								start_date=start_date,end_date=end_date,url=url,task_status=task_status)
		task.save()
		return Response(status=status.HTTP_200_OK)



class mail_task_details(APIView):
	def get(self,request):
		msg_obj  = Message.objects.all()
		data = list(msg_obj.values())
		return Response(data,status=status.HTTP_200_OK)

	def post(self,request):
		msg_obj  = Message.objects.all()
		task_status = True
		for msgs in msg_obj:
			var = base64.b64decode(msgs.body)
			data = var.decode('ascii')
			Task.objects.get_or_create(task_id=msgs.id,task_name=msgs.subject,task_description=data,task_status=task_status)
		return Response(status=status.HTTP_200_OK)