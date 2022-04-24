
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
    context = {
		'books': books,	
	}
    return render(request, "books/book_detail.html",context)    


def book_list(request):
	return render(request, 'books/book_list.html')
