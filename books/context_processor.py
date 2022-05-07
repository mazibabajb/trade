from.models import Book,Category
from django.core.paginator import Paginator , EmptyPage




def book_listings(request):
	bookcategory = request.GET.get('bookcategory ')
	if bookcategory  == None:
		books = Book.objects.all()
	else:
		books = Book.objects.filter(category__name=bookcategory)	
        	
	bookCategories = Category.objects.all()
	page_num = request.GET.get('page', 1)
	p = Paginator(books, 10)

	try:
		page = p.page(page_num)

	except EmptyPage:
		page = p.page(2)
    
	context = {	'books':page ,
				'bookCategories':bookCategories,
				}
	return context