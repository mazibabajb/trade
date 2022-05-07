from django.shortcuts import render,redirect
from.models import *
from django.core.paginator import Paginator , EmptyPage

# Create your views here.

def Property_view(request):
    context = {	
				'title':'Tradebay property list',
        		'description': 'Properties for sale to rent in zimbabwe'
				}
    return render(request, 'property_list.html',context)	

def Property_detail(request,id):
    property = Property.objects.get(id=id)
    ip = request.META["REMOTE_ADDR"]
    if not PropertyViewCount.objects.filter(property=property,session = request.session.session_key):
        veiw = PropertyViewCount(property=property,ip_address=ip,session = request.session.session_key)
        veiw.save()
    property_veiw_counter = PropertyViewCount.objects.filter(property=property)
    related_properties = Property.objects.filter(category = property.category).exclude(id=id)[:2]
    context = {
		'property': property,	
        'property_veiw_counter':property_veiw_counter,
        'title':property.seo_title,
        'description': property.seo_description,
        'related_properties':related_properties
	}
    return  render(request, "property_detail.html",context)



def liked_property(request):
    user = request.user
    if request.method == 'POST':
        property_id = request.POST.get('property_id')
        property_obj = Property.objects.get(id=property_id)

        if user in property_obj.likes.all():
            property_obj.liked.remove(user)
        else:
            property_obj.liked.add(user)

        like, created = Like.objects.get_or_create(user=user,property_id=property_id)

        if not created:
            if like.value == 'like':
                like.value == 'unlike'
            else:
                like.value == 'like'
        like.save()
    return redirect('property_list')