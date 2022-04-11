from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, View
from.models import *
from django.core.paginator import Paginator , EmptyPage

# Create your views here.

def blogsearchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Post.objects.all().filter(title=search)
        return render(request,"front_end_templates/blog_search.html",{'posts':posts})

def Post_view(request):
	is_trending = Post.objects.filter(is_trending = True).order_by('-id')
	postCategory = request.GET.get('postCategory')
	if postCategory == None:
		posts = Post.objects.all()
	else:
		posts = Post.objects.filter(category__name=postCategory)	

	postCategories = PostCategory.objects.all()
	page_num = request.GET.get('page', 3)
	p = Paginator(posts, 1)

	try:
		page = p.page(page_num)

	except EmptyPage:
		page = p.page(1)
    	
	context = {	'posts':page ,
				'is_trending':is_trending ,
				'postCategories':postCategories,
				'title':'Tradebay blog posts ',
        		'description': 'These are tradebay blog posts'
				}
	return render(request, 'front_end_templates/blog_list.html',context)	


def blog_detail(request, id):
	posts = Post.objects.get(id=id)
	is_trending = Post.objects.filter(is_trending = True).order_by('-id')
		
	postCategories = PostCategory.objects.all()
	context = {
		'posts': posts,
		'is_trending':is_trending ,
		'postCategories':postCategories,
		'title':posts.title,
        'description':posts.description
	}
	return render(request, "front_end_templates/blog_detail.html",context)


