from django.urls import path
from task.views import *

urlpatterns= [
    path('task_details', task_data.as_view(),name='taskdetails'),
    path('get_task', get_task_details.as_view(),name='taskdetails'),
    path('mail_task_details', mail_task_details.as_view(),name='mail_task_details'),
    path('getails_category', getails_category.as_view(),name='getails_category'),



]