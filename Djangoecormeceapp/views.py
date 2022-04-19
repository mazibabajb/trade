from itertools import product
from multiprocessing import context
from turtle import title
from venv import create
from django.forms.forms import Form
from django.shortcuts import render,redirect,get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import HttpResponse,HttpResponseRedirect, request
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from django.views.generic.detail import DetailView
from Djangoecormeceapp.models import *
from blog.models import Post
from django.core.paginator import Paginator , EmptyPage
from cart.forms import CartAddProductForm
from django.contrib import messages
from accounts.models import Profile



# Create your views here.
def home(request):
    is_onsale = Products.objects.filter(is_onsale = True).order_by('-id')[:4]
    is_hot = Products.objects.filter(is_hot = True).order_by('-id')[:4]
    context = {
        'is_hot': is_hot,
        'is_onsale': is_onsale,
        'title':'Tradebay Online shopping  Phones ||  TVS  ||',
        'description': 'Tradebay is an online shopping platform  in zimbabwe'
    }
    return render(request,"front_end_templates/index.html",context)

def demoPage(request):
    return HttpResponse("demo Page")


def erro_page(request,exception):
    context = {
        'title':'Tradebay Online shopping  Phones ||  TVS  ||',
        'description': 'Tradebay is an online shopping platform  in zimbabwe'
    }
    return render(request,"front_end_templates/error.html",context)

def liked_post(request):
    user = request.user
    if request.method == 'POST':
        product_id = request.POST.get('products_id')
        product_obj = Products.objects.get(id=product_id)

        if user in product_obj.liked.all():
            product_obj.liked.remove(user)
        else:
            product_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user,product_id=product_id)

        if not created:
            if like.value == 'like':
                like.value == 'unlike'
            else:
                like.value == 'like'
        like.save()
    return redirect('product_list_view')
    

def emailsubscription(request):
    if request.method == 'POST':
        email_sub = Email()
        email = request.POST.get('email')
        email_sub.email = email
        email_sub.save()
        messages.success(request, 'Thank you for subscribing for our newsletters')
    return render(request,"front_end_templates/index.html")    

        

    

def searchbar(request):
    if request.method == 'GET':
        seacrh_term = Search()
        search = request.GET.get('search')
        products = Products.objects.all().filter(product_name = search)
        seacrh_term.search = search
        seacrh_term.save()
    return render(request,"front_end_templates/search.html",{'products':products})

       


def home_product_detail(request, id, url_slug):
    products = Products.objects.get(id=id,url_slug=url_slug)
    related_products = Products.objects.filter(subcategories_id = products.subcategories_id).exclude(id=id)[:2]
    context = {
		'products': products,
        'related_product':related_products,
        
		
	}
    return render(request, "front_end_templates/products_detail.html",context)



def Product_view(request):
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
				}
	return render(request, 'front_end_templates/products_list_view.html',context)


def get_ip(request):
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def product_detail(request, id):
    product = get_object_or_404(Products,id=id)
    ip = request.META["REMOTE_ADDR"]
    if not ProductViewCount.objects.filter(product=product,session = request.session.session_key):
        veiw = ProductViewCount(product=product,ip_address=ip,session = request.session.session_key)
        veiw.save()
    product_veiw_counter = ProductViewCount.objects.filter(product=product)
    products = Products.objects.get(id=id)
    product_images = ProductMedia.objects.all()
    related_products = Products.objects.filter(subcategories_id = products.subcategories_id).exclude(id=id)[:2]
    cart_product_form = CartAddProductForm()
    context = {
		'products': products,
        'cart_product_form':cart_product_form,
        'related_products': related_products,
        'product_images': product_images,
        'title':products.title,
        'description':products.description ,
        'product_veiw_counter':product_veiw_counter
		
	}
    return render(request, "front_end_templates/products_detail.html",context)

