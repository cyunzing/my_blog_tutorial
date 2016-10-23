from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404


# Create your views here.
def home(request):
	post_list = Article.objects.all()
	return render(request, 'home.html', {'post_list': post_list})
	#return HttpResponse('Hello World, Django')


def detail(request, id):
	try:
		post = Article.objects.get(id = str(id))
#		post = Article.objects.all()[int(my_args)]
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'post.html', {'post': post})
#	_str = ('title = %s,\ncategory = %s,\ndate_time = %s,\ncontent = %s' % (post.title, post.category, post.date_time, post.content))
#	return HttpResponse(_str)


def test(request):
	return render(request, 'test.html', {'current_time': datetime.now()})


def archives(request):
	try:
		post_list = Article.objects.all()
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'archives.html', {'post_list': post_list, 'error': False})


def about_me(request):
	return render(request, 'aboutme.html')


def search_tag(request):
	try:
		post_list = Article.objects.filter(category_iexact = tag)
	except Article.DoesNotExist:
		raise Http404
	return render(request, 'tag.html', {'post_list': post_list})
	
