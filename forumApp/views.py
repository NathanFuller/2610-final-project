from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.
def index(request):
	return HttpResponse("This is the main page of the app! There ain't nothin else here for now.")