def addcomment(request, id):
    url = request.META.get('HTTP_REFERER')
    #return HttpResponse(url)
    if request.method == 'POST':
        form = Commentform(request.POST)
        if form.is_valid():
            data = ProductReviews()
            data.review_comment = form.cleaned_data['review_comment']
            data.ip = request.META.get('REMOTE_ADDR')
            data.product_id = id
            currenr_user = request.user
            data.user_id=currenr_user.id
            data.save()
            messages.success(request, 'your review has been sent thank you for your intrest')
            return HttpResponseRedirect(url)
            
    return HttpResponseRedirect(url)
    

class ProductListView(ListView):     
    model = Products
    template_name = "front_end_templates/products_list_view.html"
    paginate_by=2
    
    def get_queryset(self):
        filter_val = self.request.GET.get("filter","")
        order_by=self.request.GET.get("orderby","id")
        if filter_val !="":
            cat=Products.objects.filter(Q(title__contains=filter_val) |  Q(description__contains=filter_val)).order_by(order_by)
        else:
            cat=Products.objects.all().order_by(order_by)    
        return cat

    def get_context_data(self, **kwargs): 
        context=super(ProductListView,self).get_context_data(**kwargs)
        context["filter"]=self.request.GET.get("filter","")
        context["orderby"]=self.request.GET.get("orderby","")
        context["all_table_fields"]=Products._meta.get_fields()
        return context

	 

class ProductDetailView(DetailView):
    model = Products
    template_name = "front_end_templates/products_detail.html"


def AboutUs(request):
    context = {
        'title':'Tradebay Online  about us page ',
        'description': 'About tradebay '

    }
    return render(request,"front_end_templates/about-us.html",context)

def Faqs(request):
    context = {
        'title':'Tradebay  frequntly asked questions',
        'description': 'frequently asked questions'

    }
    return render(request,"front_end_templates/faqs.html",context)


def Payments(request):
    context = {
        'title':'Tradebay  paymeny systems',
        'description': 'how to make payments on tradebay'

    }
    return render(request,"front_end_templates/payments.html",context) 

def Deliveries(request):
    context = {
        'title':'Tradebay deliveries',
        'description': 'Tradebay  delivery system for puchachased products'

    }
    return render(request,"front_end_templates/deliveries.html",context)    

def terms(request):
    context = {
        'title':'Tradebay  terms and conditions ',
        'description': 'Tradebay terms and conditions of use '

    }
    return render(request,"front_end_templates/terms.html",context)

def Contact_Us(request):
    context = {
        'title':'Tradebay Online  contact us  ',
        'description': 'contact tradebay via phone or email'

    }
    if request.method == 'POST':
        contact = Contact_us()
        name = request.POST.get('name')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')
        comment = request.POST.get('comment')
        contact.name = name
        contact.email = email
        contact.telephone = telephone
        contact.comment= comment
        contact.save()
        messages.success(request, 'Your message has been sent we will contact you as ppossible')
    return render(request,"front_end_templates/contact-us.html",context)          
          
           

	
def BlogList(request):
    context = {
        'title':'Tradebay Online shopping  Phones ||  TVS  ||',
        'detail': 'Tradebay is an online shopping platform  in zimbabwe'

    }
    return render(request,"front_end_templates/blog_list.html",context) 


def BlogDetail(request):
    context = {
        'title':'Tradebay Online shopping  Phones ||  TVS  ||',
        'detail': 'Tradebay is an online shopping platform  in zimbabwe'

    }
    return render(request,"front_end_templates/blog_detail.html",context) 



def adminLogin(request):
    return render(request,"admintemplates/login.html")   


def adminLoginProcess(request):
    username=request.POST.get("username")  
    password=request.POST.get("password") 


    user=authenticate(request=request,username=username,password=password)  
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error in Login! Invalid login details")
        return HttpResponseRedirect(reverse("admin_login"))


def adminLogoutProcess(request):
    logout(request)
    messages.success(request,"Logout Successfully")
    return HttpResponseRedirect(reverse("home"))
