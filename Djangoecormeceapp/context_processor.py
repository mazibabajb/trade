from multiprocessing import context
from.models import Products, SubCategories
from django.core.paginator import Paginator , EmptyPage



def product_listing(request):
    productCategory = request.GET.get('productCategory')
    if productCategory == None:
        products = Products.objects.all()
    else:
        products = Products.objects.filter(subcategories_id__title=productCategory)	
        	
    productCategories = SubCategories.objects.all()
    page_num = request.GET.get('page', 1)
    p = Paginator(products, 7)
    try:
        page = p.page(page_num)

    except EmptyPage:
	    page = p.page(1)
    
    context = {	'products':page ,
				'productCategories':productCategories,
                'title':'Tradebay Online shopping  Phones ||  TVS  ||',
                'description': 'description'
				}
    return context            
    