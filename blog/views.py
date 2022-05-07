from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, View
from.models import *


# Create your views here.

def blogsearchbar(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        posts = Post.objects.all().filter(title=search)
        return render(request,"front_end_templates/blog_search.html",{'posts':posts})

def Post_view(request):
	context = {	
				'title':"Tradebay Blog Post",
        		'description': 'These are tradebay blog post'
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
		'title':posts.seo_title,
        'description':posts.seo_description
	}
	return render(request, "front_end_templates/blog_detail.html",context)


