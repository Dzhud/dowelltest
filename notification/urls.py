from django.urls import path
from . import views

urlpatterns = [	
	path('notif/', views.getNotif, name='getNotif'),
]