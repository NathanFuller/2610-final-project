import re
from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Statement
from django.core.urlresolvers import reverse
from django.utils.datastructures import MultiValueDictKeyError


# Create your views here.
def index(request):
	"""This is the main page of the app!"""
	statement_list = Statement.objects.filter()[::-1]
	return render(request, 'forumApp/index.html', {'statement_list':statement_list})
#render() gets the request,  a path to the template, and the "context" (this is just to tie variables in the template to the Python objects.


def compose(request):
	"""This is where the user will enter their Statement."""
	return render(request, 'forumApp/compose.html', {})

def save(request):
	""""An action page!!"""
	Statement.objects.create(author=request.POST['auth'], content=request.POST['content'])
	return HttpResponseRedirect('/forumApp/')

def vote(request):
	try:
		sid = request.POST['up']
		up = True
	except MultiValueDictKeyError:
		sid = request.POST['down']
		up = False
	s = Statement.objects.get(pk=sid)
	if up:
		s.votes+=1
	else:
		s.votes-=1
	s.save()
	return HttpResponseRedirect('/forumApp/#'+str(sid))
