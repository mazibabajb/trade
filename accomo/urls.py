from django.urls import path
from accomo import views

urlpatterns = [
    path('property_list/',views.Property_view,name="property_list"),
    path('property/<int:id>/',views.Property_detail, name ='property_detail'),
    path('liked-this-post/',views.liked_property, name='liked-property'),
    
  
]