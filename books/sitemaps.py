from django.contrib.sitemaps import  Sitemap
from .models import Book


class BookSitemap(Sitemap):
    def items(self):
        return  Book.objects.all()



