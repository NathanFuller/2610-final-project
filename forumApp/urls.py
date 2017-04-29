from django.conf.urls import url

from . import views

app_name = 'forumApp'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^compose', views.compose, name='compose'),
	url(r'^save', views.save, name='save'),
	url(r'^vote', views.vote, name='vote'),
]
