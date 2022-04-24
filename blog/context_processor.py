from turtle import title
from. models import Post, PostCategory
from django.core.paginator import Paginator , EmptyPage


def post_list(request):
    post_title = Post.objects.filter(title=title)
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
				'post_title':post_title,
        		'description': 'These are tradebay blog posts'
				}
    return context	