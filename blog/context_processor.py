from turtle import title
from. models import Post, PostCategory
from django.core.paginator import Paginator , EmptyPage


def post_list(request):
    
    is_trending = Post.objects.filter(is_trending = True).order_by('-id')
    postCategory = request.GET.get('postCategory')
    if postCategory == None:
        posts = Post.objects.all()
    else:
        posts = Post.objects.filter(category__name=postCategory)	

    postCategories = PostCategory.objects.all()
    page_num = request.GET.get('page', 1)
    p = Paginator(posts, 5)

    try:
        page = p.page(page_num)

    except EmptyPage:
        page = p.page(1)
    	
    context = {	'posts':page ,
				'is_trending':is_trending ,
				'postCategories':postCategories,
				'title':"The tradebay blog post",
        		'description': 'These are tradebay blog post'
				}
    return context	