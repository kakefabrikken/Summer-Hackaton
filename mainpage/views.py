from django.http import HttpResponse
from django.shortcuts import render

def index(request):
	return render(request, 'mainpage/index.html')
	#return HttpResponse('Hello world from Django!')
