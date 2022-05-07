from.models import Property, Category
from django.core.paginator import Paginator , EmptyPage

# Create your views here.

def Property_listings(request):
	propertyCategory = request.GET.get('propertyCategory')
	if propertyCategory == None:
		property = Property.objects.all()
	else:
		property = Property.objects.filter(category__name=propertyCategory)	

	propertyCategories = Category.objects.all()
	page_num = request.GET.get('page', 1)
	p = Paginator(property, 10)

	try:
		page = p.page(page_num)

	except EmptyPage:
		page = p.page(1)
    	
	context = {	'property':page ,
				'propertyCategories':propertyCategories,
				}
	return context