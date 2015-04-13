from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

#def TestView(request, **kwargs):
#	return HttpResponse("Hello World!")

# splashview: a subset of templateview
class SplashView(TemplateView): # instance of TemplateView, a subset
	template_name = 'index.html'