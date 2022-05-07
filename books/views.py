
from unicodedata import category
from django.shortcuts import render
from .models import Book, Category ,Author
from django.http import HttpResponse, response
from django.core.paginator import Paginator , EmptyPage



# Create your views here.
def download(request,path):
    file_path = os.path.join(settings.MEDIA_ROOT.path)
    if os.path.exists(file_path):
        with open(file_path, 'rb')as fh:
            response=HttpResponse(fh.read(), content_type="application/adminupload")
            response['Content-Desposition']= 'inline;filename=' +os.path.basename(file_path)
            return response
    
    raise Http404


def book_detail(request, id):
    books = Book.objects.get(id=id)
    related_topics = Book.objects.filter(category = books.category).exclude(id=id)[:2]
    context = {
		'books': books,
        'title': books.seo_title,
        'description':books.seo_description,
        'related_topics':related_topics
	}
    return render(request, "books/book_detail.html",context)    


def book_list(request):
    context= {
        'title':'Tradebay book list',
        'description':'Books from Authour around zimbabwe',

    }
    return render(request, 'books/book_list.html',context)
