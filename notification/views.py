from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from . import views
from .models import Notification


def getNotif(request):
	itms = Notification.objects.all()
	itms = [(i.product_name, i.url, i.status, i.date) for i in itms]
	return JsonResponse({"Products": itms})	