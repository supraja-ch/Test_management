from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from django.forms.models import model_to_dict
from task.models import *
from rest_framework import status
from django_mailbox.models import MessageAttachment, Message
import base64
import email

from django.shortcuts import render,get_object_or_404,HttpResponseRedirect
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect

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
		for dt in msg_obj:
			response["data"] = {
								"id " :dt.id,
								"subject":dt.subject						
						}
			response_list.append(response["data"])
		return render(request, 'pool.html', {'response':response_list})

	def post(self,request):
		msg_obj  = Message.objects.all()
		task_status = True
		for msgs in msg_obj:
			var = base64.b64decode(msgs.body)
			data = var.decode('ascii')
			email_message = email.message_from_string(data)
			body = ''
			for part in email_message.walk():
				if part.get_content_type() == "text/plain": # ignore attachments/html
					body = part.get_payload()
			Task.objects.get_or_create(task_id=msgs.id,task_name=msgs.subject,task_description=body,task_status=task_status)
		return Response(status=status.HTTP_200_OK)

class getails_category(APIView):
	def get(self,request):
		catgory_id = request.GET.get('catgory_id', None)
		task_pool_obj = task_pool.objects.filter(id=catgory_id)
		data = list(task_pool_obj.values())
		return Response(data,status=status.HTTP_200_OK)

# @csrf_exempt
	def post(self,request):
		msg_id = request.data.get('id', None)
		print(msg_id)
		c = request.data.get('category_id', None)
		print(c)
		cat_obj = category.objects.get(category_id=request.data.get('category_id', None))
		print(cat_obj)
		cat_name = cat_obj.category_name
		msg_obj  = Message.objects.filter(id = msg_id)
		for msgs in msg_obj:
			msg_attach = MessageAttachment.objects.filter(message=msgs.id).values()
			if msg_attach:
				msg_atch_id = msg_attach[0]['id']
			else:
				msg_atch_id = '0'
			var = base64.b64decode(msgs.body)
			data = var.decode('ascii')
			email_message = email.message_from_string(data)
			# this will loop through all the available multiparts in mail
			for part in email_message.walk():
				if part.get_content_type() == "text/plain": # ignore attachments/html
					body = part.get_payload()
					if cat_name in body:
						task_pool.objects.create(category=cat_obj,mailbox_id=int(msgs.mailbox_id),subject=msgs.subject,
								message_id=msgs.message_id,in_reply_to_id=msgs.in_reply_to_id,from_header=msgs.from_header,
								to_header=msgs.to_header,outgoing = msgs.outgoing,body=body,encoded=msgs.encoded,
								processed=msgs.processed,read=msgs.read,eml= msgs.eml, msg_attch_id=msg_atch_id)
						
						return JsonResponse({"message":"created"}, status=status.HTTP_200_OK)
					else:
						return JsonResponse({"message":"Not created"},status = status.HTTP_400_BAD_REQUEST)

	
class category_get(APIView):
	def get(self,request):
		response = {}
		category_list = []
		message_list  = []
		cat_qs = category.objects.all()
		for dt in cat_qs:
			response["data"] = {
								"category_id" :dt.category_id,
								"category_name":dt.category_name						
						}
			category_list.append(response["data"])

		msg_obj  = Message.objects.all()
		for dt in msg_obj:
			response["data"] = {
								"id" :dt.id,
								"subject":dt.subject						
						}
			message_list.append(response["data"])
		return render(request, 'pool.html', {'category_list':category_list, 'message_list':message_list})


