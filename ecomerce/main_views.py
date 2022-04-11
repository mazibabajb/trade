from django.shortcuts import render
from Djangoecormeceapp.models import  Products

from django.contrib import messages
from accounts.models import Profile


def home(request, *args, **kwargs):
    code = str(kwargs.get('ref_code'))
    try:
        profile = Profile.objects.get(code=code)
        request.session['ref_profile'] = profile.id
        print('id', profile)
    except:
        pass
    print(request.session.get_expiry_age())
    is_onsale = Products.objects.filter(is_onsale = True).order_by('-id')[:4]
    is_hot = Products.objects.filter(is_hot = True).order_by('-id')[:4]
    


    context = {
        'code':code,
        'is_hot': is_hot,
        'is_onsale': is_onsale,
        'title':'Tradebay Online shopping  Phones ||  TVS  ||',
        'description': 'Tradebay is an online shopping platform  in zimbabwe'
    }
    return render(request,"front_end_templates/index.html",context)
