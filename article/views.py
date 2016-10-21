from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime


# Create your views here.
def home(request):
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list': post_list})
	#return HttpResponse('Hello World, Django')


def detail(request, my_args):
	post = Article.objects.all()[int(my_args)]
	_str = ('title = %s,\ncategory = %s,\ndate_time = %s,\ncontent = %s' % (post.title, post.category, post.date_time, post.content))
	return HttpResponse(_str)


def test(request):
	return render(request, 'test.html', {'current_time': datetime.now()})

